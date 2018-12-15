# импортируем библиотеку, так как она идет в стандартном пакете, ее не надо дозагружать
import tkinter as tk
from tkinter import ttk


class Window():
    def __init__(self, name, type_window="Main", icon_adress=None):
        if type_window == "Main":
            self.root = tk.Tk(className=name)
        elif type_window == "TopLevel":
            self.root = tk.Toplevel()
            self.root.title = name

        if icon_adress is not None:
            self.root.iconbitmap(icon_adress)

    def frozen_size(self, width, height):
        self.width = width
        self.height = height

        self.root.resizable(width=False, height=False)

        self._centering_window()

    def _centering_window(self):
        win_width = self.root.winfo_screenwidth()
        win_height = self.root.winfo_screenheight()
        x = (win_width - self.width) / 2
        y = (win_height - self.height) / 2
        self.root.geometry("{}x{}+{}+{}".format(self.width, self.height, int(x), int(y)))


color_frame = "#99f2f2"
color_button = "#64e2f9"
color_exit_button = "#ff2222"


#   AUTH WINDOWS
# Функция для заполнения окна авторизыции.
def _frame_auth_create(window):
    window.canvas = tk.Canvas(window.root,
                              bg="#c7f8f8",
                              width=window.width,
                              height=window.height)
    window.canvas.pack()

    # создадим группировку для логина и пароля:
    window.login_password_frame = tk.LabelFrame(window.canvas,
                                                text="Authorization",
                                                labelanchor="n",
                                                relief="flat",
                                                bg=color_frame)
    window.login_password_frame.place(x=290, y=225)

    # добавим в нее текст над окошком логина и окно вдля ввода логина:
    window.login_label = tk.Label(window.login_password_frame,
                                  text="Enter login please!",
                                  width=30,
                                  bg=color_frame)
    window.login_text = tk.Entry(window.login_password_frame,
                                 width=30,
                                 justify="center")
    # а теперь запакуем все это:
    window.login_label.pack()
    window.login_text.pack()

    # тоже самое проделаем и для пароля:
    window.password_label = tk.Label(window.login_password_frame,
                                     text="Enter password please!",
                                     width=30,
                                     bg=color_frame)
    window.password_text = tk.Entry(window.login_password_frame,
                                    width=30,
                                    justify="center",
                                    show="*")
    window.password_label.pack()
    window.password_text.pack()

    # для удобства добавим фрейм для кнопок:
    window.but_box = tk.Frame(window.login_password_frame,
                              bg=color_frame)
    window.but_box.pack(side="bottom")

    # теперь добавим нам кнопку, которая будет отвечать за ввод данных
    window.ok_button = tk.Button(window.but_box,
                                 text='Ok',
                                 width=10,
                                 height=1,
                                 bg=color_button,
                                 activebackground=color_button)
    window.ok_button.pack(side="left")

    # теперь добавим нам кнопку, которая будет отвечать за регистрацию новых пользователей
    window.reg_button = tk.Button(window.but_box,
                                  text='Registration',
                                  width=12,
                                  height=1,
                                  bg=color_button,
                                  activebackground=color_button)
    window.reg_button.pack(side='left')

    # добавим кнопку выхода
    window.exit_button = tk.Button(window.canvas,
                                   text='Exit',
                                   width=8,
                                   height=1,
                                   relief="flat",
                                   bg="#c7f8e6",
                                   activebackground="#c7f8e6")
    window.exit_button.place(x=700, y=550)


# Функция для инициализации окна авторизыции.
def auth_window_create():
    auth_window = Window(type_window="Main",
                         name="Authorization",
                         icon_adress="./app_lib/Image/icon_auth.ico")

    # уберем возможность изменения размеров окна и зададим собственные размеры:
    auth_window.frozen_size(800, 600)

    _frame_auth_create(auth_window)
    return auth_window


