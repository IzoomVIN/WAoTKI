from app_lib.Windows_a import Windows
from app_lib.Management_apps import user_func


def view_exit_button_event(ev):
    view_window.root.destroy()
    user_func.user_win(user_type=view_window.user_type)


# CONTROL FUNCK
def view_win(user_type, array):
    global view_window
    view_window = Windows.view_window_create(user_type=user_type, array=array)

    view_window.exit_button.bind("<Button-1>", view_exit_button_event)

    view_window.root.mainloop()
