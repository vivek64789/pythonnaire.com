from tkinter import *
from ttkthemes import themed_tk as tk
import Frontend.connect_database
import Frontend.login_form
import os

class StartApp:
    """This will check if database is already connected or not
    if already connected then login form will popup otherwise
    it will ask to connect the database by calling connect database
    class"""
    def __init__(self, window):
        self.window = window
        self.window.geometry("0x0+0+0")
        self.window.title("Login Form")
        self.window.iconbitmap('images\\logo.ico')
        self.window.resizable(False, False)

        self.len = os.path.getsize("database_data.txt")
        if self.len > 0:
            win = Toplevel()
            Frontend.login_form.Login(win)
            self.window.withdraw()
            win.deiconify()

        elif self.len == 0:
            win = Toplevel()
            Frontend.connect_database.ConnectDatabase(win)
            self.window.withdraw()
            win.deiconify()

        else:
            pass


def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    StartApp(window)
    window.mainloop()


if __name__ == '__main__':
    win()