# Функция для заполнения окна регистрации.
def _frame_auth_reg_create(window):
    # создадим фреймы
    window.user_canvas = tk.Canvas(window.root,
                                   width=window.width,
                                   height=window.height,
                                   bg=color_frame)
    window.user_canvas.pack()

    window.login_frame = tk.Frame(window.user_canvas,
                                  bg=color_frame)
    window.login_frame.place(x=10, y=30)

    window.password_frame = tk.Frame(window.user_canvas,
                                     bg=color_frame)
    window.password_frame.place(x=10, y=100)

    window.password_again_frame = tk.Frame(window.user_canvas,
                                           bg=color_frame)
    window.password_again_frame.place(x=10, y=160)

    # Соберем форму в фреймы:
    #   login_frame
    window.login_label = tk.Label(window.login_frame,
                                  text="Enter login please!",
                                  width=30,
                                  bg=color_frame)
    window.login_text = tk.Entry(window.login_frame,
                                 width=30,
                                 justify="center")
    # а теперь запакуем все это:
    window.login_label.pack()
    window.login_text.pack()

    #   password_frame
    window.password_label = tk.Label(window.password_frame,
                                     text="Enter password please!",
                                     width=30,
                                     bg=color_frame)
    window.password_text = tk.Entry(window.password_frame,
                                    width=30,
                                    justify="center")
    window.password_label.pack()
    window.password_text.pack()

    #   password_again_frame
    window.password_again_label = tk.Label(window.password_again_frame,
                                           text="Enter password please!",
                                           width=30,
                                           bg=color_frame)
    window.password_again_text = tk.Entry(window.password_again_frame,
                                          width=30,
                                          justify="center")
    window.password_again_label.pack()
    window.password_again_text.pack()

    # Теперь соберем кнопки
    window.ok_button = tk.Button(window.user_canvas,
                                 text='Ok',
                                 width=10,
                                 height=1,
                                 bg=color_button,
                                 activebackground=color_button)
    window.ok_button.place(x=24, y=(window.height - 50))

    window.exit_button = tk.Button(window.user_canvas,
                                   text='Exit',
                                   width=8,
                                   height=1,
                                   bg=color_exit_button,
                                   activebackground=color_exit_button)
    window.exit_button.place(x=(window.width - 94), y=(window.height - 50))

    # Добавим CheckButton
    s = ttk.Style()
    s.configure("TCheckbutton", background=color_frame)
    window.check_admin = ttk.Checkbutton(window.user_canvas,
                                         text='Admin',
                                         style="TCheckbutton")
    window.check_admin.place(x=(window.width - 94), y=(window.height - 80))


# Функция для инициализации окна регистрации.
def auth_reg_window_create():
    reg_window = Window(type_window="TopLevel",
                        name="Registration",
                        icon_adress="./app_lib/Image/icon_good_auth.ico")
    reg_window.frozen_size(width=240, height=300)

    _frame_auth_reg_create(reg_window)

    return reg_window


# Функция для заполнения окна подтверждения главного администратора.
def _frame_reg_main_admin_auth(window):
    window.canvas = tk.Canvas(window.root,
                              bg=color_frame,
                              width=window.width,
                              height=window.height)
    window.canvas.pack()

    # создадим группировку для логина и пароля:
    window.login_password_frame = tk.LabelFrame(window.canvas,
                                                text="Authorization Main Admin",
                                                labelanchor="n",
                                                relief="flat",
                                                bg=color_frame)
    window.login_password_frame.place(x=10, y=10)

    # добавим в нее текст над окошком логина и окно вдля ввода логина:
    window.login_label = tk.Label(window.login_password_frame,
                                  text="Enter login please!",
                                  width=30,
                                  bg=color_frame)
    window.login_text = tk.Entry(window.login_password_frame,
                                 width=30,
                                 justify="center")
    # а теперь запакуем все это:
    window.login_label.pack()
    window.login_text.pack()

    # тоже самое проделаем и для пароля:
    window.password_label = tk.Label(window.login_password_frame,
                                     text="Enter password please!",
                                     width=30,
                                     bg=color_frame)
    window.password_text = tk.Entry(window.login_password_frame,
                                    width=30,
                                    justify="center",
                                    show="*")
    window.password_label.pack()
    window.password_text.pack()

    # для удобства добавим фрейм для кнопок:
    window.but_box = tk.Frame(window.login_password_frame,
                              bg=color_frame)
    window.but_box.pack(side="bottom")

    # теперь добавим нам кнопку, которая будет отвечать за ввод данных
    window.ok_button = tk.Button(window.but_box,
                                 text='Ok',
                                 width=10,
                                 height=1,
                                 bg=color_button,
                                 activebackground=color_button)
    window.ok_button.pack(side="left")

    window.exit_button = tk.Button(window.but_box,
                                   text='Exit',
                                   width=10,
                                   height=1,
                                   bg=color_exit_button,
                                   activebackground=color_exit_button)
    window.exit_button.pack(side="right")


