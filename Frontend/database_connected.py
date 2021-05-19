from tkinter import *
from PIL import ImageTk
from ttkthemes import themed_tk as tk
from datetime import *
import time
import smtplib
import random
import Backend.connection
import Model_class.student_registration
from tkinter import messagebox
import Frontend.connect_database
import Frontend.forgot_password
import Frontend.admin_dashboard
import Frontend.login_form
import Frontend.non_verified
import Model_class.database_connected


class DatabaseConnected:
    """ after successful connection of database, this will require user to create an admin account before they
    can proceed further, when created account OTP will be sent to user email and if verified it will call
    another class where unverified data are shifted to verified admin table of database otherwise leave remain
    in unverified table of database"""
    email = []
    otp = []
    def __init__(self, window):
        """takes window to display all the attributes and function for this class"""
        self.window = window
        self.window.geometry("1366x720+0+0")
        self.window.title("Admin Setup")
        self.window.iconbitmap('images\\logo.ico')
        self.window.resizable(False, False)
        self.login_frame = ImageTk.PhotoImage \
            (file='images\\admin_setup_frame.png')
        self.image_panel = Label(self.window, image=self.login_frame)
        self.image_panel.pack(fill='both', expand='yes')

        self.txt = "First Time Admin Setup"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.window, text=self.txt, font=('yu gothic ui', 30, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=480, y=70, width=450)
        self.slider()
        self.heading_color()

        self.db_connection = Backend.connection.DatabaseConnection()

        # ========================================================================
        # ============================Email====================================
        # ========================================================================

        self.email_label = Label(self.window, text="Email ", bg="white", fg="#4f4e4d",
                                 font=("yu gothic ui", 13, "bold"))
        self.email_label.place(x=495, y=155)

        self.email_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                 font=("yu gothic ui semibold", 12))
        self.email_entry.place(x=530, y=182, width=380)  # trebuchet ms

        # ========================================================================
        # ============================Username====================================
        # ========================================================================

        self.username_label = Label(self.window, text="Username ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=495, y=265)

        self.username_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.username_entry.place(x=530, y=295, width=380)  # trebuchet ms

        # ========================================================================
        # ============================Password====================================
        # ========================================================================

        self.password_label = Label(self.window, text="Password ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=495, y=380)

        self.password_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.password_entry.place(x=530, y=410, width=380)  # trebuchet ms

        # ========================================================================
        # ============================Submit button================================
        # ========================================================================

        self.submit = ImageTk.PhotoImage \
            (file='images\\submit.png')

        self.submit_button = Button(self.window, image=self.submit,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=self.validation)
        self.submit_button.place(x=500, y=500)

        # ========================================================================
        # ============================Login button================================
        # ========================================================================

        self.login = ImageTk.PhotoImage \
            (file='images\\login.png')

        self.login_button = Button(self.window, image=self.login,
                                   font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                   , borderwidth=0, background="white", cursor="hand2", command=self.click_login)
        self.login_button.place(x=640, y=503)

        # ========================================================================
        # ============================Exit button================================
        # ========================================================================

        self.exit_img = ImageTk.PhotoImage \
            (file='images\\exit.png')
        self.exit_button = Button(self.window, image=self.exit_img,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2", command=self.click_exit)
        self.exit_button.place(x=783, y=503)

        # ========================================================================
        # ========================Database Label and button=======================
        # ========================================================================

        self.database_label = Label(self.window, text="* Please enter Admin details and Submit,\n"
                                                      "Do not forget to store it in safe place,\n"
                                                      "You will need it while logging in! ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.database_label.place(x=550, y=603)

    def slider(self):
        """creates slides for heading by taking the text,
                 and that text are called after every 100 ms"""
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
        """
        configures heading label
        :return: every 50 ms returned new random color.

        """
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)

    def validation(self):
        """ tires to validates if user exist already in database or not, if not it will call another method to
        store that user in database otherwise already exists message will popup, BaseException is handled incase
        any error occurred"""
        try:
            obj_admin_database = Model_class.database_connected.GetDatabase('use cms;')
            self.db_connection.create(obj_admin_database.get_database())

            query = "select * from admin where username = %s OR email = %s ;"
            data = self.db_connection.search(query, (self.username_entry.get(), self.email_entry.get()))
            print(data)
            self.f_username = []
            self.f_email = []
            for values in data:
                f_username_list = values[1]
                f_email_list = values[2]
                self.f_username.append(f_username_list)
                self.f_email.append(f_email_list)
            print(self.f_username)
            print(self.f_email)
        except BaseException as msg:
            print(msg)
        try:
            if self.email_entry.get() == "":
                messagebox.showerror("Error", "Email can not be empty")

            elif self.username_entry.get() == "":
                messagebox.showerror("Error", "Username can not be empty")

            elif self.password_entry.get() == "":
                messagebox.showerror("Error", "Password can not be empty")

            elif self.username_entry.get() != "" or self.email_entry.get() != "":
                try:
                    if self.f_email[0] == self.email_entry.get():
                        messagebox.showerror("Error", "Email Already exists")

                    elif self.f_username[0] == self.username_entry.get():
                        messagebox.showerror("Error", "Username Already exists")

                except BaseException as msg:
                    self.non_verified_validation()
                    print(msg)

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error", "Please Check the details")

    def non_verified_validation(self):
        """ tires to validates if user exist already in database as unverified or not, if not it will call another
        method to store that user in database otherwise it will require that user to verify their email,
        BaseException is handled in case any error occurred"""
        try:
            obj_admin_database = Model_class.database_connected.GetDatabase('use cms;')
            self.db_connection.create(obj_admin_database.get_database())

            query = "select * from unverified where username = %s OR email = %s ;"
            data = self.db_connection.search(query, (self.username_entry.get(), self.email_entry.get()))
            print(data)
            self.u_username = []
            self.u_email = []
            for values in data:
                u_username_list = values[1]
                u_email_list = values[2]
                self.u_username.append(u_username_list)
                self.u_email.append(u_email_list)
            print(self.u_username)
            print(self.u_email)
        except BaseException as msg:
            print(msg)
        try:

            if self.username_entry.get() != "" or self.email_entry.get() != "":
                try:
                    if self.u_email[0] == self.email_entry.get():
                        messagebox.showerror("Error", "Email Already exists\n Please verify your email")

                    elif self.u_username[0] == self.username_entry.get():
                        messagebox.showerror("Error", "Username Already exists\n Please verify your email")

                except BaseException as msg:
                    self.click_submit()
                    print(msg)

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error", "Please Check the details")

    def click_submit(self):
        """when clicked submit button, it will save those user data to unverified admin table
        of database so that verification process can be proceed further, BaseException is handled to avoid any
        runtime error that may happen due to user"""
        try:
            obj_create_database = Model_class.database_connected.GetDatabase('use cms;')
            self.db_connection.create(obj_create_database.get_database())

            obj_database_connected = Model_class.database_connected.AdminData(self.username_entry.get(),
                                                                              self.email_entry.get(),
                                                                              self.password_entry.get())
            query = 'insert into unverified (username,email,password) values (%s,%s,%s);'
            values = (obj_database_connected.get_username(), obj_database_connected.get_email(),
                      obj_database_connected.get_password())
            # print(values)
            self.db_connection.insert(query, values)
            DatabaseConnected.email.clear()
            DatabaseConnected.email.append(self.email_entry.get())
            messagebox.showinfo("Success", f"Data inserted Successfully\n Username={values[0]},\n "
                                           f"Password={values[2]}")
            messagebox.showinfo("Wait",f"Please Hold till OTP is sent to {values[1]} ")
            self.click_send_otp()

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error", "There is some error Submitting Credentials ")

    def click_send_otp(self):
        """Sends and OTP to the email that a user uses to create admin account, BaseException is handled to avoid
        internet issue or wrong email address that may often happen due to user"""
        if self.email_entry.get() != "":
            try:
                self.value = random.randint(100000, 999999)
                DatabaseConnected.otp.clear()
                DatabaseConnected.otp.append(self.value)
                # print(value)

                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

                server.login("tkintercms@gmail.com", "tkinter@12345")

                server.sendmail("tkintercms@gmail.com", f"{self.email_entry.get()}", f"Subject: Tkinter-CMS OTP \n\n "
                                                                                     f"Your "
                                                                                     f" OTP for College Management"
                                                                                     f" system is  {self.value}")
                server.quit()
                # messagebox.showinfo("Success", f"OTP have been sent to {self.[0]}")
                # print(DatabaseConnected.otp[0])
                messagebox.showinfo("Notification", f"OTP has been sent to {self.email_entry.get()}\n Please verify "
                                                    f"email before you can log in ")
                self.otp_verification()

            except BaseException as msg:
                messagebox.showerror("Failed",
                                     "There is an error sending OTP\n Make sure you are connected to internet")

        else:
            messagebox.showerror("Empty", "Please Enter Email Address \nand Click Send OTP")

    def otp_verification(self):
        """ to verify the OTP it calls another window"""
        win = Toplevel()
        VerifyRecentOtp(win)
        self.window.withdraw()
        win.deiconify()

    def click_login(self):
        """when clicked login button, it will direct that user to login form"""
        win = Toplevel()
        Frontend.login_form.Login(win)
        self.window.withdraw()
        win.deiconify()

    def click_exit(self):
        ask = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to Exit\n Student Registration Form?")
        if ask is True:
            self.window.quit()


class VerifyRecentOtp(Frontend.non_verified.NonVerified):
    """Inherits Nonverified class from Frontend package and extends various functionality like,
    verifies OTP that has been sent while creating the admin account,
    this will take only current OTP, and validates the email, if email is verified successfully
    unverified admin details will be shift to admin table of database as a verified account
    otherwise leave by popup error message"""
    def __init__(self, wind):
        super().__init__(wind)
        """extends the functionality of NonVerified class"""
        # print(DatabaseConnected.otp[0])
        self.recent_otp = DatabaseConnected.otp[0]
        self.recent_email = DatabaseConnected.email[0]
        # print(self.recent_otp)
        # self.recent_otp_entry = self.otp_entry.get()

        self.verify_button.configure(command = self.validation)

    def validation(self):
        """Validates if user input fields in empty or not and raise error if left blank,
        else, it calls to shift the unverified"""
        # print(DatabaseConnected.otp[0])
        # if self.email_entry.get() == '':
        #     messagebox.showinfo("Empty","Something went wrong\n Please Try again")
        if self.otp_entry.get() == '':
            messagebox.showinfo("Empty","Please Enter recent OTP from your email")

        if self.recent_otp == int(self.otp_entry.get()):
            messagebox.showinfo("Success","Your Email have been verified successfully")
            self.shift_user_to_admin()
        else:
            messagebox.showerror("Error","Sorry, We can not verify your email")

    def shift_user_to_admin(self):
        """Shifts user to admin from unverified database table after successful verification of email"""
        print("Success, otp is verified, you can now verify this user")
        try:
            obj_admin_database = Model_class.database_connected.GetDatabase('use cms;')
            self.db_connection.create(obj_admin_database.get_database())

            query = "select * from unverified where email = %s ;"
            data = self.db_connection.search(query, (self.recent_email,))
            print(data)
            self.c_username = []
            self.c_email = []
            self.c_password = []
            for values in data:
                c_username_list = values[1]
                c_email_list = values[2]
                c_password_list = values [3]

                self.c_username.append(c_username_list)
                self.c_email.append(c_email_list)
                self.c_password.append(c_password_list)
            print(self.c_username)
            print(self.c_email)
            print(self.c_password)
            self.click_submit()

        except BaseException as msg:
            print(msg)

    def click_submit(self):
        """insert the verified data into admin table of database"""
        try:
            obj_create_database = Model_class.database_connected.GetDatabase('use cms;')
            self.db_connection.create(obj_create_database.get_database())

            obj_database_connected = Model_class.database_connected.AdminData(self.c_username[0],
                                                                              self.c_email[0],
                                                                              self.c_password[0])
            query = 'insert into admin (username,email,password) values (%s,%s,%s);'
            values = (obj_database_connected.get_username(), obj_database_connected.get_email(),
                      obj_database_connected.get_password())

            self.db_connection.insert(query, values)

            query = "delete from unverified where email=%s;"
            self.db_connection.delete(query, (self.c_email[0],))
            self.otp_entry.delete(0,END)

            c_email = self.c_email[0]

            print(c_email)

            c_time = time.strftime('%H:%M:%S')
            c_date = time.strftime('%Y/%m/%d')
            print(c_time)
            print(c_date)

            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

            server.login("tkintercms@gmail.com", "tkinter@12345")

            server.sendmail("tkintercms@gmail.com", f"{c_email}", f"Subject: Tkinter-CMS "
                                                                                 f"Account Created \n\n "
                                                                                 f"Your "
                                                                                 f" Your New Account for College Management System "
                                                                                 f"was Created Successfully "
                                                                                 f" at Time  {c_time}"
                                                                                 f" at Date  {c_date}")
            server.quit()

            messagebox.showinfo("Success","You can now login")
            self.go_to_login()

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error", "There is some error Submitting Credentials ")

    def go_to_login(self):
        """when clicked login, login form is opened"""
        win = Toplevel()
        Frontend.login_form.Login(win)
        self.window.withdraw()
        win.deiconify()


def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    DatabaseConnected(window)
    window.mainloop()


if __name__ == '__main__':
    win()
