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
import Model_class.database_connected
from tkinter import messagebox
import Frontend.login_form

from random import seed
from random import randint
import smtplib

import os


class ForgotPassword:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x720+0+0")
        self.window.title("Forgot Password Form")
        self.window.iconbitmap('images\\logo.ico')
        self.window.resizable(False, False)

        # im = Image.open('D:\\Softwarica study material\\Semester 2\\Introduction to Algorithm\\'
        #                 'Coding_and_Algorithms\\190352_Bibekanand_kushwaha_Sem_2_Final_assignment\\im'
        #                 'ages\\connect_database_frame.png')
        # ph = ImageTk.PhotoImage(im)
        self.db_connection = Backend.connection.DatabaseConnection()

        self.login_frame = ImageTk.PhotoImage \
            (file='images\\forgot_password_frame.png')
        self.image_panel = Label(self.window, image=self.login_frame)
        # self.image_panel = Label(self.window, image=ph)
        # self.image_panel.image = ph
        self.image_panel.pack(fill='both', expand='yes')

        self.txt = "Choose New Password"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.window, text=self.txt, font=('yu gothic ui', 30, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=470, y=70, width=450)
        self.slider()
        self.heading_color()

        # ========================================================================
        # ============================Email========================================
        # ========================================================================

        self.email_label = Label(self.window, text="Email ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
        self.email_label.place(x=495, y=180)

        self.email_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                font=("yu gothic ui semibold", 12))
        self.email_entry.place(x=530, y=210, width=380)  # trebuchet ms

        # ========================================================================
        # ============================Password====================================
        # ========================================================================

        self.password_label = Label(self.window, text="Password ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=495, y=295)

        self.password_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.password_entry.place(x=530, y=325, width=380)  # trebuchet ms

        # ========================================================================
        # ============================Confirm Password============================
        # ========================================================================

        self.c_password_label = Label(self.window, text="Confirm Password ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.c_password_label.place(x=495, y=410)

        self.c_password_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.c_password_entry.place(x=530, y=440, width=380)  # trebuchet ms

        # ========================================================================
        # ============================Submit button================================
        # ========================================================================

        self.submit = ImageTk.PhotoImage \
            (file='images\\submit.png')

        self.submit_button = Button(self.window, image=self.submit,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=self.click_submit)
        self.submit_button.place(x=500, y=520)

        # ========================================================================
        # ============================Login button================================
        # ========================================================================

        self.login = ImageTk.PhotoImage \
            (file='images\\login.png')

        self.login_button = Button(self.window, image=self.login,
                                   font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                   , borderwidth=0, background="white", cursor="hand2", command=self.click_send_again)
        self.login_button.place(x=640, y=523)

        # ========================================================================
        # ============================Exit button================================
        # ========================================================================

        self.exit_img = ImageTk.PhotoImage \
            (file='images\\exit.png')
        self.exit_button = Button(self.window, image=self.exit_img,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2", command=self.click_exit)
        self.exit_button.place(x=783, y=523)

        # ========================================================================
        # ========================Forgot password instruction=====================
        # ========================================================================

        self.forgot_ins_label = Label(self.window, text="* Please enter new password\n followed by your email address ", bg="white", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
        self.forgot_ins_label.place(x=575, y=593)

    def click_submit(self):
        try:
            obj_admin_database = Model_class.database_connected.GetDatabase('use cms;')
            self.db_connection.create(obj_admin_database.get_database())

            query = "select * from admin where email = %s;"
            data = self.db_connection.search(query,(self.email_entry.get(),))
            print(data)
            self.f_email = []
            # self.f_password = []
            for values in data:
                f_email_list = values[2]
                # f_password_list = values[2]
                self.f_email.append(f_email_list)
                # self.f_password.append(f_password_list)
            # print(self.f_password)
            print(self.f_email)
            
            try:
                self.value = random.randint(100000, 999999)
                # print(value)
    
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    
                server.login("tkintercms@gmail.com", "tkinter@12345")
    
                server.sendmail("tkintercms@gmail.com", f"{self.f_email[0]}", f"Subject: Tkinter-CMS OTP \n\n Your OTP for College Management system is  {self.value}")
                server.quit()
                messagebox.showinfo("Success",f"OTP have been sent to {self.f_email[0]}")
            except BaseException as msg:
                messagebox.showerror("Failed","There is an error sending OTP\n Make sure you are connected to internet")
            
        except BaseException as msg:
            print(msg)

    def click_send_again(self):
        print(self.c_password_entry.get())
        if int(self.c_password_entry.get()) == self.value:
            messagebox.showinfo("Hurrey", "Success")
        else:
            messagebox.showerror("Bad Requests", "Sorry we were not able to identify you")

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

    def click_login(self):
        win=Toplevel()
        Frontend.login_form.Login(win)
        self.window.withdraw()
        win.deiconify()

    def click_exit(self):
        ask = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to Exit\n College Management System?")
        if ask is True:
            self.window.quit()


def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    ForgotPassword(window)
    window.mainloop()


if __name__ == '__main__':
    win()