def reg_main_admin_auth_window_create(type_window):
    reg_main_admin_auth_window = Window(type_window=type_window,
                                        name="Registration",
                                        icon_adress="./app_lib/Image/icon_good_auth.ico")
    reg_main_admin_auth_window.frozen_size(width=240, height=300)

    _frame_reg_main_admin_auth(reg_main_admin_auth_window)

    return reg_main_admin_auth_window


#   USER WINDOWS
# Функция для заполнения окна пользователя.
def _frame_user_window_create(window):
    # создадим фреймы
    window.user_canvas = tk.Canvas(window.root,
                                   width=window.width,
                                   height=window.height,
                                   bg=color_frame)
    window.user_canvas.pack()

    window.existing_table_frame = tk.Frame(window.user_canvas,
                                           bg=color_frame)
    window.existing_table_frame.place(x=10, y=10)

    hor_scroll_frame = tk.Frame(window.existing_table_frame)
    hor_scroll_frame.pack(side='left')

    # создадим таблицу с таблицами
    window.existing_table = tk.Listbox(hor_scroll_frame,
                                       height=16,  # высота в строках
                                       width=30)  # ширина в символах)
    window.existing_table.pack()

    # создадим скроллбары для таблицы:
    scrollbar_hor = tk.Scrollbar(hor_scroll_frame, orient="horizontal")
    scrollbar_ver = tk.Scrollbar(window.existing_table_frame, orient="vertical")
    scrollbar_hor.pack(side='bottom', fill='x')
    scrollbar_ver.pack(side='right', fill='y')

    # свяжем листбокс с скроллбарами:
    # привязка скроллбара к листбоксу (по вертикали)
    scrollbar_ver['command'] = window.existing_table.yview
    window.existing_table['yscrollcommand'] = scrollbar_ver.set

    # привязка скроллбара к листбоксу (по горизонтали)
    scrollbar_hor['command'] = window.existing_table.xview
    window.existing_table['xscrollcommand'] = scrollbar_hor.set

    # создадим кнопки

    window.view_button = tk.Button(window.user_canvas,
                                   text='View Table',
                                   width=10,
                                   bg=color_button,
                                   activebackground=color_button,
                                   state="disabled")

    if window.user_type == "Admin":
        window.add_button = tk.Button(window.user_canvas,
                                      text='Add Table',
                                      width=10,
                                      bg=color_button)
        window.add_button.place(x=(window.width - 90),
                                y=10)
        window.view_button.place(x=(window.width - 90),
                                 y=46)
    else:
        window.view_button.place(x=(window.width - 90),
                                 y=10)

    window.exit_button = tk.Button(window.user_canvas,
                                   text='Exit',
                                   width=8,
                                   bg=color_exit_button)
    window.exit_button.place(x=(window.width - 76),
                             y=(window.height - 36))


# Функция для инициализации окна пользователя.
def user_window_create(user_type):

    user_window = Window(name="Home",
                         type_window="Main",
                         icon_adress="./app_lib/Image/icon_home_window.ico")
    user_window.frozen_size(width=320, height=300)

    user_window.user_type = user_type

    _frame_user_window_create(user_window)

    return user_window


