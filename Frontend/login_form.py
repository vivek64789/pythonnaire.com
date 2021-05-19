from tkinter import *
from PIL import ImageTk
from ttkthemes import themed_tk as tk
from datetime import *
import time
import smtplib
import random
import Frontend.admin_dashboard
import Frontend.connect_database
import Model_class.student_registration
import Model_class.database_connected
import Frontend.otp_verification
import Frontend.database_connected
import Frontend.non_verified
import Backend.connection
from tkinter import messagebox


class Login:
    """allows user to login to the system by providing them user interface, it verifies username/email and password
    from the unverified and admin table of database, if user exists it check for password and allow them to login if
    it matched, otherwise popup error message. if user exists but has not verified their email, it will ask them
    to verify their email address so that thay can login, only after successful verification of email they will be
    allowed to login to the system. it also allow user to login to the system by providing OTP instead of password,
    it will first verify that username/email with existing data and if password left blank, will ask them if they
    want to login in using OTP. if user want to login using OTP, an unique OTP will be sent to the associated email
    address"""
    non_verified_email = []
    otp = []
    current_user = []

    def __init__(self, window):
        """takes window to display all the attributes and methods for this class"""
        self.window = window
        self.window.geometry("1366x720+0+0")
        self.window.title("Login Form")
        self.window.iconbitmap('images\\logo.ico')
        self.window.resizable(False, False)
        self.login_frame = ImageTk.PhotoImage \
            (file='images\\login_frame.png')
        self.image_panel = Label(self.window, image=self.login_frame)
        self.image_panel.pack(fill='both', expand='yes')

        self.txt = "Welcome to Login Page"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.window, text=self.txt, font=('yu gothic ui', 30, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=460, y=70, width=450)
        self.slider()
        self.heading_color()

        self.db_connection = Backend.connection.DatabaseConnection()

        # ========================================================================
        # ============================Username====================================
        # ========================================================================

        self.username_label = Label(self.window, text="Username ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=495, y=220)

        self.username_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.username_entry.place(x=530, y=255, width=380)  # trebuchet ms

        # ========================================================================
        # ============================Password====================================
        # ========================================================================

        self.password_label = Label(self.window, text="Password ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=495, y=335)

        self.password_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12), show="*")
        self.password_entry.place(x=530, y=370, width=355)  # trebuchet ms

        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.window, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=890, y=377)

        # ========================================================================
        # ============================Login button================================
        # ========================================================================

        self.login = ImageTk.PhotoImage \
            (file='images\\login.png')

        self.login_button = Button(self.window, image=self.login,
                                   font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                   , borderwidth=0, background="white", cursor="hand2", command=self.non_verified_user)
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
                                    , borderwidth=0, background="white", cursor="hand2", command=self.click_forgot)
        self.forgot_button.place(x=820, y=410)

        # ========================================================================
        # ========================Database Label and button=======================
        # ========================================================================

        self.database_label = Label(self.window, text="* You can change your host here: ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold underline"))
        self.database_label.place(x=490, y=623)

        self.database_img = ImageTk.PhotoImage \
            (file='images\\change_host.png')
        self.database_button = Button(self.window, image=self.database_img,
                                      font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                      , borderwidth=0, background="white", cursor="hand2", command=self.click_database)
        self.database_button.place(x=750, y=620)

    def show(self):
        """allow user to show the password in password field"""
        self.hide_button = Button(self.window, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=890, y=377)
        self.password_entry.config(show='')

    def hide(self):
        """allow user to hide the password in password field"""
        self.show_button = Button(self.window, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=890, y=377)
        self.password_entry.config(show='*')

    def validation(self):
        """validates if username/email inputs exists in database or not, if exists and matched with user
        password, allows them to login by calling another method, BaseException is handled in order to avoid
        any runtime errors"""
        try:
            obj_admin_database = Model_class.database_connected.GetDatabase('use cms;')
            self.db_connection.create(obj_admin_database.get_database())

            query = "select * from admin where username = %s OR email= %s;"
            data = self.db_connection.search(query, (self.username_entry.get(), self.username_entry.get()))
            # print(data)
            self.f_username = []
            self.f_password = []
            self.f_email = []
            for values in data:
                current_list = values[2]
                f_username_list = values[1]
                f_password_list = values[3]
                f_email_list = values[2]
                self.f_email.append(f_email_list)
                self.f_username.append(f_username_list)
                self.f_password.append(f_password_list)
                Login.current_user.clear()
                Login.current_user.append(current_list)
            # print(self.f_password)
            # print(self.f_username)
            # print(Login.current_user)
        except BaseException as msg:
            print(msg)
        try:
            if self.username_entry.get() == "":
                messagebox.showerror("Error", "Username can not be empty")
            elif not self.f_username:
                messagebox.showerror("Error", "Username Does not exists")
            elif self.password_entry.get() == "":
                ask = messagebox.askyesnocancel("Error", "Password can not be empty, Would like to Login using OTP")
                if ask is True:
                    messagebox.showinfo("Hold", f"Please Hold while we send OTP to {self.f_email[0]}")
                    self.send_otp_to_login()

            elif self.password_entry.get() != self.f_password[0]:
                messagebox.showerror("Error", "Invalid Password")
            else:
                self.login_success()

        except BaseException as msg:
            messagebox.showerror("Invalid", "Invalid Username or Password")

    def non_verified_user(self):
        """validates if username/email inputs exists in unverified table of database or not, if exists
        it will ask them to verify their email before they can login to the system and guide them to
        verify their password by calling another method, BaseException is handled in order to avoid
        any runtime errors"""
        try:
            obj_admin_database = Model_class.database_connected.GetDatabase('use cms;')
            self.db_connection.create(obj_admin_database.get_database())

            query = "select * from unverified where username = %s OR email = %s ;"
            data = self.db_connection.search(query, (self.username_entry.get(), self.username_entry.get()))
            # print(data)
            self.u_username = []
            self.u_email = []
            for values in data:
                u_username_list = values[1]
                u_email_list = values[2]
                self.u_username.append(u_username_list)
                self.u_email.append(u_email_list)
                Login.non_verified_email.clear()
                Login.non_verified_email.append(u_email_list)
            # print(self.u_username)
            # print(self.u_email)
        except BaseException as msg:
            print(msg)

        if self.u_email:

            try:

                if self.username_entry.get() != "" or self.username_entry.get() != "":
                    try:
                        if self.u_email[0] == self.username_entry.get():
                            ask = messagebox.askyesnocancel("Error",
                                                            "Your Email is not verified\n Please verify your email"
                                                            "\n Would you like to verify your email now?")
                            if ask is True:
                                messagebox.showinfo("Wait", f"Please Hold Until OTP is sent to {self.u_email[0]} ")
                                self.click_send_otp()

                            else:
                                pass

                        elif self.u_username[0] == self.username_entry.get():
                            ask = messagebox.askyesnocancel("Error",
                                                            "Your Email is not verified\n Please verify your email"
                                                            "\n Would you like to verify your email now?")
                            if ask is True:
                                messagebox.showinfo("Wait", f"Please Hold Until OTP is sent to {self.u_email[0]} ")
                                self.click_send_otp()

                            else:
                                pass

                    except BaseException as msg:
                        print(msg)

            except BaseException as msg:
                print(msg)
                messagebox.showerror("Error", "Please Check the details")

        else:
            self.validation()

    def click_send_otp(self):
        """Sends and OTP to the email that a user uses to create admin account, BaseException is handled to avoid
        internet issue or wrong email address that may often happen due to user"""
        if self.username_entry.get() != "":
            try:
                self.value = random.randint(100000, 999999)
                Login.otp.clear()
                Login.otp.append(self.value)
                # print(Login.otp)

                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

                server.login("tkintercms@gmail.com", "tkinter@12345")

                # print(self.u_email[0])

                server.sendmail("tkintercms@gmail.com", f"{self.u_email[0]}", f"Subject: Tkinter-CMS OTP \n\n Your OTP"
                                                                              f" for College Management "
                                                                              f"system is  {self.value}")
                server.quit()
                # messagebox.showinfo("Success", f"OTP have been sent to {self.[0]}")
                # print(DatabaseConnected.otp[0])
                messagebox.showinfo("Notification", f"OTP has been sent to {self.u_email[0]}\n Please verify "
                                                    f"email before you can log in ")
                self.verify_this_user()

            except BaseException as msg:
                print(msg)
                messagebox.showerror("Failed",
                                     "There is an error sending OTP\n Make sure you are connected to internet")

        else:
            messagebox.showerror("Empty", "Please Enter Email Address \nand Click Send OTP")

    def send_otp_to_login(self):
        """Sends and OTP to the email that a user uses to create admin account in order to login to the system
        using OTP instead of password, BaseException is handled to avoid internet issue or wrong email address that
        may often happen due to user"""
        if self.username_entry.get() != "":
            try:
                self.otp = random.randint(100000, 999999)

                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

                server.login("tkintercms@gmail.com", "tkinter@12345")

                # print(self.u_email[0])

                server.sendmail("tkintercms@gmail.com", f"{self.f_email[0]}", f"Subject: Tkinter-CMS Login OTP \n\n "
                                                                              f"Your OTP"
                                                                              f" to get login for College Management "
                                                                              f"system is  {self.otp}")
                server.quit()
                # messagebox.showinfo("Success", f"OTP have been sent to {self.[0]}")
                # print(DatabaseConnected.otp[0])
                messagebox.showinfo("Notification", f"OTP has been sent to {self.f_email[0]}\n Please verify "
                                                    f"OTP before you can log in ")
                self.changing_login_button()
                self.otp_entry()

            except BaseException as msg:
                print(msg)
                messagebox.showerror("Failed",
                                     "There is an error sending OTP\n Make sure you are connected to internet")

        else:
            messagebox.showerror("Empty", "Please Enter Email Address \nand Click Send OTP")

    def changing_login_button(self):
        """Configures the login button if user chosen login using OTP"""
        self.login_button.configure(command=self.verify_login_using_otp)

    def verify_login_using_otp(self):
        """Verifies the OTP to the unique OTP that has been sent to get login access"""
        if self.username_entry.get() and self.password_entry.get() != '':
            if self.otp == int(self.password_entry.get()):
                self.login_success()

            else:
                messagebox.showerror("Empty", "Username or Password can not be empty")

        else:
            messagebox.showerror("Invalid", "Sorry, We can not verify your login")

    def otp_entry(self):
        """Configures the Password label to One Time Password - OTP label when user wants to login to the
        system using OTP instead of login by password"""
        self.show()
        self.password_label.configure(text="One Time Password - OTP")
        self.password_entry.configure(show='')
        self.password_entry.insert(0, "Please Enter your OTP here...")
        self.password_entry.bind('<1>', self.delete_otp_entry)

    def delete_otp_entry(self, events):
        """takes and events argument from user if user click left mouse button in password entry field
        and delete the pre inserted guide"""
        self.password_entry.delete(0, END)

    def verify_this_user(self):
        """in order to verify the user while verifying email, new window is open"""
        win = Toplevel()
        VerifyThisUser(win)
        self.window.withdraw()
        win.deiconify()

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

    def click_forgot(self):
        """when clicked forgot button on login form, it will open interface asking them to verify their email
        address"""
        win = Toplevel()
        Frontend.otp_verification.OtpVerification(win)
        self.window.withdraw()
        win.deiconify()

    def click_database(self):
        """when click on change database button, it will ask them to confirm the change of host address,
        and will also inform them that this confirmation will delete the current host credentials, after
        :returns True, then new window opens up guiding them to setup their host again"""
        ques = messagebox.askyesnocancel("Warning", "Are you sure you want to change Host")
        if ques is True:
            ask = messagebox.askyesnocancel("Confirm", "The previous Host connection\n"
                                                       "will be deleted if you select YES")
            if ask is True:
                f = open("database_data.txt", "wb")
                f.truncate(0)
                messagebox.showinfo("Success!", "Your Host have been deleted successfully")

                win = Toplevel()
                Frontend.connect_database.ConnectDatabase(win)
                self.window.withdraw()
                win.deiconify()

    def login_success(self):
        """after successful login new admin dashboard will open by fetching the current logged in user"""
        win = Toplevel()
        GetCurrentUser(win)
        self.window.withdraw()
        win.deiconify()


