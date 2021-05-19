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
import Model_class.course_registration
from tkinter import messagebox
import Frontend.manage_course
import os


class CourseRegisterForm:
    """allows admin to register courses, it validates, if that course code and name already exists or not, if
    it  exists then proper error message is thrown to let them know that these course already exists. all the validations
    of entry fields are done here for registration form so that in order to add courses all fields are required.
    """
    def __init__(self, wind):
        self.window = wind
        self.window.title('COURSE REGISTRATION FORM - COLLEGE MANAGEMENT SYSTEM')
        self.window.geometry('1366x786+0+0')
        self.window.config(bg="#f29844")

        # ======================Backend connection=============
        self.db_connection = Backend.connection.DatabaseConnection()

        self.reg_frame = Frame(self.window, bg="#ffffff", width=1300, height=680)
        self.reg_frame.place(x=30, y=30)

        self.txt = "Course Registration Form"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]

        self.heading = Label(self.reg_frame, text=self.txt, font=('yu gothic ui', 30, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=170, y=70, width=600)
        self.slider()
        self.heading_color()

        self.course_frame = LabelFrame(self.reg_frame, text="Course Details", bg="white", fg="#4f4e4d", height=380,
                                       width=800, borderwidth=2.4,
                                       font=("yu gothic ui", 13, "bold"))
        self.course_frame.config(highlightbackground="red")
        self.course_frame.place(x=100, y=170)

        # ========================================================================
        # ============================Key Bindings====================================
        # ========================================================================

        self.window.bind("<Return>", self.click_enter_submit)


        self.course_name_label = Label(self.course_frame, text="Course Name ", bg="white", fg="#4f4e4d",
                                       font=("yu gothic ui", 13, "bold"))
        self.course_name_label.place(x=160, y=65)

        self.course_name_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                       font=("yu gothic ui semibold", 12))
        self.course_name_entry.place(x=410, y=292, width=335)  # trebuchet ms

        self.course_name_line = Canvas(self.window, width=335, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.course_name_line.place(x=410, y=314)

        # ========================================================================
        # ===========================Course Duration==================================
        # ========================================================================

        self.course_duration_label = Label(self.course_frame, text="Course Duration ", bg="white", fg="#4f4e4d",
                                           font=("yu gothic ui", 13, "bold"))
        self.course_duration_label.place(x=160, y=115)

        self.course_duration_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                           font=("yu gothic ui semibold", 12))
        self.course_duration_entry.place(x=430, y=342, width=315)  # trebuchet ms

        self.course_duration_line = Canvas(self.window, width=315, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.course_duration_line.place(x=430, y=364)

        # ========================================================================
        # ===========================Course Credit==================================
        # ========================================================================

        self.course_credit_label = Label(self.course_frame, text="Course Credit ", bg="white", fg="#4f4e4d",
                                         font=("yu gothic ui", 13, "bold"))
        self.course_credit_label.place(x=160, y=165)

        self.course_credit_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                         font=("yu gothic ui semibold", 12))
        self.course_credit_entry.place(x=410, y=392, width=335)  # trebuchet ms

        self.course_credit_line = Canvas(self.window, width=335, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.course_credit_line.place(x=410, y=414)

        self.reg_date = time.strftime("%Y/%m/%d")

        # =======================================================================
        # ========================frame for information==========================
        # =======================================================================

        self.info_frame = LabelFrame(self.reg_frame, text="                                        "
                                                          "                         ",
                                     bg="white", fg="#4f4e4d", height=560,
                                     width=340, borderwidth=2.4,
                                     font=("yu gothic ui", 13, "bold"))
        self.info_frame.config(highlightbackground="red")
        self.info_frame.place(x=930, y=80)

        # ======================================
        self.logo_img = ImageTk.PhotoImage \
            (file='images\\cms_logo.png')

        self.logo = ttk.Label(self.info_frame, image=self.logo_img,
                              font=("yu gothic ui", 13, "bold"), background="white")
        self.logo.place(x=70, y=20)
        # ========================================
        self.author = ttk.Label(self.info_frame, text="Developed by Bibekanand Kushwaha\n             Coventry ID: "
                                                      "190352",
                                font=("yu gothic ui", 13, "bold"), background="white")
        self.author.place(x=20, y=470)

        # ========================================================================
        # ============================Register options=====================================
        # ========================================================================
        self.submit_img = ImageTk.PhotoImage \
            (file='images\\submit.png')

        self.submit = Button(self.course_frame, image=self.submit_img,
                             font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                             , borderwidth=0, background="white", cursor="hand2",command=self.validation)
        self.submit.place(x=90, y=267)

        self.clear_img = ImageTk.PhotoImage \
            (file='images\\clear.png')
        self.clear_button = Button(self.course_frame, image=self.clear_img,
                                   font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                   , borderwidth=0, background="white", cursor="hand2",
                                   command=self.click_clear_button)
        self.clear_button.place(x=250, y=270)

        self.back_img = ImageTk.PhotoImage \
            (file='images\\back.png')
        self.back_button = Button(self.course_frame, image=self.back_img,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2", command=self.click_back_button)
        self.back_button.place(x=410, y=270)

        self.exit_img = ImageTk.PhotoImage \
            (file='images\\exit.png')
        self.exit_button = Button(self.course_frame, image=self.exit_img,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2", command=self.exit)
        self.exit_button.place(x=570, y=270)

    def click_clear_button(self):
        # self.course_id_entry.delete(0, END)
        self.course_name_entry.delete(0, END)
        self.course_duration_entry.delete(0, END)
        self.course_credit_entry.delete(0, END)

    def click_back_button(self):
        """returns ManageCourse class if clicked on back button"""
        win = Toplevel()
        Frontend.manage_course.ManageCourse(win)
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
        """configures heading label every 50 ms
        :return: new random color."""
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)

    def click_enter_submit(self,events):
        self.validation()

    def validation(self):
        """this will validate if the course code and name of entry fields are already in database table named
        course or not if return True, error message is thrown displaying course code/name already exists"""
        try:
            obj_course_database = Model_class.course_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_course_database.get_database())

            query = "select * from course;"
            data = self.db_connection.select(query)
            # print(data)
            self.name_list = []
            for values in data:
                name_data_list = values[1]
                self.name_list.append(name_data_list)
        except BaseException as msg:
            print(msg)

        if self.course_name_entry.get() == "" or self.course_duration_entry.get() == "" or \
                self.course_credit_entry.get() == "" :
            messagebox.showwarning("Warning", "All Fields are Required\n Please fill all required fields")

        elif self.course_name_entry.get() in self.name_list:
            messagebox.showerror("Already Exists", f"{self.course_name_entry.get()} Course Already Exists")

        else:
            self.click_submit()

    def click_submit(self):
        """initialize when click submit button, which will take data from entry box
        and insert those data into student table after successful validation of those data"""
        try:
            obj_course_database = Model_class.course_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_course_database.get_database())

            obj_course_database = Model_class.course_registration.CourseRegistration(self.course_name_entry.get(),
                                                                                      self.course_duration_entry.get(),
                                                                                      self.course_credit_entry.get(),
                                                                                      self.reg_date)
            query = 'insert into course (course_name,course_duration,course_credit,reg_date) values (%s,%s,%s,%s);'
            values = (obj_course_database.get_name(),obj_course_database.get_duration(),
                      obj_course_database.get_credit(),obj_course_database.get_reg_date())
            # print(values)
            self.db_connection.insert(query, values)
            # print(values)
            messagebox.showinfo("Success", f"Data inserted Successfully\n Course name={values[0]}")

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error", f"There is some error Submitting Credentials")

    def exit(self):
        ask = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to Exit\n College Management System?")
        if ask is True:
            self.window.destroy()


class Clock:
    """this creates an working clock using different module, and displayed those function onto
    a clock image which is static"""
    def __init__(self, win_):
        self.window = win_

        # ==========Clock image=============
        self.clock_label = Label(self.window, bg="white")  # ,bd=10, relief=RAISED)
        self.clock_label.place(x=1020, y=340, height=220, width=220)
        # self.clock_image()
        self.clock_usable()

    def clock_image(self, h_, min_, sec_):
        """this will draw a new image having hight, width and it takes parameter for hour, minutes and seconds"""
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
        """this make clock to movable by calling it recursively after every 200 ms """
        hour = datetime.now().time().hour
        minutes = datetime.now().time().minute
        seconds = datetime.now().time().second
        # print(hour, minutes, seconds)
        h_ = (hour / 12) * 360
        min_ = (minutes / 60) * 360
        sec_ = (seconds / 60) * 360
        # print(h_, min_, sec_)
        self.clock_image(h_, min_, sec_)
        self.show_img = ImageTk.PhotoImage(file="images\\clock_new_image.png")
        self.clock_label.config(image=self.show_img)
        self.clock_label.after(200, self.clock_usable)


def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    CourseRegisterForm(window)
    Clock(window)
    window.mainloop()


if __name__ == '__main__':
    win()