# функция для заполнения окна добавления таблиц
def _frame_user_add_table_create(window):
    # создадим фреймы
    window.canvas = tk.Canvas(window.root,
                              width=window.width,
                              height=window.height,
                              bg=color_frame)
    window.canvas.pack()

    frame_full_parameters = tk.Frame(window.canvas,
                                     bg=color_frame)
    frame_full_parameters.place(x=15, y=15)

    button_frame = tk.Frame(frame_full_parameters,
                            bg=color_frame)
    button_frame.pack(side="bottom")

    window.none_frame = tk.Frame(frame_full_parameters,
                                 bg=color_frame,
                                 height=30,
                                 width=100)
    window.none_frame.pack(side="bottom")

    frame_to_name_of_new_table = tk.Frame(frame_full_parameters,
                                          bg=color_frame,
                                          bd=2)
    frame_to_name_of_new_table.pack(side="top", anchor="center")

    frame_to_indicator = tk.Frame(frame_full_parameters,
                                  bg=color_frame,
                                  bd=2)
    frame_to_indicator.pack(side="top", anchor="center")

    frame_to_region = tk.Frame(frame_full_parameters,
                               bg=color_frame,
                               bd=2)
    frame_to_region.pack(side="top", anchor="center")

    frame_to_first_date = tk.Frame(frame_full_parameters,
                                   bg=color_frame,
                                   bd=1)
    frame_to_first_date.pack(side="left", anchor="nw")

    frame_to_second_date = tk.Frame(frame_full_parameters,
                                    bg=color_frame,
                                    bd=1)
    frame_to_second_date.pack(side="right", anchor="ne")

    # теперь наполнение:
    #   названия:
    label_to_new_name = tk.Label(frame_to_name_of_new_table,
                                 text="Name of new table",
                                 font=("Arial", 13),
                                 justify="center",
                                 width=58,
                                 bg=color_frame)
    label_to_new_name.pack(side="top")

    label_to_indicator = tk.Label(frame_to_indicator,
                                  text="Indicator",
                                  font=("Arial", 13),
                                  justify="center",
                                  width=58,
                                  bg=color_frame)
    label_to_indicator.pack(side="top")

    label_to_region = tk.Label(frame_to_region,
                               text="Region",
                               font=("Arial", 13),
                               justify="center",
                               width=58,
                               bg=color_frame)
    label_to_region.pack(side="top")

    label_to_first_date = tk.Label(frame_to_first_date,
                                   text="First date",
                                   font=("Arial", 13),
                                   justify="center",
                                   width=24,
                                   bg=color_frame)
    label_to_first_date.pack(side="top")

    label_to_second_date = tk.Label(frame_to_second_date,
                                    text="Second date",
                                    font=("Arial", 13),
                                    justify="center",
                                    width=24,
                                    bg=color_frame)
    label_to_second_date.pack(side="top")

    #   варианты:
    window.name_of_new_table = tk.Entry(frame_to_name_of_new_table,
                                        font=("Arial", 13),
                                        justify="center",
                                        width=58)
    window.name_of_new_table.pack()

    window.cbox_to_indicator = ttk.Combobox(frame_to_indicator,
                                            width=58,
                                            font=("Arial", 13),
                                            justify="center" )
    window.cbox_to_indicator.pack()

    window.cbox_to_region = ttk.Combobox(frame_to_region,
                                         width=58,
                                         font=("Arial", 13),
                                         justify="center" )
    window.cbox_to_region.pack()

    window.cbox_to_first_date = ttk.Combobox(frame_to_first_date,
                                             width=24,
                                             font=("Arial", 13),
                                             justify="center")
    window.cbox_to_first_date.pack()

    window.cbox_to_second_date = ttk.Combobox(frame_to_second_date,
                                              width=24,
                                              font=("Arial", 13),
                                              justify="center" )
    window.cbox_to_second_date.pack()

    # кнопки
    window.ok_button = tk.Button(button_frame,
                                 text="Ok",
                                 width=10,
                                 bg=color_button,
                                 activebackground=color_button)
    window.ok_button.pack(side="left")

    window.exit_button = tk.Button(button_frame,
                                   text="Exit",
                                   width=10,
                                   bg=color_exit_button,
                                   activebackground=color_exit_button)
    window.exit_button.pack(side="right")


# функция для инициализации окна добавления таблиц
def user_add_table_window_create():
    user_add_table_window = Window(name="Add Table",
                                   type_window="TopLevel",
                                   icon_adress="./app_lib/Image/icon_home_window.ico")
    user_add_table_window.frozen_size(width=580, height=300)

    _frame_user_add_table_create(user_add_table_window)

    return user_add_table_window


#   VIEW WINDOW
# Функция для заполнения таблицы.
def _table_insert(window, array):
    for i in range(len(array[2])):
        window.table_list.insert("", text=str(i), index="end", values=tuple(j for j in array[2][i]))


# функция обработки канваса
def on_frame_configure(ev, canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))


