import requests
import time
import os
import pickle as pkl
import pandas as pd
from tkinter import TclError
from threading import Thread
from app_lib.Windows_a import Windows
from app_lib.Management_apps import user_func
from bs4 import BeautifulSoup


# Preliminary processing
def _preliminary_processing():
    web_page = '''http://www.banki.ru/banks/ratings/'''
    r = requests.get(web_page)
    data = BeautifulSoup(r.text, "html.parser")
    return data


def _dict_of_region(data):
    data_region_href = {}
    data_region_all = data.findAll("script", attrs={"id": "region-popup-template"})
    data_region_all = BeautifulSoup(data_region_all[0].text, "html.parser")
    data_region_all = data_region_all.findAll('a')

    for i in data_region_all:
        data_region_href[i.text.strip()] = i['href']

    for key in data_region_href:
        data_region_href[key] = data_region_href[key].replace("/banks/ratings/?", "")
        if data_region_href[key] == "":
            data_region_href[key] = None

    return data_region_href


def _dict_of_indicator(data):
    data_indicator_href = {}
    data_indicator_all = data.findAll("script", attrs={"id": "indicator-popup-template"})
    data_indicator_all = BeautifulSoup(data_indicator_all[0].text, "html.parser")
    data_indicator_all = data_indicator_all.findAll('a', attrs={"class": "rating-parameter-list--item__link active"})

    for i in data_indicator_all:
        data_indicator_href[i.text.strip()] = i['href']

    for key in data_indicator_href:
        data_indicator_href[key] = data_indicator_href[key].replace("/banks/ratings/?", "")

    return data_indicator_href


def _dict_of_date(data):
    date_array = {}
    date = data.findAll("th", attrs={"class": "table-title font-normal"})

    for i in date[0].find_all('option'):
        date_array[i.text] = i["value"]

    return date_array


def _dict_realise():
    data = _preliminary_processing()

    dod = _dict_of_date(data)
    doi = _dict_of_indicator(data)
    dor = _dict_of_region(data)

    return [dod, doi, dor]


def array_and_dict_realise():
    sup = _dict_realise()

    kod = [i for i in sup[0].keys()]
    koi = [i for i in sup[1].keys()]
    kor = [i for i in sup[2].keys()]

    return [[sup[0], kod],
            [sup[1], koi],
            [sup[2], kor]]


# Parser
def _preliminary_processing_to_parser(array):
    '''Получает на вход массив [[{параметры}, выбранный пользователем параметр],
                                [{регионы}, выбранный пользователем регион],
                                [{даты}, выбранная пользователем дата начала,
                                         выбранная пользователем дата конца]]'''

    web_page = '''http://www.banki.ru/banks/ratings/'''
    param_ar = []
    if array[0][1] != "":
        param_ar.append(array[0][0][array[0][1]])
    if array[1][1] != "" and array[1][1] != "все регионы":
        param_ar.append(array[1][0][array[1][1]])
    if array[2][1] != "":
        date_from = array[2][1]
    if array[2][2] != "":
        date_to = array[2][2]

    date = [i for i in array[2][0].keys()]
    for i in range(len(date)):
        if date[i] == date_from:
            date = date[:i + 1]
            break
    for i in range(len(date)):
        if date[i] == date_to:
            date = date[i:]
            break
    for i in range(len(date)):
        date[i] = array[2][0][date[i]]

    if len(param_ar) != 0:
        ind_and = len(param_ar) - 1
        web_page = web_page + '?'
        for par in param_ar:
            web_page += par
            if ind_and > 0:
                web_page += "&"
                ind_and -= 1

    return [web_page, date]


def _parser(date_2):
    global web_page, reg, pb
    w_p_pars = web_page + "&date2={}".format(date_2)

    i = 1  # счетчик страниц
    table = []  # итоговая таблица

    while True:  # цикл обработки информации
        FLAG = True  # наш флаг по которому проверяется смысл дальнейшей работы
        w_p_pars = w_p_pars + "&PAGEN_1={}".format(i)  # добавляем параметр страницы для сайта
        pars = requests.get(w_p_pars)  # получение html разметки в виде текста
        data_pars = BeautifulSoup(pars.text, "html.parser")  # преобразование в соуп для удобства обработки

        d_p = data_pars.findAll("tr", attrs={"data-test": "rating-table-item"})
        for dat in d_p:  # цикл пробега по определенным элементам в разметке
            line = []
            line.append(str(dat.findAll('td')[1].find('a').text.strip()))  # Имя банка
            line.append(str(dat.findAll('td')[1].findAll('div')[1].text.split(",")[0].strip()))  # Лицензия
            try:
                line.append(str(dat.findAll('td')[1].findAll('div')[1].text.split(",")[1].strip()))  # Регион
            except IndexError:
                line.append(str(reg))
            line.append(dat.findAll('td')[3].text.strip().replace(" ", ""))  # Данные за Data_to
            # проверка (потому как страницы по другому не проверить, или я не нашел)
            for j in table:  # пробег по строкам нашей таблицы
                if line == j:  # проверка спарсеной строки на повтор
                    FLAG = False
                    break

            # выход из внутреннего цикла по флагу
            if FLAG == False:
                break

            table.append(line)  # добавление строки в таблицу

        w_p_pars = w_p_pars.replace("&PAGEN_1={}".format(i), '')  # убираем параметр страницы для сайта
        pb.log_box.insert("end", "страница {} по дате {} : получено {} записей".format(i,
                                                                                       date_2,
                                                                                       len(table)))

        # выход из внешнего цикла по флагу
        if FLAG == False:
            break

        i += 1  # приращение счетчика

    pb.window.update()
    return table


