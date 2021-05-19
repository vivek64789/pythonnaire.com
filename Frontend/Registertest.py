from tkinter import *
from tkinter import ttk
from tkcalendar import *
from PIL import ImageTk, Image, ImageDraw
from datetime import *
import time
from math import *
import Backend.connection
import Model_class.student_registration
from tkinter import messagebox
import os


# creating window
class Register_form:
    def __init__(self, wind, image, logo):
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

        self.heading = Label(self.reg_frame, text='REGISTER HERE', font=('arial', 20, 'bold'), bg="white", fg='#13857D',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=0, y=0, width=600)

        # creating frame for Register inputs
        self.reg_frame2 = Frame(self.reg_frame, bg='white', width=300, heigh=500)
        self.reg_frame2.place(x=600)

        self.reg_frame3 = Frame(self.reg_frame, bg='white', width=600, heigh=70)
        self.reg_frame3.place(x=0, y=450)

        self.logo_img = logo
        self.image_panel = Label(self.window, image=self.logo_img, height=180, width=180, bg="white")
        self.image_panel.place(x=895, y=190)

        # ====================Entry and button for register page=================================

        # =======================================================================================
        # =============================== ID Entry and Label ====================================
        # =======================================================================================

        self.id_label = Label(self.reg_frame, text="ID", font=("Helvetica", 15, "bold"), bg="#13857D", fg="white")
        self.id_label.place(x=20, y=60)

        self.id_entry = Entry(self.reg_frame, highlightthickness=0, relief=FLAT, bg="#13857D", fg="white",
                              font=("Helvetica", 10, "bold"))
        self.id_entry.place(x=230, y=60, width=300)

        canva = Canvas(self.reg_frame, width=300, height=2, bg="black", highlightthickness=0)
        canva.place(x=230, y=80)

        # =======================================================================================
        # ============================= Username Entry and Label ================================
        # =======================================================================================

        self.username_label = Label(self.reg_frame, text="Username", font=("Halvetica", 15, "bold"), bg="#13857D",
                                    fg="white")
        self.username_label.place(x=20, y=95)

        self.username_entry = Entry(self.reg_frame, font=("Helvetica", 10, "bold"))
        self.username_entry.place(x=230, y=95, width=300)

        # =======================================================================================
        # ============================= email address Entry and Label ===========================
        # =======================================================================================

        self.email_label = Label(self.reg_frame, text="Email address", font=("Helvetica", 15, "bold"), bg="#13857D",
                                 fg="white")
        self.email_label.place(x=20, y=130)

        self.email_entry = Entry(self.reg_frame, font=("Helvetica", 10, "bold"))
        self.email_entry.place(x=230, y=130, width=300)

        # =======================================================================================
        # ============================= password Entry and Label ================================
        # =======================================================================================

        self.pass_label = Label(self.reg_frame, text="Password", font=("Helvetica", 15, "bold"), bg="#13857D",
                                fg="white")
        self.pass_label.place(x=20, y=165)

        self.pass_entry = Entry(self.reg_frame, font=("Helvetica", 10, "bold"), show="*")
        self.pass_entry.place(x=230, y=165, width=300)

        # =======================================================================================
        # ============================= confirm password Entry and Label ========================
        # =======================================================================================

        self.c_pass_label = Label(self.reg_frame, text="Confirm Password", font=("Helvetica", 15, "bold"), bg="#13857D",
                                  fg="white")
        self.c_pass_label.place(x=20, y=200)

        self.c_pass_entry = Entry(self.reg_frame, font=("Helvetica", 10, "bold"), show="*")
        self.c_pass_entry.place(x=230, y=200, width=300)

        # =======================================================================================
        # ============================= First name Entry and Label ==============================
        # =======================================================================================

        self.f_name_label = Label(self.reg_frame, text="First name", font=("Helvetica", 15, "bold"), bg="#13857D",
                                  fg="white")
        self.f_name_label.place(x=20, y=235)

        self.f_name_entry = Entry(self.reg_frame, font=("Helvetica", 10, "bold"))
        self.f_name_entry.place(x=230, y=235, width=300)

        # =======================================================================================
        # ============================= Last name Entry and Label ===============================
        # =======================================================================================

        self.l_name_label = Label(self.reg_frame, text="Last name", font=("Helvetica", 15, "bold"), bg="#13857D",
                                  fg="white")
        self.l_name_label.place(x=20, y=270)

        self.l_name_entry = Entry(self.reg_frame, font=("Helvetica", 10, "bold"))
        self.l_name_entry.place(x=230, y=270, width=300)
        self.l_name_entry.bind("<Tab>", self.pick_date)

        # =======================================================================================
        # ============================= DOB Entry and Label =====================================
        # =======================================================================================

        self.b_date_label = Label(self.reg_frame, text="DOB", font=("Helvetica", 15, "bold"), bg="#13857D",
                                  fg="white")
        self.b_date_label.place(x=20, y=305)

        self.b_date_entry = Entry(self.reg_frame, font=("Helvetica", 10, "bold"), fg="grey")
        self.b_date_entry.insert(0, "mm/dd/yyyy")
        self.b_date_entry.place(x=230, y=305, width=300)

        self.b_date_entry.bind("<1>", self.pick_date)

        # =======================================================================================
        # ============================= Register as Entry and Label =============================
        # =======================================================================================

        self.reg_as_label = Label(self.reg_frame, text="Register as", font=("Helvetica", 15, "bold"), bg="#13857D",
                                  fg="white")
        self.reg_as_label.place(x=20, y=340)

        self.reg_as_entry = Entry(self.reg_frame, font=("Helvetica", 10, "bold"))
        self.reg_as_entry.place(x=230, y=340, width=300)

        # =======================================================================================
        # ============================= Register Batch no =============================
        # =======================================================================================

        self.batch_no_label = Label(self.reg_frame, text="Batch No", font=("Helvetica", 15, "bold"), bg="#13857D",
                                    fg="white")
        self.batch_no_label.place(x=20, y=375)

        self.batch_no_entry = Entry(self.reg_frame, font=("Helvetica", 10, "bold"))
        self.batch_no_entry.place(x=230, y=375, width=300)

        # =======================================================================================
        # ============================= Register Course ID =============================
        # =======================================================================================

        self.course_id_label = Label(self.reg_frame, text="Course Id", font=("Helvetica", 15, "bold"), bg="#13857D",
                                     fg="white")
        self.course_id_label.place(x=20, y=410)

        self.course_id_entry = Entry(self.reg_frame, font=("Helvetica", 10, "bold"))
        self.course_id_entry.place(x=230, y=410, width=300)

        # =======================================================================================
        # ============================= Register Button =========================================
        # =======================================================================================
        self.reg_button = Button(self.reg_frame3, text="REGISTER", font=("Helvetica", 10, "bold"), bg="#13857D",
                                 fg="white", command=self.add)
        self.reg_button.place(x=230, y=10)

        # =======================================================================================
        # ============================= Clear form Button =========================================
        # =======================================================================================

        self.c_form_button = Button(self.reg_frame3, text="CLEAR FORM", font=("Helvetica", 10, "bold"),
                                    bg="#13857D", fg="white")
        self.c_form_button.place(x=360, y=10)

        # =======================================================================================
        # ============================= lOGIN Button =========================================
        # =======================================================================================

        self.r_login_button = Button(self.reg_frame3, text="LOGIN NOW", font=("Helvetica", 10, "bold"),
                                     bg="#13857D", fg="white")
        self.r_login_button.place(x=510, y=10)

        # ==================date picker==============================

    def pick_date(self, event):
        self.date_win = Tk()
        self.date_win.title('Choose Date of Birth')
        self.date_win.geometry('250x220+590+370')
        self.cal = Calendar(self.date_win, selectmode="day", date_pattern="mm/dd/y")
        self.cal.place(x=0, y=0)

        self.okay_btn = Button(self.date_win, text="Ok", bg="green", command=self.grab_date)
        self.okay_btn.place(x=110, y=190)

    def grab_date(self):
        self.b_date_entry.delete(0, END)
        self.b_date_entry.config(fg="black")
        self.b_date_entry.insert(0, self.cal.get_date())
        self.date_win.destroy()

    def add(self):
        register_object = Model_class.student_registration.Registration(self.id_entry.get(), self.username_entry.get(),
                                                                        self.email_entry.get(), self.pass_entry.get(),
                                                                        self.f_name_entry.get(),
                                                                        self.l_name_entry.get(), self.reg_as_entry.get(),
                                                                        self.course_id_entry.get(),
                                                                        self.batch_no_entry.get())
        print(register_object.get_id())
        query = """insert into registration values (%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
        values = (int(register_object.get_id()), register_object.get_username(), register_object.get_email(),
                  register_object.get_password(), register_object.get_f_name(), register_object.get_l_name(),
                  register_object.get_reg_as(), register_object.get_course_id(), register_object.get_batch_id())

        self.connect.insert(query, values)
        messagebox.showinfo("Success", "Data inserted successfully")


class Clock:
    def __init__(self, win_):
        self.window = win_

        # ==========Clock image=============
        self.clock_label = Label(self.window, bg="white")  # ,bd=10, relief=RAISED)
        self.clock_label.place(x=880, y=380, height=220, width=220)
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
    Register_form(window, b_image, l_image)
    Clock(window)
    window.mainloop()


if __name__ == '__main__':
    win()