# функция заполнения окна просмотра таблицы.
def _frame_view_window_create(window, array):
    # главный фрейм
    window.main_frame = tk.Frame(window.root,
                                 width=window.width,
                                 height=window.height,
                                 bg=color_frame)
    window.main_frame.pack()

    # название таблицы
    window.name_label = tk.Label(window.main_frame,
                                 font=("Arial", 12),
                                 text=array[0],
                                 width=129,
                                 justify="center",
                                 bg=color_frame)  # Лейбл для имени таблицы
    window.name_label.place(x=15, y=15)

    # Фрейм для вывода таблицы (общий)
    table_frame = tk.Frame(window.main_frame,
                           bg=color_frame)
    table_frame.place(x=15, y=50)

    # Фрейм для вывода таблицы (для добавления горизонт скроллбара)
    table_frame_bot_scr = tk.Frame(table_frame,
                                   bg=color_frame)
    table_frame_bot_scr.pack(side='left')

    # Наш Лист для вывода таблицы
    window.table_canvas = tk.Canvas(table_frame_bot_scr,
                                    bg="white",
                                    bd=0,
                                    width=(window.width - 54),
                                    height=(window.height - 104))
    window.table_canvas.pack(side='top')

    frame_to_table_list = tk.Frame(window.table_canvas,
                                   bg="white")
    window.table_canvas.create_window((1, 1),  # tuple с разметкой фрейма (столбцы, строки)
                                      window=frame_to_table_list,  # задаем наш фрейм как окно канваса
                                      tags="frame_to_table_list")  # задаем ему тэг (имя в области видимости канваса)

    #     функция для изменения размера канваса и работы скроллбара
    frame_to_table_list.bind("<Configure>",
                             lambda ev, canvas=window.table_canvas: on_frame_configure(ev, canvas))

    # создание таблицы
    columns = tuple(i for i in array[1])
    window.table_list = ttk.Treeview(frame_to_table_list,
                                     columns=columns,
                                     height=len(array[2]))
    for c in columns:
        window.table_list.heading(c, text=c.title())

    window.table_list.pack()

    # заполнение таблицы
    _table_insert(window=window, array=array)

    # наши скроллбары
    scrollbar_x = tk.Scrollbar(table_frame_bot_scr, orient="horizontal")
    scrollbar_x.pack(side='bottom', fill='x')

    scrollbar_y = tk.Scrollbar(table_frame, orient="vertical")
    scrollbar_y.pack(side='right', fill='y')

    # привязка скроллбара к листбоксу (по вертикали)
    scrollbar_y['command'] = window.table_canvas.yview
    window.table_canvas['yscrollcommand'] = scrollbar_y.set

    # привязка скроллбара к листбоксу (по вертикали)
    scrollbar_x['command'] = window.table_canvas.xview
    window.table_canvas['xscrollcommand'] = scrollbar_x.set

    # кнопка выхода
    window.exit_button = tk.Button(window.main_frame,
                                   text='Back',
                                   width=8,
                                   bg="pink",  # цвет кннопки в обычном состоянии
                                   activebackground='violet')  # цвет нажатой кнопки
    window.exit_button.place(x=(window.width - 82),
                             y=(window.height - 30))


# Функция для инициализации окна просмотра таблицы
def view_window_create(user_type, array):
    view_window = Window(name="View Table",
                         type_window="Main",
                         # icon_adress="./app_lib/Image/icon_view_window.ico")
                         )
    view_window.frozen_size(width=1198, height=715)

    view_window.user_type = user_type

    _frame_view_window_create(window=view_window, array=array)

    return view_window


#   SAPPORT WINDOW
# окно сообщения
def message_box(text, count_row, type_message):
    if type_message == "good":
        icon = "./app_lib/Image/icon_good_auth.ico"
        color = "#85e37d"
    else:
        icon = "./app_lib/Image/icon_bad_auth.ico"
        color = "#ef5050"

    message_window = Window(type_window="TopLevel", name="Mistake", icon_adress=icon)
    message_window.frozen_size(400, (20*count_row + 40))

    message_window.canvas = tk.Canvas(message_window.root,
                                      width=message_window.width,
                                      height=message_window.height,
                                      bg=color)
    message_window.canvas.pack()

    message_window.message = tk.Label(message_window.canvas,
                                      text=text,
                                      width=50,
                                      bg=color)
    message_window.message.place(x=30, y=2)

    message_window.ex_but = tk.Button(message_window.canvas,
                                      width=10,
                                      height=1,
                                      text="Ok",
                                      bg="#ff2200",
                                      command=message_window.root.destroy)
    message_window.ex_but.place(x=(message_window.width/2 - 40),
                                y=(20*count_row + 2 + 10))


