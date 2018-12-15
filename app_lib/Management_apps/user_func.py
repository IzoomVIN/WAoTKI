import pickle as pcl
import time
from tkinter import TclError
from threading import Thread
from app_lib.Windows_a import Windows
from app_lib.Management_apps import auth_func, view_func, add_tabel_func


# Наш мини обработчик событий в окне пользователя.
#   USER FUNC
def user_existing_table_event(ev):
    table = user_window.existing_table.curselection()
    if len(table) == 1:
        user_window.view_button["state"] = "active"


def user_exit_button_event(ev):
    user_window.root.destroy()
    auth_func.auth_win()


def _open_table(name):
    with open("", "rb") as file:
        table = pcl.load(file)
    return table


def user_view_button_event(ev):
    if user_window.view_button["state"] != "active":
        return
    name = user_window.existing_table.curselection()[0]
    name = user_window.existing_table.get(name)
    name = "./app_lib/Database/table_data/{}.pkl".format(name)
    with open(name, "rb") as file:
        array = pcl.load(file)
    user_window.root.destroy()
    view_func.view_win(user_type=user_window.user_type,
                       array=array)


def user_add_button_event(ev):
    user_add_win(user_window.user_type)


def canvas_graphic():
    with open("./app_lib/Database/manager_data/color_array.pkl", "rb") as file:
        color_array = pcl.load(file)
    try:
        while True:
            for d in range(289, (288 + 225)):
                time.sleep(0.01)

                # меняем параметр цвета у всего что надо
                user_window.user_canvas.configure(bg=color_array[d - 289])

                # Сразу обновляем для того, чтобы видеть это
                user_window.root.update()

            for d in range((288 + 225), 289, -1):
                time.sleep(0.01)

                # меняем параметр цвета у всего что надо
                user_window.user_canvas.configure(bg=color_array[d - 289])

                # Сразу обновляем для того, чтобы видеть это
                user_window.root.update()
    except TclError:
        return


def list_table_inserting():
    list_name = []
    try:
        with open("./app_lib/Database/manager_data/table_list.pkl", "rb") as file:
            list_name = pcl.load(file)
    except IOError:
        with open("./app_lib/Database/manager_data/table_list.pkl", "wb"):
            pass
    except EOFError:
        pass

    for i in list_name:
        user_window.existing_table.insert("end", i)


#   USER ADD_TABLE FUNC
def update_second_data(ev):
    if user_add_table_window.cbox_to_first_date.get() == "":
        return
    date_from = user_add_table_window.cbox_to_first_date.get()
    for i in range(len(data_to_pars[0][1])):
        if date_from == data_to_pars[0][1][i]:
            date_from = i
            break
    user_add_table_window.cbox_to_second_date["values"] = data_to_pars[0][1][:date_from]
    return


def user_add_ok_button_event(ev):
    par = user_add_table_window.cbox_to_indicator.get()
    reg = user_add_table_window.cbox_to_region.get()
    date1 = user_add_table_window.cbox_to_first_date.get()
    date2 = user_add_table_window.cbox_to_second_date.get()
    name_file = user_add_table_window.name_of_new_table.get()
    array_for_parser = [[data_to_pars[1][0], par],
                        [data_to_pars[2][0], reg],
                        [data_to_pars[0][0], date1, date2]]

    u_t = user_add_table_window.u_t

    user_add_table_window.root.destroy()
    user_window.root.destroy()

    add_tabel_func.pars_run(array=array_for_parser,
                            name=name_file,
                            user_type=u_t)


def user_add_exit_button_event(ev):
    user_add_table_window.root.destroy()
    user_window.root.destroy()
    user_win(user_add_table_window.u_t)


#   CONTROL FUNC
def user_win(user_type):
    global user_window
    user_window = Windows.user_window_create(user_type)

    user_window.existing_table.bind("<Button-1>", user_existing_table_event)
    user_window.view_button.bind("<Button-1>", user_view_button_event)
    user_window.exit_button.bind("<Button-1>", user_exit_button_event)
    if user_type == "Admin":
        user_window.add_button.bind("<Button-1>", user_add_button_event)

    # добавляем таблицы в лист таблиц
    list_table_inserting()

    # создаем доп поток для графики
    graph = Thread(canvas_graphic())
    # стартуем доп поток
    graph.start()

    user_window.root.mainloop()


def user_add_win(user_type):
    global user_add_table_window, data_to_pars
    user_add_table_window = Windows.user_add_table_window_create()
    user_add_table_window.u_t = user_type
    data_to_pars = add_tabel_func.array_and_dict_realise()

    user_add_table_window.cbox_to_indicator["values"] = data_to_pars[1][1]
    user_add_table_window.cbox_to_region["values"] = data_to_pars[2][1]
    user_add_table_window.cbox_to_first_date["values"] = data_to_pars[0][1]
    user_add_table_window.cbox_to_second_date["values"] = data_to_pars[0][1]

    user_add_table_window.cbox_to_first_date.bind("<Leave>", update_second_data)
    user_add_table_window.ok_button.bind("<Button-1>", user_add_ok_button_event)
    user_add_table_window.exit_button.bind("<Button-1>", user_add_exit_button_event)

    user_add_table_window.root.mainloop()
