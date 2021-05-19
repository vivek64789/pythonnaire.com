from tkinter import *
from PIL import ImageTk
from ttkthemes import themed_tk as tk
import random
import Backend.connection
import Model_class.student_registration
import Model_class.database_connected
from tkinter import messagebox
import Frontend.login_form
import Frontend.forgot_password
import smtplib


class OtpVerification:
    """sends OTP to email address that the user want to change the password after forgot password, this will
    send OTP and validates those OTP with user input, if matched another window will open allowing them to
    register new password, otherwise leave them error message displaying system can not verify the user"""
    email = []

    def __init__(self, window):
        """takes window to display all the attributes and Methods for this class"""
        self.window = window
        self.window.geometry("1366x720+0+0")
        self.window.title("Account Verification Page")
        self.window.iconbitmap('images\\logo.ico')
        self.window.resizable(False, False)

        self.db_connection = Backend.connection.DatabaseConnection()
        self.start_verification()

        # print(f"the recent otp is {Frontend.database_connected.DatabaseConnected.otp[0]}")

    def start_verification(self):
        """it starts verification process"""

        self.login_frame = ImageTk.PhotoImage \
            (file='images\\otp_verification_frame.png')
        self.image_panel = Label(self.window, image=self.login_frame)
        # self.image_panel = Label(self.window, image=ph)
        # self.image_panel.image = ph
        self.image_panel.pack(fill='both', expand='yes')

        self.txt = "Account Verification"
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
        # ============================OTP=========================================
        # ========================================================================

        self.otp_label = Label(self.window, text="Recent OTP ", bg="white", fg="#4f4e4d",
                               font=("yu gothic ui", 13, "bold"))
        self.otp_label.place(x=495, y=295)

        self.otp_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                               font=("yu gothic ui semibold", 12))
        self.otp_entry.place(x=530, y=325, width=380)  # trebuchet ms

        # ========================================================================
        # ============================Verify Button================================
        # ========================================================================

        self.verify = ImageTk.PhotoImage \
            (file='images\\verify.png')

        self.verify_button = Button(self.window, image=self.verify,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2",
                                    command=self.click_verification)
        self.verify_button.place(x=640, y=403)

        # ========================================================================
        # ============================Submit button================================
        # ========================================================================

        self.send_otp = ImageTk.PhotoImage \
            (file='images\\send_otp.png')

        self.send_otp_button = Button(self.window, image=self.send_otp,
                                      font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                      , borderwidth=0, background="white", cursor="hand2", command=self.validation)
        self.send_otp_button.place(x=500, y=503)

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
        # ========================Forgot password instruction=====================
        # ========================================================================

        self.forgot_ins_label = Label(self.window, text="* Please enter your email and\n Send OTP to verify your "
                                                        "account ",
                                      bg="white", fg="#4f4e4d",
                                      font=("yu gothic ui", 13, "bold"))
        self.forgot_ins_label.place(x=575, y=573)

    def validation(self):
        """validates if email entry field is left empty, if True
        :returns: info message displaying to enter the email address"""
        if self.email_entry.get() == '':
            messagebox.showinfo("Empty", "Please Enter Email Address")
        else:
            self.click_send_otp()

    def click_send_otp(self):
        """Sends and OTP to the email that a user uses to create admin account, BaseException is handled to avoid
        internet issue or wrong email address that may often happen due to use"""
        if self.email_entry.get() != "":

            try:
                obj_admin_database = Model_class.database_connected.GetDatabase('use cms;')
                self.db_connection.create(obj_admin_database.get_database())

                query = "select * from admin where email = %s;"
                data = self.db_connection.search(query, (self.email_entry.get(),))
                print(data)
                self.f_email = []
                # self.f_password = []
                for values in data:
                    f_email_list = values[2]
                    OtpVerification.email.append(f_email_list)
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

                    server.sendmail("tkintercms@gmail.com", f"{self.f_email[0]}", f"Subject: Tkinter-CMS OTP \n\n Your"
                                                                                  f" OTP for College Management"
                                                                                  f" system is  {self.value}")
                    server.quit()
                    messagebox.showinfo("Success", f"OTP have been sent to {self.f_email[0]}")

                except BaseException as msg:
                    messagebox.showerror("Failed",
                                         "There is an error sending OTP\n Make sure you are connected to internet")

            except BaseException as msg:
                print(msg)
        else:
            messagebox.showerror("Empty", "Please Enter Email Address \nand Click Send OTP")

    def click_verification(self):
        """if OTP entry field is not empty, it will verify the actual OTP with user OTP that they
        entered in OTP field"""
        if self.otp_entry.get() != "":
            print(self.otp_entry.get())
            if int(self.otp_entry.get()) == self.value:
                messagebox.showinfo("Success", "You Have Been Successfully Verified")
                self.update_password()
            else:
                messagebox.showerror("Bad Requests", "Sorry we were not able to identify you")

        else:
            messagebox.showerror("Empty", "Please Enter recent OTP from your email")

    def update_password(self):
        """in order to update the password, it will call another window"""
        win = Toplevel()
        FetchEmail(win)
        self.window.withdraw()
        win.deiconify()

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
        """calls login page when clicked on login button"""
        win = Toplevel()
        Frontend.login_form.Login(win)
        self.window.withdraw()
        win.deiconify()

    def click_exit(self):
        """Terminates the program when if returned True"""
        ask = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to Exit\n College Management System?")
        if ask is True:
            self.window.quit()


class FetchEmail(Frontend.forgot_password.ForgotPassword):
    """inherits ForgotPassword class in order to let user change their password on user interface
    it will fetch the email address of the user that they just validates by OTP and change the password
    in database admin table"""
    def __init__(self, wind):
        super().__init__(wind)
        email = OtpVerification.email
        # print(email)
        self.email_entry.insert(0, email[0])


def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    OtpVerification(window)
    window.mainloop()


if __name__ == '__main__':
    win()
