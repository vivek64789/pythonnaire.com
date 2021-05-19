from tkinter import *
from PIL import ImageTk
from ttkthemes import themed_tk as tk
import random
import Backend.connection


class NonVerified:
    """this is user interface to verify OTP for those user who are not verfied but have already created an account"""
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x720+0+0")
        self.window.title("Verify Registration")
        self.window.iconbitmap('images\\logo.ico')
        self.window.resizable(False, False)
        self.login_frame = ImageTk.PhotoImage \
            (file='images\\login_frame.png')
        self.image_panel = Label(self.window, image=self.login_frame)
        self.image_panel.pack(fill='both', expand='yes')

        self.txt = "Verify Registration"
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
        # ============================OTP ICON====================================
        # ========================================================================

        self.correct = ImageTk.PhotoImage \
            (file='images\\correct.png')

        self.username_label = Label(self.window, image= self.correct, bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=480, y=160, height = 150, width = 440)

        self.email_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        # self.email_entry.place(x=530, y=255, width=380)  # trebuchet ms

        # ========================================================================
        # ============================Recent OTP====================================
        # ========================================================================

        self.otp_label = Label(self.window, text="Recent OTP ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.otp_label.place(x=495, y=335)

        self.otp_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.otp_entry.place(x=530, y=370, width=380)  # trebuchet ms

        # ========================================================================
        # ============================Verify button================================
        # ========================================================================

        self.verify = ImageTk.PhotoImage \
            (file='images\\verify.png')

        self.verify_button = Button(self.window, image=self.verify,
                                   font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                   , borderwidth=0, background="white", cursor="hand2")
        self.verify_button.place(x=630, y=450)


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


def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    NonVerified(window)
    window.mainloop()


if __name__ == '__main__':
    win()
