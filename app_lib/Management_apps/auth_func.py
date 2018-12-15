import pickle as pcl
import time
from tkinter import TclError, Label
from threading import Thread
from app_lib.Windows_a import Windows
from app_lib.Management_apps import user_func


# Наш мини обработчик событий в окне авторизации.
#   AUTH_FUNC
def auth_refocus_l_p(ev):
    if ev.keysym_num == 65293:
        auth_window.password_text.focus()


def auth_refocus_p_b(ev):
    if ev.keysym_num == 65293:
        auth_window.ok_button.focus()


def auth_ok_button_event(_):
    user = [str(auth_window.login_text.get()).strip(),
            str(auth_window.password_text.get()).strip()]

    # проверяем логин, если такой есть, то проверяем пароль, если все нормально идем дальше,
    # если нет, то выдаем сообщения об ошибке
    if user[0] in log_array.keys():
        if log_array[user[0]][0] == user[1]:
            auth_window.root.destroy()
            user_func.user_win(log_array[user[0]][1])
            return
        else:
            text = "Friend, I know you, but you do not know your password!\n "
            text = text + "you are real?\n prove it! remember your password!"
            Windows.message_box(text, 3, "good")
            return

    Windows.message_box("Friend, I don't know who are you!\n Please sign up to me or get out from me!", 2, "bad")
    auth_window.reg_button.configure(relief="raised", bg="#ff2200", activebackground="#ff2200")
    auth_window.ok_button.configure(relief="raised", state="normal")
    return


def auth_exit_button_event(ev):
    auth_window.root.destroy()


def auth_reg_button_event(ev):
    reg_win()


def auth_exit_button_graph(ev):
    delta_x = auth_window.root.winfo_geometry()
    delta_x = delta_x.split("+")[1]
    delta_x = int(delta_x)
    delta_x = 700 - (ev.x_root - delta_x)

    delta_y = auth_window.root.winfo_geometry()
    delta_y = delta_y.split("+")[2]
    delta_y = int(delta_y)
    delta_y = 550 - (ev.y_root - delta_y)

    if pow((delta_x ** 2 + delta_y ** 2), 1 / 2) < 150:
        auth_window.exit_button.configure(relief="raised", bg="#ff2222", activebackground="#ff2222")
        auth_window.root.update()
        return
    else:
        auth_window.exit_button.configure(relief="flat", bg="#c7f8e6", activebackground="#c7f8e6")
        auth_window.root.update()
        return


def canvas_graphic():
    with open("./app_lib/Database/manager_data/color_array.pkl", "rb") as file:
        color_array = pcl.load(file)
    try:
        while True:
            for d in range(289, (288 + 225)):
                time.sleep(0.01)
                x0 = 400
                y0 = 300

                # Удаляем все нарисованное ранее
                auth_window.canvas.delete("all")

                # меняем параметр цвета у всего что надо
                auth_window.login_password_frame.configure(bg=color_array[d - 289])
                auth_window.but_box.configure(bg=color_array[d - 289])
                auth_window.login_label.configure(bg=color_array[d - 289])
                auth_window.password_label.configure(bg=color_array[d - 289])

                # рисуем графику
                auth_window.canvas.create_oval((x0 - d / 2), (y0 - d / 2),
                                               (x0 + d / 2), (y0 + d / 2),
                                               fill=color_array[d - 289])

                # Сразу обновляем для того, чтобы видеть это
                auth_window.root.update()

            for d in range((288 + 225), 289, -1):
                time.sleep(0.01)
                x0 = 400
                y0 = 300

                # Удаляем все нарисованное ранее
                auth_window.canvas.delete("all")

                # меняем параметр цвета у всего что надо
                auth_window.login_password_frame.configure(bg=color_array[d - 289])
                auth_window.but_box.configure(bg=color_array[d - 289])
                auth_window.login_label.configure(bg=color_array[d - 289])
                auth_window.password_label.configure(bg=color_array[d - 289])

                # рисуем графику
                auth_window.canvas.create_oval((x0 - d / 2), (y0 - d / 2),
                                               (x0 + d / 2), (y0 + d / 2),
                                               fill=color_array[d - 289])
                # Сразу обновляем для того, чтобы видеть это
                auth_window.root.update()
    except TclError:
        return


#   REG FUNC
def reg_login_text_event(ev):
    if reg_window.control_login_label is None:
        reg_window.control_login_label = Label(reg_window.login_frame,
                                               width=30)
        reg_window.control_login_label.pack(side="bottom")

    if reg_window.login_text.get() in log_array.keys():
        reg_window.control_login_label["text"] = "username already exists!"
        reg_window.control_login_label["bg"] = "#ff2222"
        reg_window.root.update()
    else:
        reg_window.control_login_label["text"] = "good name!"
        reg_window.control_login_label["bg"] = "#99f285"
        reg_window.root.update()

    if ev.keysym_num == 65293:
        reg_window.password_text.focus()

    return