def _run_pars(array, table_name):
    global web_page
    web_page = array[0]
    full_table = {"name": table_name}

    for date in array[1]:
        date_key = "{} {}".format(date.split("-")[1], date.split("-")[0])
        full_table[date_key] = _parser(date)
        time.sleep(0.1)
        pb.run_pb()
        pb.window.update()

    return full_table


# AFTER PARSER
def pd_table(data):
    array_keys = []
    for i in data.keys():
        if i == "name":
            continue
        array_keys.append(i)

    data_new = pd.DataFrame(data[array_keys[0]], columns=["Name", "License", "Area", array_keys[0]])
    del array_keys[0]

    for i in array_keys:
        data_time = pd.DataFrame(data[i], columns=["Name", "License", "Area", i])
        data_new = data_new.merge(data_time)

    return data_new


# preparing table to pickle
def array_to_table_pickle(pd_df_table, name):
    columns = [str(i) for i in pd_df_table.columns]

    table = []
    for i in pd_df_table.values:
        line = []

        for j in range(len(i)):
            if j < 3:
                line.append(str(i[j]))
                continue
            i[j] = i[j].replace("−", "-")
            i[j] = i[j].replace("н/д", "")
            i[j] = i[j].replace(",", ".")
            if i[j] == "":
                line.append(None)
                continue
            try:
                line.append(int(i[j]))
            except ValueError:
                line.append(float(i[j]))

        table.append(line)

    return [name, columns, table]


# add name of table in user home list
def add_table_in_list(name):
    try:
        with open("./app_lib/Database/manager_data/table_list.pkl", "rb") as file:
            name_list = pkl.load(file)
    except EOFError:
        name_list = []

    name_list.append(name)

    with open("./app_lib/Database/manager_data/table_list.pkl", "wb") as file:
        pkl.dump(name_list, file)

    pb.log_box.insert("end", "таблица добавлена в список как {}".format(name))
    pb.run_pb()
    pb.window.update()


# Save to pickle and run parser func
def _to_pickle(array, name, table_name):
    array = _run_pars(array=array, table_name=table_name)

    data = pd_table(data=array)
    array = array_to_table_pickle(pd_df_table=data, name=array["name"])

    add_table_in_list(name)

    F = False
    my_dir = os.listdir("./app_lib/Database/")
    for i in my_dir:
        if i == "table_data":
            F = True
            break

    if F == False:
        os.mkdir("./app_lib/Database/table_data")

    with open("./app_lib/Database/table_data/{}.pkl".format(name), "wb") as file:
        pkl.dump(array, file)

    pb.log_box.insert("end", "таблица сохранена как {}".format(name))
    pb.run_pb()
    pb.window.update()


def graph_for_pb():
    pb.rpb.start()
    with open("./app_lib/Database/manager_data/color_array.pkl", "rb") as file:
        color_array = pkl.load(file)
    try:
        while True:
            for d in range(289, (288 + 225)):
                time.sleep(0.01)

                # меняем параметр цвета у всего что надо
                pb.main_frame.configure(bg=color_array[d - 289])
                pb.label.configure(bg=color_array[d - 289])

                # Сразу обновляем для того, чтобы видеть это
                pb.window.update()

            for d in range((288 + 225), 289, -1):
                time.sleep(0.01)

                # меняем параметр цвета у всего что надо
                pb.main_frame.configure(bg=color_array[d - 289])
                pb.label.configure(bg=color_array[d - 289])

                # Сразу обновляем для того, чтобы видеть это
                pb.window.update()
    except TclError:
        return


def _exit(ev):
    pb.exit(ev)
    user_func.user_win(pb.user_type)


def pars_run(array, name, user_type):

    global reg, pb

    reg = array[1][1]
    table_name = '''Данные о "{}" в регионе: "{}"'''.format(array[0][1], reg)
    array = _preliminary_processing_to_parser(array)
    pb = Windows.MyProgressBarWindow(num=len(array[1]) + 2, user_type=user_type)

    graph_thread = Thread(daemon=True,
                          target=graph_for_pb)

    pars_thread = Thread(daemon=True,
                         target=_to_pickle,
                         args=(array, name, table_name))

    pb.ok_button.bind("<Button-1>", _exit)
    graph_thread.start()
    pars_thread.start()

    pb.window.mainloop()
