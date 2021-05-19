from tkinter import *
from PIL import ImageTk
from ttkthemes import themed_tk as tk
import random
import Backend.connection
import Model_class.student_registration
import Frontend.login_form
from tkinter import messagebox
import Frontend.database_connected
import Model_class.connect_database
import pickle
import os


class ConnectDatabase:
    """This class allows user to connect with host and database using GUI,
    user can choose their host, port, username, and password of their proxy server"""
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x720+0+0")
        self.window.title("Database Connection Form")
        self.window.iconbitmap('images\\logo.ico')
        self.window.resizable(False, False)
        self.db_connection = Backend.connection.DatabaseConnection()

        # SaveDatabaseHost()

        self.login_frame = ImageTk.PhotoImage \
            (file='images\\connect_database_frame.png')
        self.image_panel = Label(self.window, image=self.login_frame)
        # self.image_panel = Label(self.window, image=ph)
        # self.image_panel.image = ph
        self.image_panel.pack(fill='both', expand='yes')

        self.txt = "Connect Database Here"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.window, text=self.txt, font=('yu gothic ui', 30, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=470, y=40, width=450)
        self.slider()
        self.heading_color()

        # ========================================================================
        # ============================Host========================================
        # ========================================================================

        self.host_label = Label(self.window, text="Host Name ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
        self.host_label.place(x=495, y=130)

        self.host_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                font=("yu gothic ui semibold", 12))
        self.host_entry.insert(0, "localhost")
        self.host_entry.place(x=530, y=163, width=380)  # trebuchet ms

        # ========================================================================
        # ============================Port====================================
        # ========================================================================

        self.port_label = Label(self.window, text="Port ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
        self.port_label.place(x=495, y=225)

        self.port_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                font=("yu gothic ui semibold", 12))
        self.port_entry.insert(0, "3306")
        self.port_entry.place(x=530, y=253, width=380)  # trebuchet ms

        # ========================================================================
        # ============================Username====================================
        # ========================================================================

        self.username_label = Label(self.window, text="Username ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=495, y=318)

        self.username_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.username_entry.insert(0, "root")
        self.username_entry.place(x=530, y=348, width=380)  # trebuchet ms

        # ========================================================================
        # ============================Password====================================
        # ========================================================================

        self.password_label = Label(self.window, text="Password ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=495, y=410)

        self.password_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.password_entry.insert(0, "root")
        self.password_entry.place(x=530, y=440, width=380)  # trebuchet ms

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
                                   , borderwidth=0, background="white", cursor="hand2", command=self.click_login)
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
        # ========================Wipe Database============================
        # ========================================================================

        self.wipe_img = ImageTk.PhotoImage \
            (file='images\\wipe.png')
        self.wipe_button = Button(self.window, image=self.wipe_img,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2", command=self.click_wipe)
        self.wipe_button.place(x=640, y=575)

        # ========================================================================
        # ========================Database instruction============================
        # ========================================================================

        self.database_ins_label = Label(self.window, text="* Please enter the database login\n credentials of your "
                                                          "server\n and submit it. ", bg="white", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
        self.database_ins_label.place(x=575, y=615)

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

    def store_database(self):

        """
        takes user input for host connection and store them into .txt file
        by pickling it into binary form
        """

        self.dictcred = {}

        le = os.path.getsize("database_data.txt")

        host = self.host_entry.get()
        port = self.port_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        # only if user input is not empty
        if host == "" or port == "" or username == "":
            messagebox.showinfo("Empty", "Please fill up all details")

        else:
            self.listcred1 = [host, port, username, password]
            di = {1: self.listcred1}

            if le == 0:
                f = open("database_data.txt", "wb")
                self.dictcred.update(di)
                pickle.dump(self.dictcred, f)
                messagebox.showinfo("Success!", "Your data have been saved successfully")
                f.close()

            else:
                messagebox.showerror("Exists", "Database is already connected")

    def click_submit(self):
        """

        if there is any value in .txt file, it creates new database named 'cms'
        after then all the required database table are created.

        """

        try:
            le = os.path.getsize("database_data.txt")
            if le == 0:
                obj_connect_db = Model_class.connect_database.ConnectDatabase(self.host_entry.get(),
                                                                              self.port_entry.get(),
                                                                              self.username_entry.get(),
                                                                              self.password_entry.get())
                self.db_connection.d_connection(obj_connect_db.get_host(), obj_connect_db.get_port(),
                                                obj_connect_db.get_username(),
                                                obj_connect_db.get_password())
                messagebox.showinfo("Success", "Database Connection Successful")
                self.store_database()
            else:
                messagebox.showerror("Error", "Database may already connected")

            try:
                obj_create_database = Model_class.connect_database.CreateDatabase('create database cms;')
                self.db_connection.create(obj_create_database.get_database())
                messagebox.showinfo("Success", "Database \n cms\n created Successfully")
            except:
                obj_create_database = Model_class.connect_database.CreateDatabase('use cms;')
                self.db_connection.create(obj_create_database.get_database())
                messagebox.showerror("Error", "Database Creation Failed, \nDatabase May already exists!")
                return

            try:
                obj_create_database = Model_class.connect_database.CreateDatabase('use cms;')
                self.db_connection.create(obj_create_database.get_database())

                obj_create_database = Model_class.connect_database.CreateDatabase \
                    ('create table unverified(id int NOT NULL AUTO_INCREMENT, username varchar(256) NOT NULL,email '
                     'varchar(100) NOT NULL , password varchar(254) NOT NULL, PRIMARY KEY (id), UNIQUE KEY (username),'
                     'UNIQUE KEY (email))')
                self.db_connection.create(obj_create_database.get_database())

                obj_create_database = Model_class.connect_database.CreateDatabase \
                    ('create table admin(id int NOT NULL AUTO_INCREMENT, username varchar(256) NOT NULL,email '
                     'varchar(100) NOT NULL , password varchar(254) NOT NULL, PRIMARY KEY (id), UNIQUE KEY (username),'
                     'UNIQUE KEY (email))')
                self.db_connection.create(obj_create_database.get_database())

                obj_create_database = Model_class.connect_database.CreateDatabase \
                    ('create table batch(batch_id int NOT NULL AUTO_INCREMENT, batch_name varchar(50) NOT NULL,'
                     'batch_year varchar(10) NOT NULL, batch_intake varchar(20) NOT NULL,'
                     'PRIMARY KEY (batch_id), UNIQUE KEY (batch_name), reg_date date);')
                self.db_connection.create(obj_create_database.get_database())

                obj_create_database = Model_class.connect_database.CreateDatabase \
                    ('create table course(course_id int NOT NULL AUTO_INCREMENT, course_name varchar(50) NOT NULL,'
                     'course_duration varchar(10) NOT NULL, course_credit varchar(20) NOT NULL, reg_date date,'
                     'PRIMARY KEY (course_id), UNIQUE KEY (course_name));')
                self.db_connection.create(obj_create_database.get_database())

                obj_create_database = Model_class.connect_database.CreateDatabase \
                    ('create table section(section_id int NOT NULL AUTO_INCREMENT, section_code varchar(50) NOT NULL,'
                     'section_name varchar(50) NOT NULL, section_capacity int NOT NULL,'
                     'PRIMARY KEY (section_id), UNIQUE KEY (section_name), reg_date date);')
                self.db_connection.create(obj_create_database.get_database())

                obj_create_database = Model_class.connect_database.CreateDatabase \
                    ('create table department(department_id int NOT NULL AUTO_INCREMENT, department_code varchar(50) '
                     'NOT NULL,'
                     'department_name varchar(50) NOT NULL,'
                     'PRIMARY KEY (department_id), UNIQUE KEY (department_name), reg_date date);')
                self.db_connection.create(obj_create_database.get_database())

                obj_create_database = Model_class.connect_database.CreateDatabase \
                    ('create table students(student_id int NOT NULL AUTO_INCREMENT,'
                     'username varchar(254) NOT NULL, email varchar(50) NOT NULL,'
                     'password varchar(254) NOT NULL,f_name varchar(50) NOT NULL,'
                     'l_name varchar(50), dob varchar(20),gender varchar(10),'
                     'address varchar(30), contact_no int(13) NOT NULL,shift varchar(20) NOT NULL,'
                     'course_enrolled varchar(50) NOT NULL,batch varchar(50) NOT NULL,'
                     'section_enrolled varchar(20) NOT NULL, reg_date date, PRIMARY KEY (student_id),'
                     'FOREIGN KEY (course_enrolled) REFERENCES course (course_name),'
                     'FOREIGN KEY (batch) REFERENCES batch (batch_name),'
                     'CONSTRAINT UC_username UNIQUE (username,email));')
                self.db_connection.create(obj_create_database.get_database())

                obj_create_database = Model_class.connect_database.CreateDatabase \
                    ('create table employees(employee_id int NOT NULL AUTO_INCREMENT,'
                     'username varchar(254) NOT NULL, email varchar(50) NOT NULL,'
                     'password varchar(254) NOT NULL,f_name varchar(50) NOT NULL,'
                     'l_name varchar(50), dob varchar(20),gender varchar(10),'
                     'address varchar(30), contact_no int(13) NOT NULL,job_type varchar(20) NOT NULL,'
                     'registered_as varchar(50) NOT NULL,qualification varchar(50) NOT NULL,'
                     'department varchar(20) NOT NULL, reg_date date, PRIMARY KEY (employee_id),'
                     'FOREIGN KEY (department) REFERENCES department (department_name),'
                     'CONSTRAINT UC_username UNIQUE (username,email));')
                self.db_connection.create(obj_create_database.get_database())

                messagebox.showinfo("Success", "All Table are created successfully")

            except BaseException as msg:
                print(msg)
                messagebox.showerror("Error", "Database Table Creation Failed")
                return

            ask = messagebox.askokcancel("Setup Admin", "Please Setup First time Admin Login?\n "
                                                        "It will take just few seconds to get ready")
            if ask is True:
                win = Toplevel()
                Frontend.database_connected.DatabaseConnected(win)
                self.window.withdraw()
                win.deiconify()

        except BaseException as msg:

            messagebox.showerror("Error", f"Invalid Database Credentials\n {msg}")
            return

    def click_login(self):
        """when clicked login
        :returns new window of login page"""

        win = Toplevel()
        Frontend.login_form.Login(win)
        self.window.withdraw()
        win.deiconify()

    def click_exit(self):
        """when clicked exit button
        :return self.widow.quit() """
        ask = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to Exit\n Student Registration Form?")
        if ask is True:
            self.window.quit()

    def click_wipe(self):
        try:
            ask = messagebox.askyesnocancel("Confirm Wipe",
                                            "Are you sure you want to Wipe Database?\n All your Saved data will be "
                                            "lost.\n "
                                            "if chosen Yes!")
            if ask is True:
                obj_create_database = Model_class.connect_database.CreateDatabase('use cms;')
                self.db_connection.create(obj_create_database.get_database())

                obj_create_database = Model_class.connect_database.CreateDatabase \
                    ('drop database cms;')
                self.db_connection.create(obj_create_database.get_database())
                messagebox.showinfo("Success", "Database CMS Wiped out Successfully")
        except:
            messagebox.showerror("Error", "Database not found \n Please Connect database first")


class SaveDatabaseHost(Backend.connection.DatabaseConnection):
    """ inherits DatabaseConnection class from backend and extend the functionality
    by fetching the data from .txt file and set those data to current host for making
    connection with database."""
    def __init__(self):

        super().__init__()
        self.file()

    def file(self):
        self.len = os.path.getsize("D:\\Softwarica study material\\Semester 2\\Introduction to Algorithm\\Coding_and_"
                                   "Algorithms\\190352_Bibekanand_kushwaha_Sem_2_Final_assignment\\Frontend\\"
                                   "database_data.txt")
        if self.len > 0:
            f = open("D:\\Softwarica study material\\Semester 2\\Introduction to Algorithm\\Coding_and_"
                     "Algorithms\\190352_Bibekanand_kushwaha_Sem_2_Final_assignment\\Frontend\\"
                     "database_data.txt", "rb")
            self.dictcred = pickle.load(f)

            for k, p in self.dictcred.items():
                l = p[0]
                po = p[1]
                u = p[2]
                pa = p[3]
                self.d_connection(l, po, u, pa)


def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    ConnectDatabase(window)
    window.mainloop()


if __name__ == '__main__':
    win()