def reg_password_text_event(ev):
    if reg_window.control_password_label is None:
        reg_window.control_password_label = Label(reg_window.password_frame,
                                                  width=30)
        reg_window.control_password_label.pack(side="bottom")

    if len(reg_window.password_text.get()) < 6:
        text = "bad password! append {} characters please!".format(6 - len(reg_window.password_text.get()))
        reg_window.control_password_label["text"] = text
        reg_window.control_password_label["bg"] = "#ff2222"
        reg_window.root.update()
    else:
        reg_window.control_password_label["text"] = "good password!"
        reg_window.control_password_label["bg"] = "#99f285"
        reg_window.root.update()

    if ev.keysym_num == 65293:
        reg_window.password_again_text.focus()

    return


def reg_password_again_text_event(ev):
    if reg_window.control_password_again_label is None:
        reg_window.control_password_again_label = Label(reg_window.password_again_frame,
                                                        width=30)
        reg_window.control_password_again_label.pack(side="bottom")

    if reg_window.password_text.get() != reg_window.password_again_text.get():
        reg_window.control_password_again_label["text"] = "incorrect password!"
        reg_window.control_password_again_label["bg"] = "#ff2222"
        reg_window.root.update()
    else:
        reg_window.control_password_again_label["text"] = "good password!"
        reg_window.control_password_again_label["bg"] = "#99f285"
        reg_window.root.update()

    if ev.keysym_num == 65293:
        reg_window.ok_button.focus()

    return


def reg_ok_button_event(ev):
    condition1 = (reg_window.control_password_again_label is None
                  or reg_window.control_password_again_label["bg"] == "#ff2222")
    condition2 = (reg_window.control_password_label is None
                  or reg_window.control_password_label["bg"] == "#ff2222")
    condition3 = (reg_window.control_password_label is None
                  or reg_window.control_password_label["bg"] == "#ff2222")
    if condition1 or condition2 or condition3:
        text = "Friend, your login or password is incorrect!\n correct the problem and try again!"
        Windows.message_box(text, 2, "bad")
        return
    if 'selected' not in reg_window.check_admin.state():
        login = reg_window.login_text.get()
        password = reg_window.password_text.get()

        log_array[login] = [password, "Student"]
        with open("./app_lib/Database/manager_data/log_array.pkl", "wb") as file:
            pcl.dump(log_array, file)

        reg_exit_button_event(True)
    else:
        reg_main_admin_auth(type_win="auth")


def reg_exit_button_event(ev):
    reg_window.root.destroy()
    auth_window.root.destroy()
    auth_win()


def reg_graph():
    with open("./app_lib/Database/manager_data/color_array.pkl", "rb") as file:
        color_array = pcl.load(file)
        try:
            while True:
                for d in range(289, (288 + 225)):
                    time.sleep(0.01)

                    # меняем параметр цвета у всего что надо
                    reg_window.user_canvas.configure(bg=color_array[d - 289])
                    reg_window.login_frame.configure(bg=color_array[d - 289])
                    reg_window.password_frame.configure(bg=color_array[d - 289])
                    reg_window.password_again_frame.configure(bg=color_array[d - 289])
                    reg_window.login_label.configure(bg=color_array[d - 289])
                    reg_window.password_label.configure(bg=color_array[d - 289])
                    reg_window.password_again_label.configure(bg=color_array[d - 289])
                    reg_window.check_admin.configure(bg=color_array[d - 289])

                    # Сразу обновляем для того, чтобы видеть это
                    auth_window.root.update()

                for d in range((288 + 225), 289, -1):
                    time.sleep(0.01)

                    # меняем параметр цвета у всего что надо
                    reg_window.user_canvas.configure(bg=color_array[d - 289])
                    reg_window.login_frame.configure(bg=color_array[d - 289])
                    reg_window.password_frame.configure(bg=color_array[d - 289])
                    reg_window.password_again_frame.configure(bg=color_array[d - 289])
                    reg_window.login_label.configure(bg=color_array[d - 289])
                    reg_window.password_label.configure(bg=color_array[d - 289])
                    reg_window.password_again_label.configure(bg=color_array[d - 289])
                    reg_window.check_admin.configure(bg=color_array[d - 289])

                    # Сразу обновляем для того, чтобы видеть это
                    auth_window.root.update()
        except TclError:
            return


#   REG AUTH MAIN ADMIN FUNC
def reg_main_admin_auth_login_text_event(ev):
    if ev.keysym_num == 65293:
        reg_main_admin_auth_window.password_text.focus()


def reg_main_admin_auth_password_text_event(ev):
    if ev.keysym_num == 65293:
        reg_main_admin_auth_window.ok_button.focus()


