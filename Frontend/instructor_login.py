from tkinter import *
from tkinter import ttk
from tkcalendar import *
from PIL import ImageTk, Image, ImageDraw
from ttkthemes import themed_tk as tk
from datetime import *
import time
from math import *
import random
import Backend.connection
import Model_class.student_registration
from tkinter import messagebox
import os


class Login:
    def __init__(self, window, img, login, database_img):
        self.window = window
        self.window.geometry("1366x720+0+0")
        self.window.title("Student Login Form")
        self.window.iconbitmap('images\\logo.ico')
        self.window.resizable(False, False)
        self.login_frame = img
        self.image_panel = Label(self.window, image=self.login_frame)
        self.image_panel.pack(fill='both', expand='yes')

        self.txt = "Instructor Login"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.window, text=self.txt, font=('yu gothic ui', 30, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=570, y=70, width=280)
        self.slider()
        self.heading_color()

        # ========================================================================
        # ============================Username====================================
        # ========================================================================

        self.username_label = Label(self.window, text="Username ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=495, y=220)

        self.username_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12), show="*")
        self.username_entry.place(x=530, y=255, width=380)  # trebuchet ms

        # ========================================================================
        # ============================Password====================================
        # ========================================================================

        self.password_label = Label(self.window, text="Password ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=495, y=335)

        self.password_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12),show="*")
        self.password_entry.place(x=530, y=370, width=380)  # trebuchet ms

        # ========================================================================
        # ============================Login button================================
        # ========================================================================

        login = login
        self.login_button = Button(self.window, image=login,
                                   font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                   , borderwidth=0, background="white", cursor="hand2")
        self.login_button.place(x=640, y=450)

        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================

        self.forgot_label = Label(self.window, text="Forgot ", bg="white", fg="#4f4e4d",
                                  font=("yu gothic ui", 13, "bold underline"))
        self.forgot_label.place(x=767, y=413)

        self.forgot_button = Button(self.window, text="Password ?",
                                    font=("yu gothic ui", 13, "bold underline"), fg="red", relief=FLAT,
                                    activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2")
        self.forgot_button.place(x=820, y=410)

    def slider(self):
        if self.count >= len(self.txt):
            self.count = -1
            self.text = ''
            self.heading.config(text=self.text)

        else:
            self.text = self.text + self.txt[self.count]
            self.heading.config(text=self.text)
        self.count += 1

        self.heading.after(100, self.slider)

    def heading_color(self):
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)


def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    img = ImageTk.PhotoImage(Image.open("images\\login_frame.png"))

    login = ImageTk.PhotoImage(Image.open("images\\login.png"))

    database_img = ImageTk.PhotoImage(Image.open("images\\connect_database.png"))

    Login(window, img, login, database_img)
    window.mainloop()


if __name__ == '__main__':
    win()