class GetCurrentUser(Frontend.admin_dashboard.AdminDashboard):
    """Inherits and extend the functionality of AdminDashboard class, by adding the feature of current active user"""
    def __init__(self, wind):
        """takes window as a argument from login_success() method of class LoginForm  """
        super().__init__(wind)
        user = Login.current_user
        current_user = user[0]
        # print(f"this is {current_user}")
        self.current_user.configure(text=current_user)


class VerifyThisUser(Frontend.non_verified.NonVerified):
    """inherits NonVerified class from non_verified module in order to verify the user email address
    by Validating the OTP and shifts unverified credentials of user to
    verified admin table of database after successful verification of"""
    def __init__(self, wind):
        """takes window as a argument from verify_this_user() method of class LoginForm"""
        super().__init__(wind)
        # print(DatabaseConnected.otp[0])
        self.recent_otp = Login.otp[0]
        self.recent_email = Login.non_verified_email[0]
        # print(self.recent_otp)
        # self.recent_otp_entry = self.otp_entry.get()

        self.verify_button.configure(command=self.validation)

    def validation(self):
        """Validates the OTP and shifts unverified credentials of user to
         verified admin table of database after successful verification of; calling another method
         which will shift the data"""
        # print(DatabaseConnected.otp[0])
        # if self.email_entry.get() == '':
        #     messagebox.showinfo("Empty","Something went wrong\n Please Try again")
        if self.otp_entry.get() == '':
            messagebox.showinfo("Empty", "Please Enter recent OTP from your email")

        if self.recent_otp == int(self.otp_entry.get()):
            messagebox.showinfo("Success", "Your Email have been verified successfully")
            self.shift_user_to_admin()
        else:
            messagebox.showerror("Error", "Sorry, We can not verify your email")

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
                c_password_list = values[3]

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
            self.otp_entry.delete(0, END)
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

            messagebox.showinfo("Success", "You can now login")
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
    Login(window)
    window.mainloop()


if __name__ == '__main__':
    win()