def main_admin_auth_ok_button_event(ev):
    login = reg_main_admin_auth_window.login_text.get()
    password = reg_main_admin_auth_window.password_text.get()
    if login in log_array.keys() and log_array[login][0] == password and log_array[login][1] == "Main_Admin":
        login = reg_window.login_text.get()
        password = reg_window.password_text.get()

        log_array[login] = [password, "Admin"]
        with open("./app_lib/Database/manager_data/log_array.pkl", "wb") as file:
            pcl.dump(log_array, file)

        reg_main_admin_auth_window.root.destroy()
        reg_window.root.destroy()
        auth_window.root.destroy()

        auth_win()
    else:
        reg_main_admin_auth_window.root.destroy()
        reg_window.root.destroy()

        text = "You're not Main Admin!\n goodbye!"
        Windows.message_box(text, 2, "bad")

        reg_win()


def reg_main_admin_ok_button_event(ev):
    global log_array
    login = reg_main_admin_auth_window.login_text.get()
    password = reg_main_admin_auth_window.password_text.get()

    log_array = {}
    log_array[login] = [password, "Main_Admin"]

    with open("./app_lib/Database/manager_data/log_array.pkl", "wb") as file:
        pcl.dump(log_array, file)

    Windows.message_box("Ok", 1, "good")

    reg_main_admin_auth_window.root.destroy()


def reg_main_admin_auth_exit_button_event(ev):
    reg_main_admin_auth_window.root.destroy()


#   CONTROL FUNC
def auth_win():
    global auth_window, log_array

    try:
        with open("./app_lib/Database/manager_data/log_array.pkl", "rb") as file:
            log_array = pcl.load(file)
    except FileNotFoundError:
        reg_main_admin_auth(type_win="reg")

    auth_window = Windows.auth_window_create()

    auth_window.login_text.bind("<KeyPress>", auth_refocus_l_p)

    auth_window.password_text.bind("<KeyPress>", auth_refocus_p_b)

    auth_window.reg_button.bind("<Button-1>", auth_reg_button_event)
    auth_window.reg_button.bind("<Return>", auth_reg_button_event)

    auth_window.ok_button.bind("<Button-1>", auth_ok_button_event)
    auth_window.ok_button.bind("<Return>", auth_ok_button_event)

    auth_window.canvas.bind("<Motion>", auth_exit_button_graph)
    auth_window.exit_button.bind("<Button-1>", auth_exit_button_event)
    auth_window.exit_button.bind("<Return>", auth_exit_button_event)

    # создаем доп поток для графики
    graph = Thread(daemon=True, target=canvas_graphic())
    # стартуем доп поток
    graph.start()

    auth_window.root.mainloop()


def reg_win():
    global reg_window
    reg_window = Windows.auth_reg_window_create()

    reg_window.control_login_label = None
    reg_window.control_password_label = None
    reg_window.control_password_again_label = None

    reg_window.ok_button.bind("<Button-1>", reg_ok_button_event)
    reg_window.ok_button.bind("<Return>", reg_ok_button_event)
    reg_window.exit_button.bind("<Button-1>", reg_exit_button_event)
    reg_window.exit_button.bind("<Return>", reg_exit_button_event)

    reg_window.login_text.bind("<KeyPress>", reg_login_text_event)
    reg_window.password_text.bind("<KeyPress>", reg_password_text_event)
    reg_window.password_again_text.bind("<KeyPress>", reg_password_again_text_event)

    t = Thread(reg_graph())
    t.start()

    reg_window.root.mainloop()


def reg_main_admin_auth(type_win):
    global reg_main_admin_auth_window, auth_window

    if type_win == "auth":
        reg_main_admin_auth_window = Windows.reg_main_admin_auth_window_create(type_window="TopLevel")

        reg_main_admin_auth_window.ok_button.bind("<Button-1>", main_admin_auth_ok_button_event)
        reg_main_admin_auth_window.ok_button.bind("<Return>", main_admin_auth_ok_button_event)

        reg_main_admin_auth_window.exit_button.bind("<Button-1>", reg_main_admin_auth_exit_button_event)
        reg_main_admin_auth_window.exit_button.bind("<Return>", reg_main_admin_auth_exit_button_event)
    elif type_win == "reg":
        reg_main_admin_auth_window = Windows.reg_main_admin_auth_window_create(type_window="Main")

        Windows.message_box("Enter Main Admin for program please", 1, "good")

        reg_main_admin_auth_window.ok_button.bind("<Button-1>", reg_main_admin_ok_button_event)
        reg_main_admin_auth_window.ok_button.bind("<Return>", reg_main_admin_ok_button_event)

        reg_main_admin_auth_window.exit_button.destroy()

    reg_main_admin_auth_window.login_text.bind("<KeyPress>", reg_main_admin_auth_login_text_event)
    reg_main_admin_auth_window.password_text.bind("<KeyPress>", reg_main_admin_auth_password_text_event)

    reg_main_admin_auth_window.root.mainloop()
