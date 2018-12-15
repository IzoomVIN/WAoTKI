from cx_Freeze import setup, Executable
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))

os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

include_files = [os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                 os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
                 ("app_lib/Database/manager_data/color_array.pkl", "app_lib/Database/manager_data/color_array.pkl"),
                 "app_lib/Database/table_data/",
                 ("app_lib/Image/icon_add_window.ico", "app_lib/Image/icon_add_window.ico"),
                 ("app_lib/Image/icon_auth.ico", "app_lib/Image/icon_auth.ico"),
                 ("app_lib/Image/icon_bad_auth.ico", "app_lib/Image/icon_bad_auth.ico"),
                 ("app_lib/Image/icon_good_auth.ico", "app_lib/Image/icon_good_auth.ico"),
                 ("app_lib/Image/icon_home_window.ico", "app_lib/Image/icon_home_window.ico"),
                 ("app_lib/Image/icon_load.ico", "app_lib/Image/icon_load.ico"),
                 ("app_lib/Image/icon_view_window.ico", "app_lib/Image/icon_view_window.ico"),]

packages = ["numpy", "os"]

build_exe = {'include_files': include_files,
             "include_msvcr": True,
             "build_exe": "This_is_table",  # создает папку с файлами с именем...
             "packages": packages,
             "includes": ["idna.idnadata"]}

executables = [Executable(script="Main.py",
                          targetName="My_app.exe",
                          icon="./main_ico.ico",
                          base="Win32GUI")]
                          # shortcutName='Vinogradov app',
                          # shortcutDir='ProgramMenuFolder')]

setup(name="My_app",
      version="0.0.99",
      description="apps",
      executables=executables,
      options={'build_exe': build_exe})
