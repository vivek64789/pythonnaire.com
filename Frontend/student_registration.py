from tkinter import *
from tkinter import ttk
from tkcalendar import *
from PIL import ImageTk, Image, ImageDraw
from ttkthemes import themed_tk as tk
from tkinter import messagebox
from datetime import *
import time
from math import *
import random
import Backend.connection
import Model_class.student_registration
import Frontend.manage_student


# creating window
class RegisterForm:
    """allows admin to register students, it validates, if that username and email address already exists or not, if
    it  exists then proper error message is thrown to let them know that these user already exists. all the validations
    of entry fields are done here for registration form so that in order to add students all fields are required.
    before able to add students, there are pre requisites need to be fulfilled, such as course, batch and section
    should already been added other wise error message showing those data should be added first are being displayed.
    to avoid the error if pre requisites is not fulfilled exception handling is done while setting current index
    of combobox"""
    def __init__(self, wind):
        self.window = wind
        self.window.title('COLLEGE MANAGEMENT SYSTEM')
        self.window.geometry('1366x786+0+0')
        self.window.config(bg="#f29844")
        self.window.iconbitmap('images\\logo.ico')
        self.window.resizable(False, False)
        self.manage_student_frame = ImageTk.PhotoImage \
            (file='images\\student_frame.png')

        # # win= Toplevel()
        # a= Frontend.manage_student.ManageStudent.list_of_tree
        # print(a)

        # ======================Backend connection=============
        self.db_connection = Backend.connection.DatabaseConnection()

        # ======================Variables======================

        self.reg_frame = Frame(self.window, bg="#ffffff", width=1300, height=680)
        self.reg_frame.place(x=30, y=30)

        self.txt = "Student Registration Form"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]

        self.heading = Label(self.reg_frame, text=self.txt, font=('yu gothic ui', 30, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=350, y=0, width=600)
        self.slider()
        self.heading_color()

        self.cred_frame = LabelFrame(self.reg_frame, text="Account Details", bg="white", fg="#4f4e4d", height=140,
                                     width=800, borderwidth=2.4,
                                     font=("yu gothic ui", 13, "bold"))
        self.cred_frame.config(highlightbackground="red")
        self.cred_frame.place(x=100, y=100)

        # ========================================================================
        # ============================Key Bindings====================================
        # ========================================================================

        self.window.bind("<Return>", self.click_enter_submit)

        # ========================================================================
        # ============================Username====================================
        # ========================================================================

        self.username_label = Label(self.cred_frame, text="Username ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=10, y=10)

        self.username_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.username_entry.place(x=230, y=167, width=260)  # trebuchet ms

        self.username_line = Canvas(self.window, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=230, y=189)

        # ========================================================================
        # ============================Email=======================================
        # ========================================================================

        self.email_label = Label(self.cred_frame, text="Email ", bg="white", fg="#4f4e4d",
                                 font=("yu gothic ui", 13, "bold"))
        self.email_label.place(x=370, y=10)

        self.email_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                 font=("yu gothic ui semibold", 12))
        self.email_entry.place(x=555, y=167, width=350)  # trebuchet ms

        self.email_line = Canvas(self.window, width=350, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.email_line.place(x=555, y=189)

        # ========================================================================
        # ============================Password====================================
        # ========================================================================

        self.password_label = Label(self.cred_frame, text="Password ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=10, y=50)

        self.password_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12), show="*")
        self.password_entry.place(x=230, y=207, width=260)  # trebuchet ms

        self.password_line = Canvas(self.window, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=230, y=230)

        # ========================================================================
        # ============================Confirm password============================
        # ========================================================================

        self.c_password_label = Label(self.cred_frame, text="Confirm Password ", bg="white", fg="#4f4e4d",
                                      font=("yu gothic ui", 13, "bold"))
        self.c_password_label.place(x=370, y=50)

        self.c_password_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                      font=("yu gothic ui semibold", 12), show="*")
        self.c_password_entry.place(x=650, y=207, width=255)  # trebuchet ms

        self.c_password_line = Canvas(self.window, width=255, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.c_password_line.place(x=650, y=230)

        # =======================================================================
        # ========================frame for personal credentials ================
        # =======================================================================

        self.personal_frame = LabelFrame(self.reg_frame, text="Personal Details", bg="white", fg="#4f4e4d", height=265,
                                         width=800, borderwidth=2.4,
                                         font=("yu gothic ui", 13, "bold"))
        self.personal_frame.config(highlightbackground="red")
        self.personal_frame.place(x=100, y=260)

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
        # ============================First name==================================
        # ========================================================================
        self.f_name_label = Label(self.personal_frame, text="First Name ", bg="white", fg="#4f4e4d",
                                  font=("yu gothic ui", 13, "bold"))
        self.f_name_label.place(x=10, y=10)

        self.f_name_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                  font=("yu gothic ui semibold", 12))
        self.f_name_entry.place(x=235, y=327, width=260)  # trebuchet ms

        self.f_name_line = Canvas(self.window, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.f_name_line.place(x=235, y=349)

        # ========================================================================
        # ============================Last name===================================
        # ========================================================================

        self.l_name_label = Label(self.personal_frame, text="Last Name ", bg="white", fg="#4f4e4d",
                                  font=("yu gothic ui", 13, "bold"))
        self.l_name_label.place(x=370, y=10)

        self.l_name_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                  font=("yu gothic ui semibold", 12))
        self.l_name_entry.place(x=595, y=327, width=315)  # trebuchet ms

        self.l_name_line = Canvas(self.window, width=315, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.l_name_line.place(x=595, y=349)

        # ========================================================================
        # ============================DOB=========================================
        # ========================================================================

        self.dob_label = Label(self.personal_frame, text="DOB ", bg="white", fg="#4f4e4d",
                               font=("yu gothic ui", 13, "bold"))
        self.dob_label.place(x=10, y=50)

        self.dob_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                               font=("yu gothic ui semibold", 12))
        self.dob_entry.insert(0, "mm/dd/yyyy")
        self.dob_entry.place(x=190, y=367, width=305)  # trebuchet ms
        self.dob_entry.bind("<1>", self.pick_date)

        self.dob_line = Canvas(self.window, width=305, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.dob_line.place(x=190, y=389)

        # ========================================================================
        # ===========================Gender=======================================
        # ========================================================================
        style = ttk.Style()

        # style.map('TCombobox', selectbackground=[('readonly', 'grey')])
        self.window.option_add("*TCombobox*Listbox*Foreground", '#f29844')

        self.gender_label = Label(self.personal_frame, text="Gender ", bg="white", fg="#4f4e4d",
                                  font=("yu gothic ui", 13, "bold"))
        self.gender_label.place(x=370, y=50)

        self.gender_combo = ttk.Combobox(self.window, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                         width=35)

        gender_list = ['Male', 'Female', 'Rather not say']
        self.gender_combo['values'] = gender_list
        # self.gender_combo.current(0)
        self.gender_combo.place(x=570, y=367)

        # self.gender_line = Canvas(self.window, width=315, height=1.5, bg="#bdb9b1", highlightthickness=0)
        # self.gender_line.place(x=595, y=369)

        # ========================================================================
        # ============================Address====================================
        # ========================================================================

        self.address_label = Label(self.personal_frame, text="Address ", bg="white", fg="#4f4e4d",
                                   font=("yu gothic ui", 13, "bold"))
        self.address_label.place(x=10, y=90)

        self.address_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                   font=("yu gothic ui semibold", 12))
        self.address_entry.place(x=215, y=407, width=280)  # trebuchet ms

        self.address_line = Canvas(self.window, width=280, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.address_line.place(x=215, y=429)

        # ========================================================================
        # ============================Contact no====================================
        # ========================================================================

        self.contact_label = Label(self.personal_frame, text="Contact No. ", bg="white", fg="#4f4e4d",
                                   font=("yu gothic ui", 13, "bold"))
        self.contact_label.place(x=370, y=90)

        self.contact_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                   font=("yu gothic ui semibold", 12))
        self.contact_entry.place(x=605, y=407, width=305)  # trebuchet ms

        self.contact_line = Canvas(self.window, width=305, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.contact_line.place(x=605, y=429)

        # ========================================================================
        # ============================Shift No====================================
        # ========================================================================

        self.shift_label = Label(self.personal_frame, text="Shift ", bg="white", fg="#4f4e4d",
                                 font=("yu gothic ui", 13, "bold"))
        self.shift_label.place(x=10, y=130)

        self.shift_combo = ttk.Combobox(self.window, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                        width=28)
        shift_list = ["Morning", "Day", "Evening"]
        self.shift_combo['values'] = shift_list
        self.shift_combo.current(0)
        self.shift_combo.place(x=213, y=447)

        try:
            obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_student_database.get_database())

            query = "select * from section"
            section_tuple = self.db_connection.select(query)
            # print(section_tuple)
            self.section_list = []
            for i in section_tuple:
                section_name = i[2]
                self.section_list.append(section_name)
                # print(section_name)
                # print(self.section_list)

        except BaseException as msg:
            print(msg)

        try:
            obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_student_database.get_database())

            query = "select * from course"
            course_tuple = self.db_connection.select(query)
            # print(course_tuple)
            self.course_list = []
            for i in course_tuple:
                course_name = i[1]
                self.course_list.append(course_name)
                # print(course_name)
                # print(self.course_list)

        except BaseException as msg:
            print(msg)

        try:
            obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_student_database.get_database())

            query = "select * from batch"
            batch_tuple = self.db_connection.select(query)
            # print(batch_tuple)
            self.batch_list = []
            for i in batch_tuple:
                batch_name = i[1]
                self.batch_list.append(batch_name)
                # print(batch_name)
                # print(self.batch_list)

        except BaseException as msg:
            print(msg)

        # ========================================================================
        # ============================Course enrolled=============================
        # ========================================================================

        self.course_label = Label(self.personal_frame, text="Course Enrolled ", bg="white", fg="#4f4e4d",
                                  font=("yu gothic ui", 13, "bold"))
        self.course_label.place(x=370, y=130)

        self.course_combo = ttk.Combobox(self.window, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                         width=28)

        self.course_combo['values'] = self.course_list
        try:
            self.course_combo.current(0)
        except:
            messagebox.showerror("Error","You must add course first")
        self.course_combo.place(x=635, y=447)

        # ========================================================================
        # ============================Batch=======================================
        # ========================================================================

        self.batch_label = Label(self.personal_frame, text="Batch ", bg="white", fg="#4f4e4d",
                                 font=("yu gothic ui", 13, "bold"))
        self.batch_label.place(x=10, y=170)

        self.batch_combo = ttk.Combobox(self.window, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                        width=28)

        self.batch_combo['values'] = self.batch_list
        try:
            self.batch_combo.current(0)
        except:
            messagebox.showerror("Error", "You must add batch first")
        self.batch_combo.place(x=213, y=487)

        # ========================================================================
        # ============================Section=====================================
        # ========================================================================

        self.section_label = Label(self.personal_frame, text="Section ", bg="white", fg="#4f4e4d",
                                   font=("yu gothic ui", 13, "bold"))
        self.section_label.place(x=370, y=170)

        self.section_combo = ttk.Combobox(self.window, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                          width=28)

        self.section_combo['values'] = self.section_list
        try:
            self.section_combo.current(0)
        except:
            messagebox.showerror("Error", "You must add section first")
        self.section_combo.place(x=635, y=487)

        self.reg_date = time.strftime("%Y/%m/%d")

        # ========================================================================
        # ============================Register options=====================================
        # ========================================================================

        self.options_frame = LabelFrame(self.reg_frame, text="Register Options", bg="white", fg="#4f4e4d", height=95,
                                        width=800, borderwidth=2.4,
                                        font=("yu gothic ui", 13, "bold"))
        self.options_frame.config(highlightbackground="red")
        self.options_frame.place(x=100, y=545)

        # ========================================================================
        # ============================Register options=====================================
        # ========================================================================
        self.submit_img = ImageTk.PhotoImage \
            (file='images\\submit.png')

        self.submit = Button(self.options_frame, image=self.submit_img,
                             font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                             , borderwidth=0, background="white", cursor="hand2", command=self.validation)
        self.submit.place(x=90, y=10)

        self.clear_img = ImageTk.PhotoImage \
            (file='images\\clear.png')
        self.clear_button = Button(self.options_frame, image=self.clear_img,
                                   font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                   , borderwidth=0, background="white", cursor="hand2",
                                   command=self.click_clear_button)
        self.clear_button.place(x=250, y=13)

        self.back_img = ImageTk.PhotoImage \
            (file='images\\back.png')
        self.back_button = Button(self.options_frame, image=self.back_img,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2", command=self.click_back_button)
        self.back_button.place(x=410, y=13)

        self.exit_img = ImageTk.PhotoImage \
            (file='images\\exit.png')
        self.exit_button = Button(self.options_frame, image=self.exit_img,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2", command=self.exit)
        self.exit_button.place(x=570, y=13)

    def click_back_button(self):
        """returns ManageStudent class if clicked on back button"""
        win = Toplevel()
        Frontend.manage_student.ManageStudent(win)
        self.window.withdraw()
        win.deiconify()

    def pick_date(self, event):
        """left click event is being handled when trying to add DOB"""
        self.date_win = tk.ThemedTk()
        self.date_win.get_themes()
        self.date_win.set_theme("arc")
        self.date_win.grab_set()
        self.date_win.title('Choose Date of Birth')
        self.date_win.geometry('250x220+500+370')
        self.cal = Calendar(self.date_win, selectmode="day", date_pattern="mm/dd/y")
        self.cal.place(x=0, y=0)

        self.okay_btn = ttk.Button(self.date_win, text="Okay", command=self.grab_date)
        self.okay_btn.place(x=80, y=180)

    def grab_date(self):
        """Grabs the date that being handled in pick_date() methods"""
        self.dob_entry.delete(0, END)
        self.dob_entry.config(fg="#6b6a69")
        self.dob_entry.insert(0, self.cal.get_date())
        self.date_win.destroy()

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

        configures heading label every 50 ms
        :return: new random color.

        """
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)

    def click_enter_submit(self,events):
        """events for return or enter key is handled and validation method is called"""
        self.validation()

    def validation(self):
        """this will validate if the username and email of entry fields are already in database table named student or
        not if return True, error message is thrown displaying email/username already exists"""
        try:
            obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_student_database.get_database())

            query = "select * from students;"
            data = self.db_connection.select(query)
            # print(data)
            self.username_list = []
            self.email_list = []
            for values in data:
                # print(values)
                user_data_list = values[1]
                self.username_list.append(user_data_list)
                email_data_list = values[2]
                self.email_list.append(email_data_list)
                # print(self.final_list)
                # print(self.data_list)
        except BaseException as msg:
            print(msg)

        if self.username_entry.get() == "" or self.email_entry.get() == "" or self.password_entry.get() == "" \
                or self.f_name_entry.get() == "" or self.l_name_entry.get() == "" or self.dob_entry.get() == "" \
                or self.address_entry.get() == "" or self.contact_entry.get() == "":
            messagebox.showwarning("Warning", "All Fields are Required\n Please fill all required fields")

        elif self.username_entry.get() in self.username_list:
            messagebox.showerror("Already Exists", f"{self.username_entry.get()} username Already Exists")

        elif self.email_entry.get() in self.email_list:
            messagebox.showerror("Already Exists", f"{self.email_entry.get()} Email ID Already Exists")

        elif self.password_entry.get() != self.c_password_entry.get():
            messagebox.showerror("Not Matched", "Password Does not Matched")

        else:
            self.click_submit()

    def click_submit(self):
        """initialize when click submit button, which will take data from entry box
        and insert those data into student table after successful validation of those data"""
        try:
            obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_student_database.get_database())

            obj_student_database = Model_class.student_registration.StudentRegistration(self.username_entry.get(),
                                                                                        self.email_entry.get(),
                                                                                        self.password_entry.get(),
                                                                                        self.f_name_entry.get(),
                                                                                        self.l_name_entry.get(),
                                                                                        self.dob_entry.get(),
                                                                                        self.gender_combo.get(),
                                                                                        self.address_entry.get(),
                                                                                        self.contact_entry.get(),
                                                                                        self.shift_combo.get(),
                                                                                        self.course_combo.get(),
                                                                                        self.batch_combo.get(),
                                                                                        self.section_combo.get(),
                                                                                        self.reg_date)
            query = 'insert into students (username,email,password,f_name,l_name,dob,gender,address,' \
                    'contact_no,shift,course_enrolled,batch,section_enrolled,reg_date) values (%s,%s,%s,%s,%s,%s,' \
                    '%s,%s,%s,%s,%s,%s,%s,%s);'
            values = (obj_student_database.get_username(), obj_student_database.get_email(),
                      obj_student_database.get_password(), obj_student_database.get_f_name(),
                      obj_student_database.get_l_name(), obj_student_database.get_dob(),
                      obj_student_database.get_gender(), obj_student_database.get_address(),
                      obj_student_database.get_contact(), obj_student_database.get_shift(),
                      obj_student_database.get_course_id(), obj_student_database.get_batch_id(),
                      obj_student_database.get_section(), obj_student_database.get_reg_date())
            # print(values)
            self.db_connection.insert(query, values)
            # print(values)
            messagebox.showinfo("Success", f"Data inserted Successfully\n Username={values[0]},\n "
                                           f"Password={values[1]}")

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error", "There is some error Submitting Credentials ")

    def click_clear_button(self):
        """this will clear entire field to default when click on clear button"""
        self.username_entry.delete(0, END)
        self.f_name_entry.delete(0, END)
        self.l_name_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.c_password_entry.delete(0, END)
        self.dob_entry.delete(0, END)
        self.gender_combo.current(0)
        self.address_entry.delete(0, END)
        self.contact_entry.delete(0, END)
        self.shift_combo.current(0)
        self.batch_combo.current(0)
        self.course_combo.current(0)
        self.batch_combo.current(0)
        self.section_combo.current(0)

    def exit(self):
        ask = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to Exit\n Student Registration Form?")
        if (ask == True):
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
        try:
            self.show_img = ImageTk.PhotoImage(file="images\\clock_new_image.png")
        except:
            pass
        self.clock_label.config(image=self.show_img)
        self.clock_label.after(200, self.clock_usable)


def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    RegisterForm(window)
    Clock(window)
    window.mainloop()


if __name__ == '__main__':
    win()
