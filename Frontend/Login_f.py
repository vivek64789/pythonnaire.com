from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from datetime import *
import time
from math import *
import Backend.connection
import Model_class.student_registration
from tkinter import messagebox


# creating window
class Login_form:
    """creating class to create login form as student, teacher, and admin will log into"""

    def __init__(self, wind, image, logo, user, username_icon, password_icon, login_button, register_button):
        self.window = wind
        self.window.title('COLLEGE MANAGEMENT SYSTEM')
        self.window.geometry('1366x786+0+0')

        # ======================Backend connection=============
        # self.connect = Backend.Connection.Database_connection()

        # ========background image===========
        self.background_img = image
        self.image_panel = Label(self.window, image=self.background_img)
        self.image_panel.pack(fill='both', expand='yes')

        # creating frame for Register
        self.reg_frame = Frame(self.window, bg='#13857D', width=900, height=500)
        self.reg_frame.place(x=240, y=140)

        self.heading = Label(self.reg_frame, text='LOGIN', font=('arial', 20, 'bold'), bg="#13857D", fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=300, y=110, width=600)

        # creating frame for Register inputs
        self.reg_frame2 = Frame(self.reg_frame, bg='white', width=300, heigh=500)
        self.reg_frame2.place(x=0)
        #
        # self.reg_frame3 = Frame(self.reg_frame, bg='white', width=600, heigh=70)
        # self.reg_frame3.place(x=300, y=450)

        self.logo_img = logo
        self.image_panel = Label(self.window, image=self.logo_img, height=180, width=180, bg="white")
        self.image_panel.place(x=300, y=190)

        self.user_logo = user
        self.user_label = Label(self.reg_frame, image=self.user_logo, bg="#13857D")
        self.user_label.place(x=565, y=40)

        self.username_icon = username_icon
        self.username_label = Label(self.reg_frame, image=self.username_icon, bg="#13857D")
        self.username_label.place(x=390, y=180)

        self.password_icon = password_icon
        self.password_label = Label(self.reg_frame, image=self.password_icon, bg="#13857D")
        self.password_label.place(x=390, y=230)

        self.login_button = login_button
        self.login_btn = Button(self.reg_frame, image=self.login_button, borderwidth=0, activebackground="#13857D",
                                bg="#13857D",cursor="hand2",command=self.login)
        self.login_btn.place(x=525, y=250)

        self.register_button = register_button
        self.register_btn = Button(self.reg_frame, image=self.register_button, borderwidth=0,
                                   activebackground="#13857D",
                                   bg="#13857D",cursor="hand2")
        self.register_btn.place(x=629, y=279)

        # ====================Entry and button for Login form=================================

        # =======================================================================================
        # =============================== ID Entry and Label ====================================
        # =======================================================================================

        self.id_login = Label(self.reg_frame, text="Username:", font=("Helvetica", 15, "bold"), bg="#13857D",
                              fg="white")
        self.id_login.place(x=430, y=183)

        self.id_entry_login = Entry(self.reg_frame, font=("Helvetica", 10, "bold"))
        self.id_entry_login.place(x=540, y=187, width=200)

        # =======================================================================================
        # =============================== ID Entry and Label ====================================
        # =======================================================================================

        self.pass_login = Label(self.reg_frame, text="Password:", font=("Helvetica", 15, "bold"), bg="#13857D",
                                fg="white")
        self.pass_login.place(x=430, y=233)

        self.id_entry_password = Entry(self.reg_frame, font=("Helvetica", 10, "bold"))
        self.id_entry_password.place(x=540, y=237, width=200)

    def login(self):
        username = self.id_entry_login
        password = self.id_entry_password
        login_object= Model_class.student_registration.Registration()
        print(login_object.get_id())

class Clock:
    def __init__(self, win_):
        self.window = win_

        # ==========Clock image=============
        self.clock_label = Label(self.window, bg="white")  # ,bd=10, relief=RAISED)
        self.clock_label.place(x=280, y=380, height=220, width=220)
        # self.clock_image()
        self.clock_usable()

    def clock_image(self, h_, min_, sec_):
        clock_img = Image.new("RGB", (300, 300), (255, 255, 255))
        draw_img = ImageDraw.Draw(clock_img)
        bg = Image.open("images\\clockNew.jpg")
        bg = bg.resize((200, 200), Image.ANTIALIAS)
        clock_img.paste(bg, (50, 50))

        center = 150, 150
        # ============= Clock hour Line===========
        draw_img.line((center, 150 + 30 * sin(radians(h_)), 150 - 30 * cos(radians(h_))), fill="white", width=4)

        # ============= Clock Minutes Line===========
        draw_img.line((center, 150 + 50 * sin(radians(min_)), 150 - 50 * cos(radians(min_))), fill="white", width=3)

        # ============= Clock Seconds Line===========
        draw_img.line((center, 150 + 60 * sin(radians(sec_)), 150 - 60 * cos(radians(sec_))), fill="white", width=2)

        # ============= Clock Eclipse===========
        draw_img.ellipse((147, 147, 153, 153), fill="black")
        clock_img.save(
            "images\\clock_new_image.png")

    def clock_usable(self):
        hour = datetime.now().time().hour
        minutes = datetime.now().time().minute
        seconds = datetime.now().time().second
        print(hour, minutes, seconds)
        h_ = (hour / 12) * 360
        min_ = (minutes / 60) * 360
        sec_ = (seconds / 60) * 360
        print(h_, min_, sec_)
        self.clock_image(h_, min_, sec_)
        self.show_img = ImageTk.PhotoImage(file="images\\clock_new_image.png")
        self.clock_label.config(image=self.show_img)
        self.clock_label.after(200, self.clock_usable)


def win():
    window = Tk()
    b_image = ImageTk.PhotoImage(Image.open('images\\background.jpg'))
    l_image = ImageTk.PhotoImage(Image.open("images\\CMSlogo.png"))
    u_image = ImageTk.PhotoImage(Image.open("images\\user.png"))

    username_icon = ImageTk.PhotoImage(Image.open("images\\username_icon.png"))

    password_icon = ImageTk.PhotoImage(Image.open("images\\security.png"))

    login_button = ImageTk.PhotoImage(Image.open("images\\login_100.png"))

    register_button = ImageTk.PhotoImage(Image.open("images\\register.png"))
    Login_form(window, b_image, l_image, u_image, username_icon, password_icon, login_button, register_button)
    Clock(window)
    window.mainloop()


if __name__ == '__main__':
    win()