class MyProgressBarWindow():
    def __init__(self, num, user_type, name="Loading", text="Loading a new table:", color="#4bbc10"):
        self.window = tk.Tk(className=name)
        self.window.iconbitmap("./app_lib/Image/icon_load.ico")

        self._config()
        self._main_frame()
        self._label(text)
        self._progressbar()
        self._log_frame()
        self._run_see_pb()
        self._ok_button()
        self._centering_window()
        self._control()

        self.color_bar = color
        self.num = num
        self.now_num = 1
        self.user_type = user_type

    def _config(self):
        self.width = 435
        self.height = 280
        self.window.resizable(width=False, height=False)

    def _main_frame(self):
        self.main_frame = tk.Frame(self.window,
                                   width=self.width,
                                   height=self.height,
                                   bg="aqua")
        # bg=color_frame)
        self.main_frame.pack()

    def _label(self, text):
        self.label = tk.Label(self.main_frame,
                              text=text,
                              font=("arial", 12),
                              justify="left",
                              relief="flat",
                              bg=color_frame)
        self.label.place(x=15, y=10)

    def _progressbar(self):
        self.bar_height = 18
        self.bar_width = 395

        self.progress_bar_frame = tk.Frame(self.main_frame,
                                           relief="sunken",
                                           bg=color_frame,
                                           bd=2)
        self.progress_bar_frame.place(x=15, y=35)

        self.progress_bar_canvas = tk.Canvas(self.progress_bar_frame,
                                             width=self.bar_width,
                                             height=self.bar_height,
                                             bg="white")
        self.progress_bar_canvas.pack()

    def _log_frame(self):
        self.log_frame = tk.Frame(self.main_frame,
                                  relief="sunken",
                                  bg=color_frame,
                                  bd=2)
        self.log_frame.place(x=15, y=65)

        self.hor_log_frame = tk.Frame(self.log_frame)
        self.hor_log_frame.pack(side="left")

        self.log_box = tk.Listbox(self.hor_log_frame,
                                  font=("arial", 8),
                                  height=12,
                                  width=51,
                                  bg="white")
        self.log_box.pack(side="top")

        self.log_y_scrollbar = tk.Scrollbar(self.log_frame,
                                            orient="vertical")
        self.log_y_scrollbar.pack(side="right", fill='y')

        self.log_x_scrollbar = tk.Scrollbar(self.hor_log_frame,
                                            orient="horizontal")
        self.log_x_scrollbar.pack(side="bottom", fill='x')

        self.log_box["yscrollcommand"] = self.log_y_scrollbar.set
        self.log_y_scrollbar["command"] = self.log_box.yview

        self.log_box["xscrollcommand"] = self.log_x_scrollbar.set
        self.log_x_scrollbar["command"] = self.log_box.xview

    def _run_see_pb(self):
        self.rpb = ttk.Progressbar(self.main_frame,
                                   length=160,
                                   orient="vertical")
        self.rpb.place(x=376, y=65)

    def _ok_button(self):
        self.ok_button = tk.Button(self.main_frame,
                                   text="Ok",
                                   font=("arial", 12),
                                   width=6,
                                   state="disabled",
                                   bg="blue")
        # bg=color_button)
        self.ok_button.place(x=355, y=230)

    def _centering_window(self):
        win_width = self.window.winfo_screenwidth()
        win_height = self.window.winfo_screenheight()
        x = (win_width - self.width) / 2
        y = (win_height - self.height) / 2
        self.window.geometry("{}x{}+{}+{}".format(self.width, self.height, int(x), int(y)))

    def exit(self, ev):
        if self.ok_button["state"] == "disabled":
            return
        self.window.destroy()

    def _control(self):
        pass

    def run_pb(self):
        width_el = int(self.bar_width / self.num)
        self.progress_bar_canvas.delete("all")
        if self.now_num < self.num:
            ne_point = [width_el * self.now_num, 0]
            se_point = [width_el * self.now_num, self.bar_height]
        else:
            ne_point = [self.bar_width, 0]
            se_point = [self.bar_width, self.bar_height]
            self.ok_button["state"] = "normal"

        nw_point = [0, 0]
        sw_point = [0, self.bar_height]
        point = nw_point + ne_point + se_point + sw_point

        self.progress_bar_canvas.create_polygon(point,
                                                fill=self.color_bar)
        self.window.update()

        self.now_num += 1
