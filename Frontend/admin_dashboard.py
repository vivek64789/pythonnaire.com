from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from ttkthemes import themed_tk as tk
from datetime import *
import time
import smtplib
import random
import Backend.connection
import Model_class.student_registration
import Model_class.database_connected
from tkinter import messagebox
import Frontend.forgot_password
import Frontend.login_form
import Frontend.manage_student
import Frontend.manage_employee
import Frontend.manage_department
import Frontend.manage_batch
import Frontend.manage_course
import Frontend.manage_section


class AdminDashboard:
    """comes in use when user successfully login to the system, it allows user to view brief information about
    students, employees and department in click_home() method, let user manage the system such as, students,
    employees, department, courses, section, batch from click_manage() method, also it allows user to view partial
    data about students, employees, departments and course from click_view() method. lastly, it also allows them to
    change their current password if they remember current password from click_setting() methods"""
    def __init__(self, window):
        """takes window as arguments to show all the attributes and keep let them get advantage of the methods,
        that have been created to provide them various feature"""
        self.window = window
        self.window.geometry("1366x720+0+0")
        self.window.title("Dashboard")
        self.window.iconbitmap('images\\logo.ico')
        self.window.resizable(False, False)
        self.admin_dashboard_frame = ImageTk.PhotoImage \
            (file='images\\admin_frame.png')
        self.image_panel = Label(self.window, image=self.admin_dashboard_frame)
        self.image_panel.pack(fill='both', expand='yes')

        self.db_connection = Backend.connection.DatabaseConnection()

        self.txt = "Welcome to Admin Dashboard"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.window, text=self.txt, font=('yu gothic ui', 30, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=350, y=26, width=550)
        self.slider()
        self.heading_color()

        # ========================================================================
        # ============================Date and time==============================
        # ========================================================================
        self.clock_image = ImageTk.PhotoImage(file="images/time.png")
        self.date_time_image = Label(self.window, image=self.clock_image, bg="white")
        self.date_time_image.place(x=35, y=45)

        self.date_time = Label(self.window)
        self.date_time.place(x=65, y=35)
        self.time_running()
  
        # ========================================================================
        # ============================Current user================================
        # ========================================================================
        self.current_user_image = ImageTk.PhotoImage(file="images/current_user.png")
        self.current_user_label = Label(self.window, image=self.current_user_image, bg="white")
        self.current_user_label.place(x=1000, y=47)

        self.current_user = Label(self.window, bg="white",
                                  font=("yu gothic ui", 10, "bold"),fg="green")
        self.current_user.place(x=1030, y=48)

        # ========================================================================
        # ============================Home button====================================
        # ========================================================================
        self.home = ImageTk.PhotoImage \
            (file='images\\home.png')
        self.home_button = Button(self.window, image=self.home,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2", command=self.click_home)

        self.home_button.place(x=43, y=113)
        self.click_home()

        # ========================================================================
        # ============================Manage button===============================
        # ========================================================================
        self.manage = ImageTk.PhotoImage \
            (file='images\\manage.png')
        self.manage_button = Button(self.window, image=self.manage,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=self.click_manage)

        self.manage_button.place(x=41, y=233)

        # ========================================================================
        # ============================View button===============================
        # ========================================================================
        self.view = ImageTk.PhotoImage \
            (file='images\\view.png')
        self.view_button = Button(self.window, image=self.view,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2", command=self.click_view)
        self.view_button.place(x=41, y=353)

        # ========================================================================
        # ============================Setting button===============================
        # ========================================================================
        self.setting = ImageTk.PhotoImage \
            (file='images\\setting.png')
        self.setting_button = Button(self.window, image=self.setting,
                                     font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                     , borderwidth=0, background="white", cursor="hand2", command=self.click_setting)
        self.setting_button.place(x=41, y=473)

        # ========================================================================
        # ============================Exit button===============================
        # ========================================================================
        self.exit = ImageTk.PhotoImage \
            (file='images\\exit_button.png')
        self.exit_button = Button(self.window, image=self.exit,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2", command=self.click_exit)
        self.exit_button.place(x=41, y=593)

        # ========================================================================
        # ============================Logout button===============================
        # ========================================================================
        self.logout = ImageTk.PhotoImage \
            (file='images\\logout.png')
        self.logout_button = Button(self.window, image=self.logout,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=self.click_logout)
        self.logout_button.place(x=1241, y=50)

    def click_student_button(self):
        """this opens student management dashboard from where admin can manage the students"""
        win = Toplevel()
        Frontend.manage_student.ManageStudent(win)
        self.window.withdraw()
        win.deiconify()

    def click_home(self):
        """set to default home tab where details like no. of students, employees, department shows """
        home_frame = Frame(self.window)
        home_frame.place(x=145, y=105, height=576, width=1181)

        self.home_dashboard_frame = ImageTk.PhotoImage \
            (file='images\\home_frame.png')
        self.home_panel = Label(home_frame, image=self.home_dashboard_frame, bg="white")
        self.home_panel.pack(fill='both', expand='yes')

        try:
            obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_student_database.get_database())

            query = "SELECT COUNT(*) FROM students;"
            data = self.db_connection.select(query)
            global no_students
            for value in data:
                no_students = value[0]

            total_students = Label(home_frame, text=f" TOTAL\n {no_students}\n STUDENTS",
                                   font=("yu gothic ui", 30, "bold"),
                                   background="white", fg='#e67c0b')
            total_students.place(x=230, y=80)

            query = "SELECT COUNT(*) FROM employees;"
            data = self.db_connection.select(query)
            global no_employees
            for value in data:
                no_employees = value[0]

            total_employees = Label(home_frame, text=f" TOTAL\n {no_employees}\n EMPLOYEES",
                                    font=("yu gothic ui", 30, "bold"),
                                    background="white", fg='#e67c0b')
            total_employees.place(x=720, y=80)

            query = "SELECT COUNT(*) FROM department;"
            data = self.db_connection.select(query)
            global no_department
            for value in data:
                no_department = value[0]

            total_department = Label(home_frame, text=f" TOTAL\n {no_department}\n DEPARTMENTS",
                                     font=("yu gothic ui", 30, "bold"),
                                     background="white", fg='#e67c0b')
            total_department.place(x=190, y=320)

        except BaseException as msg:
            print(msg)

    def click_manage(self):
        """ opens new frame from where one can go to manage students, employees, departments, course, section
        and batch"""
        manage_frame = Frame(self.window, bg="white")
        manage_frame.place(x=145, y=105, height=576, width=1181)

        self.manage_dashboard_frame = ImageTk.PhotoImage \
            (file='images\\manage_frame.png')
        self.manage_panel = Label(manage_frame, image=self.manage_dashboard_frame, bg="white")
        self.manage_panel.pack(fill='both', expand='yes')

        self.student = ImageTk.PhotoImage \
            (file='images\\student.png')
        self.student_button = Button(manage_frame, image=self.student, relief=FLAT, borderwidth=0,
                                     activebackground="white", bg="white", cursor="hand2",
                                     command=self.click_student_button)
        self.student_button.place(x=158, y=157)

        self.employee = ImageTk.PhotoImage \
            (file='images\\employee.png')
        self.employee_button = Button(manage_frame, image=self.employee, relief=FLAT, borderwidth=0,
                                      activebackground="white", bg="white", cursor="hand2",
                                      command=self.click_employee_button)
        self.employee_button.place(x=515, y=156)

        self.department = ImageTk.PhotoImage \
            (file='images\\department.png')
        self.department_button = Button(manage_frame, image=self.department, relief=FLAT, borderwidth=0,
                                        activebackground="white", bg="white", cursor="hand2",
                                        command=self.click_department_button)
        self.department_button.place(x=875, y=156)

        self.course = ImageTk.PhotoImage \
            (file='images\\course.png')
        self.course_button = Button(manage_frame, image=self.course, relief=FLAT, borderwidth=0,
                                    activebackground="white", bg="white", cursor="hand2",
                                    command=self.click_course_button)
        self.course_button.place(x=158, y=395)

        self.section = ImageTk.PhotoImage \
            (file='images\\section.png')
        self.section_button = Button(manage_frame, image=self.section, relief=FLAT, borderwidth=0,
                                     activebackground="white", bg="white", cursor="hand2",
                                     command=self.click_section_button)
        self.section_button.place(x=518, y=395)

        self.batch = ImageTk.PhotoImage \
            (file='images\\batch.png')
        self.batch_button = Button(manage_frame, image=self.batch, relief=FLAT, borderwidth=0,
                                   activebackground="white", bg="white", cursor="hand2",
                                   command=self.click_batch_button)
        self.batch_button.place(x=876, y=395)

    def click_view(self):
        """ Displays partial data into tree view of students, employees, departments, courses when clicked view tab
        on interface """
        view_frame = Frame(self.window, bg="white")
        view_frame.place(x=145, y=105, height=576, width=1181)

        self.view_dashboard_frame = ImageTk.PhotoImage \
            (file='images\\view_frame.png')
        self.view_panel = Label(view_frame, image=self.view_dashboard_frame, bg="white")
        self.view_panel.pack(fill='both', expand='yes')

        self.department_view_label = Label(view_frame, text="View Department Information ", bg="white", fg="#4f4e4d",
                                           font=("yu gothic ui", 13, "bold"))
        self.department_view_label.place(x=770, y=290)

        self.course_view_label = Label(view_frame, text="View Course Information ", bg="white", fg="#4f4e4d",
                                       font=("yu gothic ui", 13, "bold"))
        self.course_view_label.place(x=170, y=290)

        # ========================================================================
        # ============================Displaying Student Information==============
        # ========================================================================

        self.student_view_label = Label(view_frame, text="View Students Information ", bg="white", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
        self.student_view_label.place(x=170, y=6)

        self.view_student_frame = Frame(view_frame, bg="white")
        self.view_student_frame.place(x=10, y=40, height=250, width=575)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('yu gothic ui', 10, "bold"), foreground="red")
        style.configure("Treeview", font=('yu gothic ui', 9, "bold"), foreground="#f29b0f")

        scroll_y = Scrollbar(self.view_student_frame, orient=VERTICAL)
        scroll_x = Scrollbar(self.view_student_frame, orient=HORIZONTAL)
        self.view_student_tree = ttk.Treeview(self.view_student_frame,
                                              columns=(
                                                  "STUDENT ID", "STUDENT NAME", "COURSE ENROLLED", "PHONE NO."),
                                              xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.view_student_tree.xview)
        scroll_y.config(command=self.view_student_tree.yview)

        # ==========================TreeView Heading====================
        self.view_student_tree.heading("STUDENT ID", text="STUDENT ID")
        self.view_student_tree.heading("STUDENT NAME", text="STUDENT NAME")
        self.view_student_tree.heading("COURSE ENROLLED", text="COURSE ENROLLED")
        self.view_student_tree.heading("PHONE NO.", text="PHONE NO.")
        self.view_student_tree["show"] = "headings"

        # ==========================TreeView Column====================
        self.view_student_tree.column("STUDENT ID", width=50)
        self.view_student_tree.column("STUDENT NAME", width=150)
        self.view_student_tree.column("COURSE ENROLLED", width=150)
        self.view_student_tree.column("PHONE NO.", width=100)
        self.view_student_tree.pack(fill=BOTH, expand=1)

        # ========================================================================
        # =========================Displaying instructor Information==============
        # ========================================================================

        self.view_employee_frame = Frame(view_frame, bg="white")
        self.view_employee_frame.place(x=595, y=40, height=250, width=575)

        self.employee_view_label = Label(view_frame, text="View Employees Information ", bg="white", fg="#4f4e4d",
                                         font=("yu gothic ui", 13, "bold"))
        self.employee_view_label.place(x=770, y=6)

        scroll_y_e = Scrollbar(self.view_employee_frame, orient=VERTICAL)
        scroll_x_e = Scrollbar(self.view_employee_frame, orient=HORIZONTAL)
        self.view_employee_tree = ttk.Treeview(self.view_employee_frame,
                                               columns=(
                                                   "EMPLOYEE ID", "EMPLOYEE NAME", "DEPARTMENT", "EMPLOYEE TYPE"),
                                               xscrollcommand=scroll_x_e.set, yscrollcommand=scroll_y_e.set)
        scroll_x_e.pack(side=BOTTOM, fill=X)
        scroll_y_e.pack(side=RIGHT, fill=Y)
        scroll_x_e.config(command=self.view_employee_tree.xview)
        scroll_y_e.config(command=self.view_employee_tree.yview)

        # ==========================TreeView Heading====================
        self.view_employee_tree.heading("EMPLOYEE ID", text="EMPLOYEE ID")
        self.view_employee_tree.heading("EMPLOYEE NAME", text="EMPLOYEE NAME")
        self.view_employee_tree.heading("DEPARTMENT", text="DEPARTMENT")
        self.view_employee_tree.heading("EMPLOYEE TYPE", text="EMPLOYEE TYPE")
        self.view_employee_tree["show"] = "headings"

        # ==========================TreeView Column====================
        self.view_employee_tree.column("EMPLOYEE ID", width=50)
        self.view_employee_tree.column("EMPLOYEE NAME", width=150)
        self.view_employee_tree.column("DEPARTMENT", width=100)
        self.view_employee_tree.column("EMPLOYEE TYPE", width=100)
        self.view_employee_tree.pack(fill=BOTH, expand=1)

        # ========================================================================
        # =========================Displaying Course Information==============
        # ========================================================================

        self.view_course_frame = Frame(view_frame, bg="white")
        self.view_course_frame.place(x=10, y=320, height=250, width=575)

        scroll_y_e = Scrollbar(self.view_course_frame, orient=VERTICAL)
        scroll_x_e = Scrollbar(self.view_course_frame, orient=HORIZONTAL)
        self.view_course_tree = ttk.Treeview(self.view_course_frame,
                                             columns=(
                                                 "COURSE ID", "COURSE NAME", "COURSE DURATION", "COURSE CREDIT"),
                                             xscrollcommand=scroll_x_e.set, yscrollcommand=scroll_y_e.set)
        scroll_x_e.pack(side=BOTTOM, fill=X)
        scroll_y_e.pack(side=RIGHT, fill=Y)
        scroll_x_e.config(command=self.view_course_tree.xview)
        scroll_y_e.config(command=self.view_course_tree.yview)

        # ==========================TreeView Heading====================
        self.view_course_tree.heading("COURSE ID", text="COURSE ID")
        self.view_course_tree.heading("COURSE NAME", text="COURSE NAME")
        self.view_course_tree.heading("COURSE DURATION", text="COURSE DURATION")
        self.view_course_tree.heading("COURSE CREDIT", text="COURSE CREDIT")
        self.view_course_tree["show"] = "headings"

        # ==========================TreeView Column====================
        self.view_course_tree.column("COURSE ID", width=50)
        self.view_course_tree.column("COURSE NAME", width=150)
        self.view_course_tree.column("COURSE DURATION", width=100)
        self.view_course_tree.column("COURSE CREDIT", width=100)
        self.view_course_tree.pack(fill=BOTH, expand=1)

        # ========================================================================
        # =========================Displaying Department Information==============
        # ========================================================================

        self.view_department_frame = Frame(view_frame, bg="white")
        self.view_department_frame.place(x=595, y=320, height=250, width=575)

        scroll_y_e = Scrollbar(self.view_department_frame, orient=VERTICAL)
        scroll_x_e = Scrollbar(self.view_department_frame, orient=HORIZONTAL)
        self.view_department_tree = ttk.Treeview(self.view_department_frame,
                                                 columns=(
                                                     "DEPARTMENT ID", "DEPARTMENT NAME", "DEPARTMENT CODE"),
                                                 xscrollcommand=scroll_x_e.set, yscrollcommand=scroll_y_e.set)
        scroll_x_e.pack(side=BOTTOM, fill=X)
        scroll_y_e.pack(side=RIGHT, fill=Y)
        scroll_x_e.config(command=self.view_department_tree.xview)
        scroll_y_e.config(command=self.view_department_tree.yview)

        # ==========================TreeView Heading====================
        self.view_department_tree.heading("DEPARTMENT ID", text="DEPARTMENT ID")
        self.view_department_tree.heading("DEPARTMENT NAME", text="DEPARTMENT NAME")
        self.view_department_tree.heading("DEPARTMENT CODE", text="DEPARTMENT CODE")
        self.view_department_tree["show"] = "headings"

        # ==========================TreeView Column====================
        self.view_department_tree.column("DEPARTMENT ID", width=50)
        self.view_department_tree.column("DEPARTMENT NAME", width=150)
        self.view_department_tree.column("DEPARTMENT CODE", width=100)
        self.view_department_tree.pack(fill=BOTH, expand=1)

        self.view_student_information()
        self.view_employee_information()
        self.view_course_information()
        self.view_department_information()

    def view_student_information(self):
        """fetched data of students from database and inserted required index to student tree view"""
        try:
            obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_student_database.get_database())

            query = "select * from students;"
            data = self.db_connection.select(query)
            self.a = Label(self.window)
            # print(data)
            self.view_student_tree.delete(*self.view_student_tree.get_children())
            for values in data:
                data_list = [values[0], values[4], values[11], values[9]]
                # print(data_list)
                self.view_student_tree.insert('', END, values=data_list)

        except BaseException as msg:
            print(msg)

    def view_employee_information(self):
        """fetched data of employees from database and inserted required index to employee tree view"""
        try:
            obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_student_database.get_database())

            query = "select * from employees;"
            data = self.db_connection.select(query)
            # print(data)
            # self.view_employee_tree.delete(*self.view_employee_tree.get_children())
            for values in data:
                data_list = [values[0], values[4], values[13], values[11]]
                # print(data_list)
                self.view_employee_tree.insert('', END, values=data_list)

        except BaseException as msg:
            print(msg)

    def view_course_information(self):
        """fetched data of course from database and inserted required index to course tree view"""
        try:
            obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_student_database.get_database())

            query = "select * from course;"
            data = self.db_connection.select(query)
            # print(data)
            # self.view_course_tree.delete(*self.view_course_tree.get_children())
            for values in data:
                data_list = [values[0], values[1], values[2], values[3]]
                # print(data_list)
                self.view_course_tree.insert('', END, values=data_list)

        except BaseException as msg:
            print(msg)

    def view_department_information(self):
        """fetched data of department from database and inserted required index to department tree view"""
        try:
            obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_student_database.get_database())

            query = "select * from department;"
            data = self.db_connection.select(query)
            # print(data)
            self.view_department_tree.delete(*self.view_department_tree.get_children())
            for values in data:
                data_list = [values[0], values[2], values[1]]
                # print(data_list)
                self.view_department_tree.insert('', END, values=data_list)

        except BaseException as msg:
            print(msg)

    def click_setting(self):
        """ Allows user to change their password using old password, validations, update entry data to database
        table containing that email or username is done in this method"""
        setting_frame = Frame(self.window, bg="white")
        setting_frame.place(x=145, y=105, height=576, width=1181)
        self.setting_dashboard_frame = ImageTk.PhotoImage \
            (file='images\\setting_frame.png')
        self.setting_panel = Label(setting_frame, image=self.setting_dashboard_frame, bg="white")
        self.setting_panel.pack(fill='both', expand='yes')

        txt = "Change Password"

        heading = Label(setting_frame, text=txt, font=('yu gothic ui', 20, "bold"), bg="white",
                        fg='black',
                        bd=5,
                        relief=FLAT)
        heading.place(x=410, y=27, width=350)

        # ========================================================================
        # ============================Username====================================
        # ========================================================================

        self.username_label = Label(setting_frame, text="Username ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=415, y=90)

        self.username_entry = Entry(setting_frame, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 11))
        self.username_entry.place(x=450, y=118, width=300)  # trebuchet ms

        # ========================================================================
        # ============================PreviousPassword============================
        # ========================================================================

        self.p_password_label = Label(setting_frame, text="Old Password ", bg="white", fg="#4f4e4d",
                                      font=("yu gothic ui", 13, "bold"))
        self.p_password_label.place(x=415, y=180)

        self.p_password_entry = Entry(setting_frame, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                      font=("yu gothic ui semibold", 12),show='*' )
        self.p_password_entry.place(x=450, y=207, width=300)  # trebuchet ms

        # ========================================================================
        # ============================New Password============================
        # ========================================================================

        self.n_password_label = Label(setting_frame, text="New Password ", bg="white", fg="#4f4e4d",
                                      font=("yu gothic ui", 13, "bold"))
        self.n_password_label.place(x=415, y=270)

        self.n_password_entry = Entry(setting_frame, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                      font=("yu gothic ui semibold", 12),show='*')
        self.n_password_entry.place(x=450, y=298, width=300)  # trebuchet ms

        # ========================================================================
        # ============================Confirm Password============================
        # ========================================================================

        self.c_password_label = Label(setting_frame, text="Confirm Password ", bg="white", fg="#4f4e4d",
                                      font=("yu gothic ui", 13, "bold"))
        self.c_password_label.place(x=415, y=360)

        self.c_password_entry = Entry(setting_frame, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                      font=("yu gothic ui semibold", 12),show='*')
        self.c_password_entry.place(x=450, y=388, width=300)  # trebuchet ms

        # ========================================================================
        # ============================Submit button================================
        # ========================================================================

        self.submit = ImageTk.PhotoImage \
            (file='images\\submit.png')

        self.submit_button = Button(setting_frame, image=self.submit,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2",
                                    command = self.validation)
        self.submit_button.place(x=520, y=450)

    def validation(self):
        """validation in order to check if username exists or not that the user want to change the password of"""
        try:
            obj_admin_database = Model_class.database_connected.GetDatabase('use cms;')
            self.db_connection.create(obj_admin_database.get_database())

            query = "select * from admin where username = %s;"
            data = self.db_connection.search(query,(self.username_entry.get(),))
            print(data)
            self.f_username = []
            self.f_password = []
            self.f_email = []
            for values in data:
                f_username_list = values[1]
                f_password_list = values[3]
                f_email_list = values[2]
                self.f_email.append(f_email_list)
                self.f_username.append(f_username_list)
                self.f_password.append(f_password_list)
            print(self.f_password)
            print(self.f_username)
        except BaseException as msg:
            print(msg)
        try:
            if self.username_entry.get() == "":
                messagebox.showerror("Error", "Username can not be empty")
            elif not self.f_username:
                messagebox.showerror("Error","Username Does not exists")
            elif self.p_password_entry.get() == "":
                messagebox.showerror("Error", "You must enter Old Password")
            elif self.n_password_entry.get() == "":
                messagebox.showerror("Error", "New Password can not be empty")
            elif self.n_password_entry.get() == self.p_password_entry.get():
                messagebox.showerror("Error", "New Password must be different from old password")
            elif self.c_password_entry.get() == "":
                messagebox.showerror("Error", "You must confirm Password")
            elif self.n_password_entry.get() != self.c_password_entry.get():
                messagebox.showerror("Error","Confirm Password Does not matched")
            elif self.username_entry.get() != self.f_username[0]:
                messagebox.showerror("Error", "Invalid Old Password")
            elif self.p_password_entry.get() != self.f_password[0]:
                messagebox.showerror("Error", "Invalid Old Password")
            else:
                self.update_password()

        except BaseException as msg:
            messagebox.showerror("Invalid","Invalid Username or Password")

    def update_password(self):
        """ updates the password of entry fields into the admin table of database where username is from username
        entry fields"""
        try:
            obj_admin_database = Model_class.database_connected.GetDatabase('use cms;')
            self.db_connection.create(obj_admin_database.get_database())

            obj_admin_database = Model_class.database_connected.DatabaseConnected(
                self.f_username[0], self.n_password_entry.get())

            query = 'update admin set password=%s where username=%s;'
            values = (obj_admin_database.get_password(),obj_admin_database.get_username())
            # print(values)
            self.db_connection.insert(query, values)
            # print(values)
            messagebox.showinfo("Success", "Password Updated Successfully")
            self.clear_update_password()
            c_email = self.f_email[0]
            print(c_email)

            c_time = time.strftime('%H:%M:%S')
            c_date = time.strftime('%Y/%m/%d')
            print(c_time)
            print(c_date)

            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

            server.login("tkintercms@gmail.com", "tkinter@12345")

            server.sendmail("tkintercms@gmail.com", f"{c_email}", f"Subject: Tkinter-CMS "
                                                                                 f"Password changed \n\n "
                                                                                 f"Your "
                                                                                 f" Password for College Management was "
                                                                                 f"Changed Recently "
                                                                                 f" at Time  {c_time}"
                                                                                 f"at Date  {c_date}")
            server.quit()

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error", "There is some error Submitting Credentials ")

    def clear_update_password(self):
        """clear the entry form of setting tab"""
        self.username_entry.delete(0,END)
        self.p_password_entry.delete(0,END)
        self.n_password_entry.delete(0,END)
        self.c_password_entry.delete(0,END)

    def click_employee_button(self):
        """opens employee window where admin can manage the employee data"""
        win = Toplevel()
        Frontend.manage_employee.ManageEmployee(win)
        self.window.withdraw()
        win.deiconify()

    def click_department_button(self):
        """opens department window where admin can manage the department data"""
        win = Toplevel()
        Frontend.manage_department.ManageDepartment(win)
        self.window.withdraw()
        win.deiconify()

    def click_course_button(self):
        """opens course window where admin can manage the course data"""
        win = Toplevel()
        Frontend.manage_course.ManageCourse(win)
        self.window.withdraw()
        win.deiconify()

    def click_section_button(self):
        """opens section window where admin can manage the section data"""
        win = Toplevel()
        Frontend.manage_section.ManageSection(win)
        self.window.withdraw()
        win.deiconify()

    def click_batch_button(self):
        """opens batch window where admin can manage the batch data"""
        win = Toplevel()
        Frontend.manage_batch.ManageBatch(win)
        self.window.withdraw()
        win.deiconify()

    def click_exit(self):
        """ Allows user to terminates the program when chosen yes"""
        self.window.deiconify()
        ask = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to Exit\n Student Registration Form?")
        if ask is True:
            self.window.quit()

    def click_logout(self):
        """Logouts the user to login page from where they will require password in order to login again"""
        win = Toplevel()
        Frontend.login_form.Login(win)
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
        configures heading label every 50 ms
        :return: new random color.

        """
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)

    def time_running(self):
        """ displays the current date and time which is shown at top left corner of admin dashboard"""
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%Y/%m/%d')
        concated_text = f"  {self.time} \n {self.date}"
        self.date_time.configure(text=concated_text, font=("yu gothic ui", 13, "bold"), relief=FLAT
                                 , borderwidth=0, background="white", foreground="black")
        self.date_time.after(100, self.time_running)


def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    AdminDashboard(window)
    window.mainloop()


if __name__ == '__main__':
    win()
