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
import Model_class.student_registration
from tkinter import messagebox
import Frontend.connect_database
import Frontend.forgot_password
import Frontend.login_form
import Frontend.admin_dashboard
import Frontend.employee_registration
import Model_class.employee_registration
import Frontend.database_connected

import os


class ManageEmployee:
    """Allows Admin to manage employee; add, update, delete, fetch the data, here, admin can view all the details of
    employees and have various option to perform, they can search them by different functionality, such as employee_id,
    name, email, phone number and also they can search data such as id name and email from one date to another.
    searching can be performed even just by providing the character that the employees detail may contain and it will
    fetch all the data regarding that. this was done by using wild card feature of MySQL after grabbing all the data
    and then performing bubble sort on that and later sent to binary search method if data exists then all the data
    were inserted on the employee tree view. to make sorting possible, bubble sort method is used. also this method
    is used to sort the data in order to search."""
    list_of_tree = []
    get_id = []

    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x720+0+0")
        self.window.title("Manage Employee - College Management System")
        self.window.iconbitmap('images\\logo.ico')
        self.window.resizable(False, False)
        self.manage_student_frame = ImageTk.PhotoImage \
            (file='images\\student_frame.png')
        self.image_panel = Label(self.window, image=self.manage_student_frame)
        self.image_panel.pack(fill='both', expand='yes')

        self.db_connection = Backend.connection.DatabaseConnection()

        self.txt = "Employee Management Dashboard"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "#fa3939"]
        self.heading = Label(self.window, text=self.txt, font=('yu gothic ui', 30, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=420, y=26, width=640)
        self.slider()
        self.heading_color()

        # =======================================================================
        # ========================Defining Variables=============================
        # =======================================================================

        self.search_by_var = StringVar()
        self.sort_by_var = StringVar()
        self.sort_in_var = StringVar()
        self.sort_date_in_var = StringVar()

        # =======================================================================
        # ========================Left frame ====================================
        # =======================================================================

        left_view_frame = Frame(self.window, bg="white")
        left_view_frame.place(x=48, y=105, height=572, width=315)

        # =======================================================================
        # ========================Tree view frame================================
        # =======================================================================

        self.tree_view_frame = Frame(self.window, bg="white")
        self.tree_view_frame.place(x=388, y=140, height=535, width=930)

        # =======================================================================
        # ========================frame for personal credentials =================
        # =======================================================================

        personal_frame = LabelFrame(left_view_frame, text="Employee Management Options", bg="white", fg="#4f4e4d",
                                    height=465,
                                    width=303, borderwidth=2.4,
                                    font=("yu gothic ui", 13, "bold"))
        personal_frame.config(highlightbackground="red")
        personal_frame.place(x=5, y=45)

        # ========================================================================
        # ============================Add employee button===============================
        # ========================================================================

        self.add_admin = ImageTk.PhotoImage \
            (file='images\\add_admin.png')
        self.add_admin_button = Button(personal_frame, image=self.add_admin, relief=FLAT, borderwidth=0,
                                          activebackground="white", bg="white", cursor="hand2",
                                          command = self.click_add_admin)
        self.add_admin_button.place(x=8, y=60)

        # ========================================================================
        # ============================Add employee button===============================
        # ========================================================================

        self.add_employee = ImageTk.PhotoImage \
            (file='images\\add_employee.png')
        self.add_employee_button = Button(personal_frame, image=self.add_employee, relief=FLAT, borderwidth=0,
                                          activebackground="white", bg="white", cursor="hand2",
                                          command=self.click_add_employee)
        self.add_employee_button.place(x=8, y=125)
        # self.add_employee_button.place(x=36, y=295)

        # ========================================================================
        # ============================Update employee button===============================
        # ========================================================================

        self.update_employee = ImageTk.PhotoImage \
            (file='images\\update_employee.png')
        self.update_employee_button = Button(personal_frame, image=self.update_employee, relief=FLAT, borderwidth=0,
                                             activebackground="white", bg="white", cursor="hand2",
                                             command=self.tree_event_handle)
        self.update_employee_button.place(x=8, y=190)
        # self.update_employee_button.place(x=36, y=355)

        # ========================================================================
        # ============================Delete employee button===============================
        # ========================================================================

        self.delete_employee = ImageTk.PhotoImage \
            (file='images\\delete_employee.png')
        self.delete_employee_button = Button(personal_frame, image=self.delete_employee, relief=FLAT, borderwidth=0,
                                             activebackground="white", bg="white", cursor="hand2",
                                             command=self.click_delete_employee)
        self.delete_employee_button.place(x=8, y=255)
        # self.delete_employee_button.place(x=36, y=405)

        # ========================================================================
        # ============================Goto Main dashboard button===============================
        # ========================================================================

        self.goto_dashboard = ImageTk.PhotoImage \
            (file='images\\goto_dashboard.png')
        self.goto_dashboard_button = Button(personal_frame, image=self.goto_dashboard, relief=FLAT, borderwidth=0,
                                            activebackground="white", bg="white", cursor="hand2",
                                            command=self.click_go_to_dashboard)
        self.goto_dashboard_button.place(x=8, y=315)

        # =======================================================================
        # ========================Starting Tree View=============================
        # =======================================================================

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('yu gothic ui', 10, "bold"), foreground="red")

        scroll_x = Scrollbar(self.tree_view_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.tree_view_frame, orient=VERTICAL)
        self.employee_tree = ttk.Treeview(self.tree_view_frame,
                                         columns=(
                                             "EMPLOYEE ID", "FNAME", "LNAME", "EMAIL", "DOB", "GENDER", "ADDRESS",
                                             "CONTACT NO", "JOB TYPE", "DEPARTMENT", "QUALIFICATION", "REGISTERED AS",
                                             "REGISTRATION DATE"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.employee_tree.xview)
        scroll_y.config(command=self.employee_tree.yview)

        # ==========================TreeView Heading====================
        self.employee_tree.heading("EMPLOYEE ID", text="EMPLOYEE ID")
        self.employee_tree.heading("FNAME", text="FNAME")
        self.employee_tree.heading("LNAME", text="LNAME")
        self.employee_tree.heading("EMAIL", text="EMAIL")
        self.employee_tree.heading("DOB", text="DOB")
        self.employee_tree.heading("GENDER", text="GENDER")
        self.employee_tree.heading("ADDRESS", text="ADDRESS")
        self.employee_tree.heading("CONTACT NO", text="CONTACT NO")
        self.employee_tree.heading("JOB TYPE", text="JOB TYPE")
        self.employee_tree.heading("DEPARTMENT", text="DEPARTMENT")
        self.employee_tree.heading("QUALIFICATION", text="QUALIFICATION")
        self.employee_tree.heading("REGISTERED AS", text="REGISTERED AS")
        self.employee_tree.heading("REGISTRATION DATE", text="REGISTRATION DATE")
        self.employee_tree["show"] = "headings"

        # ==========================TreeView Column====================
        self.employee_tree.column("EMPLOYEE ID", width=150)
        self.employee_tree.column("FNAME", width=170)
        self.employee_tree.column("LNAME", width=170)
        self.employee_tree.column("EMAIL", width=200)
        self.employee_tree.column("ADDRESS", width=150)
        self.employee_tree.column("GENDER", width=150)
        self.employee_tree.column("CONTACT NO", width=150)
        self.employee_tree.column("DOB", width=150)
        self.employee_tree.column("JOB TYPE", width=150)
        self.employee_tree.column("DEPARTMENT", width=150)
        self.employee_tree.column("QUALIFICATION", width=150)
        self.employee_tree.column("REGISTERED AS", width=150)
        self.employee_tree.column("REGISTRATION DATE", width=150)
        self.employee_tree.pack(fill=BOTH, expand=1)
        # self.emp_tree.bind("<ButtonRelease-1>", self.getcredon_click)
        self.employee_tree.bind("<Button-3>", self.do_popup)
        self.employee_tree.bind("<Delete>", self.click_delete_key)
        self.employee_tree.bind("<Return>", self.tree_double_click)
        self.employee_tree.bind("<Double-Button-1>", self.tree_double_click)
        self.search_start()
        self.search_by.current(0)
        self.click_view_all()

    def click_view_all(self):
        """it will show all the data contains on the employee table of cms database, when clicked by default this method
        is called while initializing the class ManageEmployee. Exception is handled to avoid run time error which may
        cause by user."""
        try:
            obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_student_database.get_database())

            query = "select * from employees;"
            data = self.db_connection.select(query)
            # print(data)
            self.employee_tree.delete(*self.employee_tree.get_children())
            for values in data:
                data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
                             values[8],
                             values[9], values[10], values[13], values[12], values[11], values[14]]
                # print(data_list)
                self.employee_tree.insert('', END, values=data_list)

        except BaseException as msg:
            print(msg)

    def click_go_to_dashboard(self):
        """returns AdminDashboard class when clicked go to dashboard"""
        win = Toplevel()
        Frontend.admin_dashboard.AdminDashboard(win)
        self.window.withdraw()
        win.deiconify()

    def click_add_employee(self):
        """returns EmployeeRegisterForm class when clicked go to add employee button, where admin can add new employees
        to the database"""
        win = Toplevel()
        Frontend.employee_registration.EmployeeRegisterForm(win)
        Frontend.employee_registration.Clock(win)
        self.window.withdraw()
        win.deiconify()

    def click_add_admin(self):
        """Allows admin to add another admin by calling new window"""
        win = Toplevel()
        AddAdmin(win)
        self.window.withdraw()
        win.deiconify()

    def click_delete_key(self,events):
        """delete key of keyboard events is being handled here, and click_employee_student() methods is being called"""
        self.click_delete_employee()

    def click_delete_employee(self):
        """when clicked delete employees, it will require to select the employees and after selecting and
        performing the delete method, it will ask the admin either they are sure they want to delete that employee
        or not if yes then employee containing that id in employee table is deleted."""
        try:
            obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_student_database.get_database())

            tree_view_content = self.employee_tree.focus()
            tree_view_items = self.employee_tree.item(tree_view_content)
            tree_view_values = tree_view_items['values'][0]
            ask = messagebox.askyesno("Warning",
                                      f"Are you sure you want to delete employee having id {tree_view_values}")
            if ask is True:
                query = "delete from employees where employee_id=%s;"
                self.db_connection.delete(query, (tree_view_values,))
                messagebox.showinfo("Success", f" Employee id {tree_view_values} deleted Successfully")

                self.click_view_all()
            else:
                pass

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error",
                                 "There is some error deleting the data\n Make sure you have Selected the data")

    def tree_double_click(self, events):
        """Double click of mouse events is being handled here, and tree_event_handle() methods is being called"""
        self.tree_event_handle()

    def tree_event_handle(self):
        try:
            obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_student_database.get_database())

            tree_view_content = self.employee_tree.focus()
            tree_view_items = self.employee_tree.item(tree_view_content)
            # print(tree_view_items)
            tree_view_values = tree_view_items['values']
            tree_view_id = tree_view_items['values'][0]
            # print("tree",tree_view_id)
            ManageEmployee.get_id.clear()
            ManageEmployee.get_id.append(tree_view_id)
            ManageEmployee.list_of_tree.clear()
            # print("Appended", ManageEmployee.get_id)
            for i in tree_view_values:
                ManageEmployee.list_of_tree.append(i)

            # print(ManageEmployee.list_of_tree)
            # print(tree_view_values)

            ask = messagebox.askyesno("Confirm",
                                      f"Do you want to Update employee having id {tree_view_id}")
            if ask is True:
                self.click_update_employee()

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error",
                                 "There is some error updating the data\n Make sure you have Selected the data")

    def click_update_employee(self):
        """calls UpdateEmployeeForm class when clicked on update employee button"""
        win_ = Toplevel()
        UpdateEmployeeForm(win_)
        self.window.withdraw()
        win_.deiconify()

    def do_popup(self, event):
        """does popup menu when clicked right click on tree view, where there will be three option to choose from
        if chosen update it will call update method and similar to that for remaining menus"""
        popup = Menu(self.window, tearoff=0)
        popup.add_command(label="UPDATE", command=self.tree_event_handle)
        popup.add_separator()
        popup.add_command(label="DELETE", command=self.click_delete_employee)
        popup.add_separator()
        popup.add_command(label="FETCH", command=self.click_fetch_employee)

        try:
            popup.tk_popup(event.x_root, event.y_root, 0)
        finally:
            # make sure to release the grab (Tk 8.0a1 only)
            popup.grab_release()

    # def search_sort_combo(self, events):
    #     if self.search_sort.get() == "Search":
    #         self.search_start()
    #     else:
    #         self.sort_start()
    #         self.sort_by.current(0)
    #
    # def start_search_combo(self, events):
    #     # print("okay")
    #     if self.search_by.get() == "ID" or self.search_by.get() == "Name" or self.search_by.get() == "Email" \
    #             or self.search_by.get() == "Phone No." or self.search_by.get() == "Search by":
    #         self.search_start()
    #     else:
    #         self.search_date()


    def click_fetch_employee(self):
        """when chosen fetch employees from popup menu, this methods will be executed which will grab all the
        information of that employee into list and calls get_fetch_employee() methods when output is True"""
        try:
            obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_student_database.get_database())

            tree_view_content = self.employee_tree.focus()
            tree_view_items = self.employee_tree.item(tree_view_content)
            # print(tree_view_items)
            tree_view_values = tree_view_items['values']
            tree_view_id = tree_view_items['values'][0]
            ManageEmployee.list_of_tree.clear()
            for i in tree_view_values:
                ManageEmployee.list_of_tree.append(i)
            # print(ManageEmployee.list_of_tree)
            # print(tree_view_values)

            ask = messagebox.askyesno("Confirm",
                                      f"Do you want to Fetch Employee having id {tree_view_id}")
            if ask is True:
                self.get_fetch_employee()

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error",
                                 "There is some error fetching the data\n Make sure you have Selected the data")

    def get_fetch_employee(self):
        """calls FetchEmployeeForm class when clicked on fetch option of popup menu"""
        win_ = Toplevel()
        FetchEmployeeForm(win_)
        self.window.withdraw()
        win_.deiconify()

    # =======================================================================
    # ========================Searching Started==============================
    # =======================================================================
    @classmethod
    def binary_search(self, _list, target):
        """this is class method searching for user input into the table"""
        start = 0
        end = len(_list) - 1

        while start <= end:
            middle = (start + end) // 2
            midpoint = _list[middle]
            if midpoint > target:
                end = middle - 1
            elif midpoint < target:
                start = middle + 1
            else:
                return midpoint

    @classmethod
    def bubble_sort(self, list):
        """this class methods sort the string value of user input such as name"""
        # print("Success")
        for j in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i].upper() > list[i + 1].upper():
                    list[i], list[i + 1] = list[i + 1], list[i]
        # print('the sorted list is ', list)
        return list

    @classmethod
    def bubble_sort_integer(self, list):
        """this class methods sort the integer value of user input such as id and phone"""
        # print("Success")
        for j in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i] > list[i + 1]:
                    list[i], list[i + 1] = list[i + 1], list[i]
        # print('the sorted list is ', list)
        return list

    def search_by_id_start(self):
        """this method initialize the search by id feature from combobox of search_by attribute"""
        a = self.search_entry.get()
        if self.search_entry.get() != '':
            if a.isnumeric():
                try:
                    search_list = []
                    for child in self.employee_tree.get_children():
                        val = self.employee_tree.item(child)["values"][0]
                        search_list.append(val)

                    # print(search_list)

                    output = self.binary_search(search_list, int(self.search_entry.get()))
                    # print(output)
                    if output:
                        messagebox.showinfo("Found", f"employee having id {output} found")

                        obj_employee_database = Model_class.employee_registration.GetDatabase('use cms;')
                        self.db_connection.create(obj_employee_database.get_database())

                        query = "select * from employees where employee_id=%s;"
                        # print(output)
                        data = self.db_connection.search(query, (output,))
                        # print(data)
                        # self.employee_tree.delete(*self.employee_tree.get_children())

                        for values in data:
                            data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
                                         values[8],
                                         values[9], values[10], values[11], values[12], values[13], values[14]]

                            self.employee_tree.delete(*self.employee_tree.get_children())
                            self.employee_tree.insert('', END, values=data_list)

                    else:
                        messagebox.showerror("Error", " ID Not found")

                except BaseException as msg:
                    print(msg)

            else:
                messagebox.showerror("Error", "Please Search Integer value")
        else:
            messagebox.showerror("Blank", "Search field can not be Empty")

    def search_by_name_start(self):
        """this method initialize the search by name feature from combobox of search_by attribute"""
        a = self.search_entry.get()
        if self.search_entry.get() != '':
            if a.isalpha():
                try:
                    search_list = []
                    for child in self.employee_tree.get_children():
                        val = self.employee_tree.item(child)["values"][1]
                        search_list.append(val)
                    # print(search_list)

                    sorted_list = self.bubble_sort(search_list)

                    self.output = self.binary_search(sorted_list, self.search_entry.get())
                    # print(output)
                    if self.output:
                        messagebox.showinfo("Found", f"employee having Name '{self.output}' found")

                        obj_employee_database = Model_class.employee_registration.GetDatabase('use cms;')
                        self.db_connection.create(obj_employee_database.get_database())

                        query = "select * from employees where f_name LIKE '" + str(self.output) + "%'"
                        # print(output)
                        data = self.db_connection.select(query)
                        # print(data)
                        self.employee_tree.delete(*self.employee_tree.get_children())

                        for values in data:
                            data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
                                         values[8],
                                         values[9], values[10], values[11], values[12], values[13], values[14]]

                            # self.employee_tree.delete(*self.employee_tree.get_children())
                            self.employee_tree.insert('', END, values=data_list)

                    else:
                        messagebox.showerror("Error", " Name Not found\n Relevant Name are Extracted")

                        obj_employee_database = Model_class.employee_registration.GetDatabase('use cms;')
                        self.db_connection.create(obj_employee_database.get_database())

                        query = "select * from employees where f_name LIKE '%" + str(self.search_entry.get()) + "%'"
                        # print(output)
                        data = self.db_connection.select(query)
                        # print(data)
                        self.employee_tree.delete(*self.employee_tree.get_children())

                        for values in data:
                            data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
                                         values[8],
                                         values[9], values[10], values[11], values[12], values[13], values[14]]

                            # self.employee_tree.delete(*self.employee_tree.get_children())
                            self.employee_tree.insert('', END, values=data_list)

                except BaseException as msg:
                    print(msg)

            else:
                messagebox.showerror("Error", "Please Search value")
        else:
            messagebox.showerror("Blank", "Search field can not be Empty")

    def search_by_email_start(self):
        """this method initialize the search by email feature from combobox of search_by attribute"""
        a = self.search_entry.get()
        if self.search_entry.get() != '':
            if True:
                try:
                    search_list = []
                    for child in self.employee_tree.get_children():
                        val = self.employee_tree.item(child)["values"][3]
                        search_list.append(val)
                    # print(search_list)

                    sorted_list = self.bubble_sort(search_list)

                    self.output = self.binary_search(sorted_list, self.search_entry.get())
                    # print(output)
                    if self.output:
                        messagebox.showinfo("Found", f"employee having Email '{self.output}' found")

                        obj_employee_database = Model_class.employee_registration.GetDatabase('use cms;')
                        self.db_connection.create(obj_employee_database.get_database())

                        query = "select * from employees where email LIKE '" + str(self.output) + "%'"
                        # print(output)
                        data = self.db_connection.select(query)
                        # print(data)
                        self.employee_tree.delete(*self.employee_tree.get_children())

                        for values in data:
                            data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
                                         values[8],
                                         values[9], values[10], values[11], values[12], values[13], values[14]]

                            # self.employee_tree.delete(*self.employee_tree.get_children())
                            self.employee_tree.insert('', END, values=data_list)

                    else:
                        messagebox.showerror("Error", " Email Not found\n Relevant Email are Extracted")

                        obj_employee_database = Model_class.employee_registration.GetDatabase('use cms;')
                        self.db_connection.create(obj_employee_database.get_database())

                        query = "select * from employees where email LIKE '%" + str(self.search_entry.get()) + "%'"
                        # print(output)
                        data = self.db_connection.select(query)
                        # print(data)
                        self.employee_tree.delete(*self.employee_tree.get_children())

                        for values in data:
                            data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
                                         values[8],
                                         values[9], values[10], values[11], values[12], values[13], values[14]]

                            # self.employee_tree.delete(*self.employee_tree.get_children())
                            self.employee_tree.insert('', END, values=data_list)

                except BaseException as msg:
                    print(msg)
        else:
            messagebox.showerror("Blank", "Search field can not be Empty")

    def search_by_phone_start(self):
        """this method initialize the search by phone number feature from combobox of search_by attribute"""
        a = self.search_entry.get()
        if self.search_entry.get() != '':
            if a.isnumeric():
                try:
                    search_list = []
                    for child in self.employee_tree.get_children():
                        val = self.employee_tree.item(child)["values"][7]
                        search_list.append(val)
                    # print(search_list)

                    sorted_list = self.bubble_sort_integer(search_list)

                    self.output = self.binary_search(sorted_list, int(self.search_entry.get()))
                    # print(output)
                    if self.output:
                        messagebox.showinfo("Found", f"employee having phone '{self.output}' found")

                        obj_employee_database = Model_class.employee_registration.GetDatabase('use cms;')
                        self.db_connection.create(obj_employee_database.get_database())

                        query = "select * from employees where contact_no LIKE '" + str(self.output) + "%'"
                        # print(output)
                        data = self.db_connection.select(query)
                        # print(data)
                        self.employee_tree.delete(*self.employee_tree.get_children())

                        for values in data:
                            data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
                                         values[8],
                                         values[9], values[10], values[11], values[12], values[13], values[14]]

                            # self.employee_tree.delete(*self.employee_tree.get_children())
                            self.employee_tree.insert('', END, values=data_list)

                    else:
                        messagebox.showerror("Error", " Phone Number Not found\n Relevant Phone Number are Extracted")

                        obj_employee_database = Model_class.employee_registration.GetDatabase('use cms;')
                        self.db_connection.create(obj_employee_database.get_database())

                        query = "select * from employees where contact_no LIKE '%" + str(self.search_entry.get()) + "%'"
                        # print(output)
                        data = self.db_connection.select(query)
                        # print(data)
                        self.employee_tree.delete(*self.employee_tree.get_children())

                        for values in data:
                            data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
                                         values[8],
                                         values[9], values[10], values[11], values[12], values[13], values[14]]

                            # self.employee_tree.delete(*self.employee_tree.get_children())
                            self.employee_tree.insert('', END, values=data_list)

                except BaseException as msg:
                    print(msg)

            else:
                messagebox.showerror("Error", "Please Search value")
        else:
            messagebox.showerror("Blank", "Search field can not be Empty")

    def search_by_date_start(self):
        """this method initialize the search by date feature from combobox of search_by attribute"""
        # print("pass")
        a = self.search_in_date_entry.get()
        print(a)
        if self.search_in_date_entry.get() != '':
            if True:
                try:
                    obj_employee_database = Model_class.employee_registration.GetDatabase('use cms;')
                    self.db_connection.create(obj_employee_database.get_database())

                    query = "select * from employees where f_name LIKE '%" + str(
                        self.search_in_date_entry.get()) + "%'  AND reg_date between %s and %s OR email LIKE '%" + str(
                        self.search_in_date_entry.get()) + "%' AND reg_date between %s and %s"

                    # query = "select * from employees where f_name LIKE '%" + str(self.search_in_date_entry.get()) + "%' AND reg_date between %s and %s"
                    # query = "select * from employees where reg_date between %s and %s"
                    # query = "select * from employees where f_name LIKE '%" + str(self.search_entry.get()) + "%' and reg_date between %s and %s"
                    # print(output)
                    data = self.db_connection.search(query,
                                                     (self.search_fdate_entry.get(), self.search_tdate_entry.get(),
                                                      self.search_fdate_entry.get(), self.search_tdate_entry.get()))
                    print(data)
                    if data:
                        self.employee_tree.delete(*self.employee_tree.get_children())

                        for values in data:
                            data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
                                         values[8],
                                         values[9], values[10], values[11], values[12], values[13], values[14]]

                            # self.employee_tree.delete(*self.employee_tree.get_children())
                            self.employee_tree.insert('', END, values=data_list)

                    else:
                        messagebox.showerror("Not found", "No data were found")


                except BaseException as msg:
                    print(msg)
        else:
            messagebox.showerror("Blank", "Search field can not be Empty")

    def search_sort_combo(self, events):
        """handles selected events of combobox for search attribute"""
        if self.search_sort.get() == "Search":
            self.search_start()
        else:
            self.sort_start()
            self.sort_by.current(0)
            messagebox.showinfo("Notification", "By default Data is Sorted in Ascending Order By ID")

    def start_search_combo(self, events):
        """it validates the search combobox and start calling methods with the desire"""
        if self.search_by.get() == "Search by":
            self.search_start()
            self.search_button.configure(command=self.search_by_id_start)

        if self.search_by.get() == "ID":
            self.search_start()
            self.search_button.configure(command=self.search_by_id_start)

        if self.search_by.get() == "Name":
            self.search_start()
            self.search_button.configure(command=self.search_by_name_start)

        if self.search_by.get() == "Email":
            self.search_start()
            self.search_button.configure(command=self.search_by_email_start)

        if self.search_by.get() == "Phone No.":
            self.search_start()
            self.search_button.configure(command=self.search_by_phone_start)

        if self.search_by.get() == "Date":
            self.search_date()
            self.search_date_button.configure(command=self.search_by_date_start)

        # ======================================================================
        # =====================================searching END====================
        # ======================================================================

    def search_start(self):
        """here search frame, label, combobox are written which is shown while admin views employee dashboard"""
        # =======================================================================
        # ========================search tree view frame================================
        # =======================================================================

        self.search_view_frame = Frame(self.window, bg="white")
        self.search_view_frame.place(x=388, y=105, height=35, width=930)

        # =======================================================================
        # ========================Starting Search and Sort=======================
        # =======================================================================
        self.search_img = ImageTk.PhotoImage \
            (file='images\\search.png')
        self.search_button = Button(self.search_view_frame, image=self.search_img, relief=FLAT, borderwidth=0,
                                    activebackground="white", bg="white", cursor="hand2")
        self.search_button.place(x=765, y=5)

        self.view_all_img = ImageTk.PhotoImage \
            (file='images\\view_all.png')
        self.view_all_button = Button(self.search_view_frame, image=self.view_all_img, relief=FLAT, borderwidth=0,
                                      activebackground="white", bg="white", cursor="hand2", command=self.click_view_all)
        self.view_all_button.place(x=845, y=5)

        # =======================================================================
        # ========================search and sort combo=======================
        # =======================================================================

        style = ttk.Style()
        self.window.option_add("*TCombobox*Listbox*Foreground", '#fa3939')

        self.search_sort = ttk.Combobox(self.search_view_frame, font=('yu gothic ui semibold', 12, 'bold'),
                                        state='readonly',
                                        width=10)
        self.search_sort['values'] = ('Search', 'Sort')
        self.search_sort.current(0)
        self.search_sort.place(x=15, y=3)
        self.search_sort.bind('<<ComboboxSelected>>', self.search_sort_combo)

        # =======================================================================
        # ========================search and sort combo=======================
        # =======================================================================

        self.search_by = ttk.Combobox(self.search_view_frame, font=('yu gothic ui semibold', 12, 'bold'),
                                      state='readonly',
                                      width=10, textvariable=self.search_by_var)
        self.search_by['values'] = ('Search by', 'ID', 'Name', 'Email', 'Phone No.', 'Date')
        self.search_by.place(x=145, y=3)
        # self.search_by.current(0)
        self.search_by.bind('<<ComboboxSelected>>', self.start_search_combo)

        self.search_start_frame = Frame(self.window, bg="white")
        self.search_start_frame.place(x=652, y=105, height=35, width=503)
        # =======================================================================
        # ========================Entry for search=======================
        # =======================================================================

        self.search_entry = Entry(self.search_start_frame, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                  font=("yu gothic ui semibold", 12))
        self.search_txt = "Search here.........."
        self.search_entry.insert(0, self.search_txt)
        self.search_entry.place(x=10, y=3, width=480)  # trebuchet ms
        self.search_entry.bind("<1>", self.clear_search)

        self.search_line = Canvas(self.search_start_frame, width=480, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.search_line.place(x=10, y=26)

    def search_date(self):
        """here search date frame, label, calender events are written which is shown while admin view employee
        dashboard"""
        self.search_date_frame = Frame(self.window, bg="white")
        self.search_date_frame.place(x=652, y=105, height=35, width=583)

        self.search_date_img = ImageTk.PhotoImage \
            (file='images\\search.png')
        self.search_date_button = Button(self.search_date_frame, image=self.search_date_img, relief=FLAT, borderwidth=0,
                                         activebackground="white", bg="white", cursor="hand2")
        self.search_date_button.place(x=501, y=5)

        # =======================================================================
        # ========================Entry for from  Date=======================
        # =======================================================================

        self.search_fdate_entry = Entry(self.search_date_frame, highlightthickness=0, relief=FLAT, bg="white",
                                        fg="#6b6a69",
                                        font=("yu gothic ui semibold", 12))

        self.search_fdate_txt = "From..."
        self.search_fdate_entry.insert(0, self.search_fdate_txt)
        self.search_fdate_entry.place(x=10, y=3, width=100)  # trebuchet ms
        # self.search_fdate_entry.bind("<1>", self.clear_fdate)
        self.search_fdate_entry.bind("<1>", self.pick_date)

        self.search_fdate_line = Canvas(self.search_date_frame, width=100, height=1.5, bg="#bdb9b1",
                                        highlightthickness=0)
        self.search_fdate_line.place(x=10, y=26)

        # =======================================================================
        # ========================Entry for till Date=======================
        # =======================================================================

        self.search_tdate_entry = Entry(self.search_date_frame, highlightthickness=0, relief=FLAT, bg="white",
                                        fg="#6b6a69",
                                        font=("yu gothic ui semibold", 12))

        self.search_tdate_txt = "To..."
        self.search_tdate_entry.insert(0, self.search_tdate_txt)
        self.search_tdate_entry.place(x=125, y=3, width=100)  # trebuchet ms
        # self.search_tdate_entry.bind("<1>", self.clear_tdate)
        self.search_tdate_entry.bind("<1>", self.t_pick_date)

        self.search_tdate_line = Canvas(self.search_date_frame, width=100, height=1.5, bg="#bdb9b1",
                                        highlightthickness=0)
        self.search_tdate_line.place(x=125, y=26)

        # =======================================================================
        # ========================Entry for search in Date=======================
        # =======================================================================

        self.search_in_date_entry = Entry(self.search_date_frame, highlightthickness=0, relief=FLAT, bg="white",
                                          fg="#6b6a69",
                                          font=("yu gothic ui semibold", 12))

        self.search_in_date_txt = "Search here..."
        self.search_in_date_entry.insert(0, self.search_in_date_txt)
        self.search_in_date_entry.place(x=240, y=3, width=250)  # trebuchet ms
        self.search_in_date_entry.bind("<1>", self.clear_sindate)

        self.search_in_date_line = Canvas(self.search_date_frame, width=250, height=1.5, bg="#bdb9b1",
                                          highlightthickness=0)
        self.search_in_date_line.place(x=240, y=26)

    def pick_date(self, event):
        """handles the calender events, and pick those data for entry fields"""
        self.search_fdate_entry.delete(0, END)
        self.date_win = tk.ThemedTk()
        self.date_win.get_themes()
        self.date_win.set_theme("arc")
        self.date_win.grab_set()
        self.date_win.title('Choose Date of Birth')
        self.date_win.geometry('250x220+590+170')
        self.cal = Calendar(self.date_win, selectmode="day", date_pattern="y/mm/dd")
        self.cal.place(x=0, y=0)

        self.okay_btn = ttk.Button(self.date_win, text="Okay", command=self.grab_date)
        self.okay_btn.place(x=80, y=180)

    def grab_date(self):
        """this grabs the date which was picked by pick_date() method"""
        self.search_fdate_entry.delete(0, END)
        self.search_fdate_entry.config(fg="#6b6a69")
        self.search_fdate_entry.insert(0, self.cal.get_date())
        self.date_win.destroy()

    def t_pick_date(self, event):
        """handles the calender events for to date, and pick those data for entry fields"""
        self.search_tdate_entry.delete(0, END)
        self.t_date_win = tk.ThemedTk()
        self.t_date_win.get_themes()
        self.t_date_win.set_theme("arc")
        self.t_date_win.grab_set()
        self.t_date_win.title('Choose Date of Birth')
        self.t_date_win.geometry('250x220+710+170')
        self.t_cal = Calendar(self.t_date_win, selectmode="day", date_pattern="y/mm/dd")
        self.t_cal.place(x=0, y=0)

        self.t_okay_btn = ttk.Button(self.t_date_win, text="Okay", command=self.t_grab_date)
        self.t_okay_btn.place(x=80, y=180)

    def t_grab_date(self):
        """this grabs the date which was picked by t_pick_date() method"""
        self.search_tdate_entry.delete(0, END)
        self.search_tdate_entry.config(fg="#6b6a69")
        self.search_tdate_entry.insert(0, self.t_cal.get_date())
        self.t_date_win.destroy()

    def sort_start(self):
        """codes for sorting starts here, all the frame, combobox, lable, entry and button in order to
        sort any data will be found here."""
        self.sort_start_frame = Frame(self.window, bg="white")
        self.sort_start_frame.place(x=534, y=105, height=35, width=701)

        # =======================================================================
        # ========================Sort by combobox=======================
        # =======================================================================

        self.sort_by = ttk.Combobox(self.sort_start_frame, font=('yu gothic ui semibold', 12, 'bold'),
                                    state='readonly',
                                    width=15, textvariable=self.sort_by_var)
        self.sort_by['values'] = ('Sort by', 'ID', 'Name', 'Email', 'Phone No.', 'Registration Date')
        self.sort_by.place(x=0, y=3)
        # self.sort_by.current(0)
        self.sort_by.bind('<<ComboboxSelected>>', self.sort_by_start)

        # =======================================================================
        # ========================Sort Form combobox=======================
        # =======================================================================

        self.sort_in = ttk.Combobox(self.sort_start_frame, font=('yu gothic ui semibold', 12, 'bold'),
                                    state='readonly',
                                    width=45, textvariable=self.sort_in_var)
        self.sort_in['values'] = ('Ascending Order', 'Descending Order')
        self.sort_in.place(x=175, y=3)
        self.sort_in.current(0)
        self.sort_in.bind('<<ComboboxSelected>>', self.sort_by_start)
        # self.sort_in.bind('<<ComboboxSelected>>', self.start_sort_combo)

        self.sort_img = ImageTk.PhotoImage \
            (file='images\\sort.png')
        self.sort_button = Button(self.sort_start_frame, image=self.sort_img, relief=FLAT, borderwidth=0,
                                  activebackground="white", bg="white", cursor="hand2")
        self.sort_button.place(x=619, y=5)

    def start_sort_combo(self, events):
        """handles the sort by comobobox events of sort_by attribute and calls methods when validation is filled"""
        if self.sort_by.get() == "Sort by" or self.sort_by.get() == "ID" or self.sort_by.get() == "Name" or \
                self.sort_by.get() == "Email" or self.sort_by.get() == "Phone No.":
            self.sort_start()

        else:
            self.sort_date()

    def sort_date(self):
        """in order to sort the data by date, all the frames, button, events are being handled here, exception are
        also handeled in order to avoid the run time error that user may cause"""
        self.sort_date_frame = Frame(self.window, bg="white")
        self.sort_date_frame.place(x=696, y=105, height=35, width=539)

        self.sort_date_img = ImageTk.PhotoImage \
            (file='images\\sort.png')
        self.sort_date_button = Button(self.sort_date_frame, image=self.sort_date_img, relief=FLAT, borderwidth=0,
                                       activebackground="white", bg="white", cursor="hand2")
        self.sort_date_button.place(x=457, y=5)

        # =======================================================================
        # ========================Sort method combobox=======================
        # =======================================================================

        self.sort_date_in = ttk.Combobox(self.sort_date_frame, font=('yu gothic ui semibold', 12, 'bold'),
                                         state='readonly',
                                         width=19, textvariable=self.sort_date_in_var)
        self.sort_date_in['values'] = ('Recent Registration',
                                       'Oldest Registration')
        self.sort_date_in.place(x=245, y=3)

        self.sort_date_in.current(0)

        # =======================================================================
        # ========================Entry for from  Date=======================
        # =======================================================================

        self.sort_fdate_entry = Entry(self.sort_date_frame, highlightthickness=0, relief=FLAT, bg="white",
                                      fg="#6b6a69",
                                      font=("yu gothic ui semibold", 12))

        self.sort_fdate_txt = "From..."
        self.sort_fdate_entry.insert(0, self.sort_fdate_txt)
        self.sort_fdate_entry.place(x=15, y=3, width=100)  # trebuchet ms
        # self.search_fdate_entry.bind("<1>", self.clear_fdate)
        self.sort_fdate_entry.bind("<1>", self.s_f_pick_date)

        self.sort_fdate_line = Canvas(self.sort_date_frame, width=100, height=1.5, bg="#bdb9b1",
                                      highlightthickness=0)
        self.sort_fdate_line.place(x=15, y=26)

        # =======================================================================
        # ========================Entry for till Date=======================
        # =======================================================================

        self.sort_tdate_entry = Entry(self.sort_date_frame, highlightthickness=0, relief=FLAT, bg="white",
                                      fg="#6b6a69",
                                      font=("yu gothic ui semibold", 12))

        self.sort_tdate_txt = "To..."
        self.sort_tdate_entry.insert(0, self.sort_tdate_txt)
        self.sort_tdate_entry.place(x=130, y=3, width=100)  # trebuchet ms
        # self.search_tdate_entry.bind("<1>", self.clear_tdate)
        self.sort_tdate_entry.bind("<1>", self.s_t_pick_date)

        self.sort_tdate_line = Canvas(self.sort_date_frame, width=100, height=1.5, bg="#bdb9b1",
                                      highlightthickness=0)
        self.sort_tdate_line.place(x=130, y=26)

    def s_f_pick_date(self, event):
        """this method handles the events for from date calendar for sorting for from date"""
        self.sort_fdate_entry.delete(0, END)
        self.s_f_date_win = tk.ThemedTk()
        self.s_f_date_win.get_themes()
        self.s_f_date_win.set_theme("arc")
        self.s_f_date_win.grab_set()
        self.s_f_date_win.title('Choose Date of Birth')
        self.s_f_date_win.geometry('250x220+590+170')
        self.s_f_cal = Calendar(self.s_f_date_win, selectmode="day", date_pattern="mm/dd/y")
        self.s_f_cal.place(x=0, y=0)

        self.s_f_okay_btn = ttk.Button(self.s_f_date_win, text="Okay", command=self.s_f_grab_date)
        self.s_f_okay_btn.place(x=80, y=180)

    def s_f_grab_date(self):
        """grabs the date that s_f_pick_date() picks the data from calendar"""
        self.sort_fdate_entry.delete(0, END)
        self.sort_fdate_entry.config(fg="#6b6a69")
        self.sort_fdate_entry.insert(0, self.s_f_cal.get_date())
        self.s_f_date_win.destroy()

    def s_t_pick_date(self, event):
        """this method handles the events for to date calendar for sorting for from date"""
        self.sort_tdate_entry.delete(0, END)
        self.s_t_date_win = tk.ThemedTk()
        self.s_t_date_win.get_themes()
        self.s_t_date_win.set_theme("arc")
        self.s_t_date_win.grab_set()
        self.s_t_date_win.title('Choose Date of Birth')
        self.s_t_date_win.geometry('250x220+710+170')
        self.s_t_cal = Calendar(self.s_t_date_win, selectmode="day", date_pattern="mm/dd/y")
        self.s_t_cal.place(x=0, y=0)

        self.s_t_okay_btn = ttk.Button(self.s_t_date_win, text="Okay", command=self.s_t_grab_date)
        self.s_t_okay_btn.place(x=80, y=180)

    def s_t_grab_date(self):
        """grabs the date that s_t_pick_date() picks the data from calendar"""
        self.sort_tdate_entry.delete(0, END)
        self.sort_tdate_entry.config(fg="#6b6a69")
        self.sort_tdate_entry.insert(0, self.s_t_cal.get_date())
        self.s_t_date_win.destroy()


        # =======================================================================
        # ========================Sorting started================================
        # =======================================================================

    def sort_by_start(self,events):
        """events for combobox in order to sort the data starts here"""
        if self.sort_by.get() == "Sort by":
            self.sort_button.configure(command=self.sort_by_id_ascending)
            self.sort_by_id_ascending()

        if self.sort_by.get() == "ID" and self.sort_in.get() == "Ascending Order":
            self.sort_button.configure(command=self.sort_by_id_ascending)
            self.sort_by_id_ascending()

        if self.sort_by.get() == "ID" and self.sort_in.get() == "Descending Order":
            self.sort_button.configure(command=self.sort_by_id_descending)
            self.sort_by_id_descending()

        if self.sort_by.get() == "Name" and self.sort_in.get() == "Ascending Order":
            self.sort_button.configure(command=self.sort_by_name_ascending)
            self.sort_by_name_ascending()

        if self.sort_by.get() == "Name" and self.sort_in.get() == "Descending Order":
            self.sort_button.configure(command=self.sort_by_name_descending)
            self.sort_by_name_descending()

        if self.sort_by.get() == "Email" and self.sort_in.get() == "Ascending Order":
            self.sort_button.configure(command=self.sort_by_email_ascending)
            self.sort_by_email_ascending()

        if self.sort_by.get() == "Email" and self.sort_in.get() == "Descending Order":
            self.sort_button.configure(command=self.sort_by_email_descending)
            self.sort_by_email_descending()

        if self.sort_by.get() == "Phone No." and self.sort_in.get() == "Ascending Order":
            self.sort_button.configure(command=self.sort_by_phone_ascending)
            self.sort_by_phone_ascending()

        if self.sort_by.get() == "Phone No." and self.sort_in.get() == "Descending Order":
            self.sort_button.configure(command=self.sort_by_phone_descending)
            self.sort_by_phone_descending()

        if self.sort_by.get() == "Registration Date" and self.sort_in.get() == "Ascending Order":
            self.sort_button.configure(command=self.sort_by_registration_ascending)
            self.sort_by_registration_ascending()

        if self.sort_by.get() == "Registration Date" and self.sort_in.get() == "Descending Order":
            self.sort_button.configure(command=self.sort_by_registration_descending)
            self.sort_by_registration_descending()

    def sort_by_id_ascending(self):
        """this will sort the id in ascending order, here data is extracted from database and then
        all the data containing id are sent to bubble_sort_ascending() methods to sort that data and
        lastly those data are again inserted into table in sorted form"""
        query = "select * from employees;"
        data = self.db_connection.select(query)
        sort_list = []
        for values in data:
            sort_list.append(values)
        # print(sort_list)
        sorted_list= self.bubble_sort_ascending(sort_list)
        # messagebox.showinfo("Sorted", "Data is sorted in Ascending order by ID")
        if len(sorted_list) != 0:
            self.employee_tree.delete(*self.employee_tree.get_children())
            for values in sorted_list:
                data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
                             values[8],
                             values[9], values[10], values[11], values[12], values[13], values[14]]
                self.employee_tree.insert('', END, values=data_list)

    def bubble_sort_ascending(self,list):
        """this will sort the data by using bubble sort method while performing sort data"""
        for j in range(len(list)-1):
            for i in range(len(list)-1):
                if list[i] > list[i+1]:
                    list[i], list[i+1] = list[i+1], list[i]
        print('the sorted list is ',list)
        return list

    def sort_by_id_descending(self):
        """ this will sort the id in descending order, here data is extracted from database and then
        all the data containing id are sent to bubble_sort_descending() methods to sort that data and
        lastly those data are again inserted into table in sorted form"""
        query = "select * from employees;"
        data = self.db_connection.select(query)
        sort_list = []
        for values in data:
            sort_list.append(values)
        # print(sort_list)
        sorted_list= self.bubble_sort_descending(sort_list)
        # messagebox.showinfo("Sorted", "Data is Sorted in Descending order By ID")
        if len(sorted_list) != 0:
            self.employee_tree.delete(*self.employee_tree.get_children())
            for values in sorted_list:
                data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
                             values[8],
                             values[9], values[10], values[11], values[12], values[13], values[14]]
                self.employee_tree.insert('', END, values=data_list)

    def bubble_sort_descending(self,list):
        """this will sort the data by using bubble sort method while performing sort data"""
        for j in range(len(list)-1):
            for i in range(len(list)-1):
                if list[i] < list[i+1]:
                    list[i], list[i+1] = list[i+1], list[i]
        print('the sorted list is ',list)
        return list

    def sort_by_name_ascending(self):
        """this will sort name in ascending order, here data is extracted from database and then
        all the data containing id are sent to bubble_sort_ascending() methods to sort that data and
        lastly those data are again inserted into table in sorted form"""
        # print("I am in sort by name in ascending order")
        query = "select * from employees;"
        data = self.db_connection.select(query)
        print(data)
        sort_list = []
        for values in data:
            sort_list.append(values)
        # print(sort_list[0])
        sorted_list = self.bubble_name_ascending(sort_list)
        # messagebox.showinfo("Sorted", "Data is Sorted in Descending order By Name")
        if len(sorted_list) != 0:
            self.employee_tree.delete(*self.employee_tree.get_children())
            for values in sorted_list:
                data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
                             values[8],
                             values[9], values[10], values[11], values[12], values[13], values[14]]
                self.employee_tree.insert('', END, values=data_list)

    def sort_by_name_descending(self):
        """this will sort the name in descending order, here data is extracted from database and then
        all the data containing id are sent to bubble_sort_descending() methods to sort that data and
        lastly those data are again inserted into table in sorted form"""
        # print("i am in sort by name in descending order")
        query = "select * from employees;"
        data = self.db_connection.select(query)
        print(data)
        sort_list = []
        for values in data:
            sort_list.append(values)
        # print(sort_list[0])
        sorted_list = self.bubble_name_descending(sort_list)
        # messagebox.showinfo("Sorted", "Data is Sorted in Descending order By Name")
        if len(sorted_list) != 0:
            self.employee_tree.delete(*self.employee_tree.get_children())
            for values in sorted_list:
                data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
                             values[8],
                             values[9], values[10], values[11], values[12], values[13], values[14]]
                self.employee_tree.insert('', END, values=data_list)


    def bubble_name_ascending(self,list):
        """this will sort the data by using bubble sort method while performing sort data"""
        print("Success")
        for j in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i][4].upper() > list[i + 1][4].upper():
                    list[i], list[i + 1] = list[i + 1], list[i]
        print('the sorted list is ', list)
        return list

    def bubble_name_descending(self,list):
        """this will sort the data by using bubble sort method while performing sort data"""
        print("Success")
        for j in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i][4].upper() < list[i + 1][4].upper():
                    list[i], list[i + 1] = list[i + 1], list[i]
        print('the sorted list is ', list)
        return list

    def sort_by_email_ascending(self):
        """this will sort the email in ascending order, here data is extracted from database and then
        all the data containing id are sent to bubble_sort_ascending() methods to sort that data and
        lastly those data are again inserted into table in sorted form"""
        # print("I am in sort by name in ascending order")
        query = "select * from employees;"
        data = self.db_connection.select(query)
        print(data)
        sort_list = []
        for values in data:
            sort_list.append(values)
        # print(sort_list[0])
        sorted_list = self.bubble_email_ascending(sort_list)
        # messagebox.showinfo("Sorted", "Data is Sorted in Descending order By Name")
        if len(sorted_list) != 0:
            self.employee_tree.delete(*self.employee_tree.get_children())
            for values in sorted_list:
                data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
                             values[8],
                             values[9], values[10], values[11], values[12], values[13], values[14]]
                self.employee_tree.insert('', END, values=data_list)

    def sort_by_email_descending(self):
        """this will sort the email in descending order, here data is extracted from database and then
        all the data containing id are sent to bubble_sort_descending() methods to sort that data and
        lastly those data are again inserted into table in sorted form"""
        # print("i am in sort by name in descending order")
        query = "select * from employees;"
        data = self.db_connection.select(query)
        print(data)
        sort_list = []
        for values in data:
            sort_list.append(values)
        # print(sort_list[0])
        sorted_list = self.bubble_email_descending(sort_list)
        # messagebox.showinfo("Sorted", "Data is Sorted in Descending order By Name")
        if len(sorted_list) != 0:
            self.employee_tree.delete(*self.employee_tree.get_children())
            for values in sorted_list:
                data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
                             values[8],
                             values[9], values[10], values[11], values[12], values[13], values[14]]
                self.employee_tree.insert('', END, values=data_list)


    def bubble_email_ascending(self,list):
        """this will sort the data by using bubble sort method while performing sort data"""
        print("Success")
        for j in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i][2].upper() > list[i + 1][2].upper():
                    list[i], list[i + 1] = list[i + 1], list[i]
        print('the sorted list is ', list)
        return list

    def bubble_email_descending(self,list):

        print("Success")
        for j in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i][2].upper() < list[i + 1][2].upper():
                    list[i], list[i + 1] = list[i + 1], list[i]
        print('the sorted list is ', list)
        return list

    def sort_by_phone_ascending(self):
        """this will sort the phone in ascending order, here data is extracted from database and then
        all the data containing id are sent to bubble_sort_ascending() methods to sort that data and
        lastly those data are again inserted into table in sorted form"""
        query = "select * from employees;"
        data = self.db_connection.select(query)
        print(data)
        sort_list = []
        for values in data:
            sort_list.append(values)
        # print(sort_list[0])
        sorted_list = self.bubble_phone_ascending(sort_list)
        # messagebox.showinfo("Sorted", "Data is Sorted in Descending order By Name")
        if len(sorted_list) != 0:
            self.employee_tree.delete(*self.employee_tree.get_children())
            for values in sorted_list:
                data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
                             values[8],
                             values[9], values[10], values[11], values[12], values[13], values[14]]
                self.employee_tree.insert('', END, values=data_list)

    def sort_by_phone_descending(self):
        """this will sort the phone in descending order, here data is extracted from database and then
        all the data containing id are sent to bubble_sort_descending() methods to sort that data and
        lastly those data are again inserted into table in sorted form"""
        # print("i am in sort by name in descending order")
        query = "select * from employees;"
        data = self.db_connection.select(query)
        print(data)
        sort_list = []
        for values in data:
            sort_list.append(values)
        # print(sort_list[0])
        sorted_list = self.bubble_phone_descending(sort_list)
        # messagebox.showinfo("Sorted", "Data is Sorted in Descending order By Name")
        if len(sorted_list) != 0:
            self.employee_tree.delete(*self.employee_tree.get_children())
            for values in sorted_list:
                data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
                             values[8],
                             values[9], values[10], values[11], values[12], values[13], values[14]]
                self.employee_tree.insert('', END, values=data_list)


    def bubble_phone_ascending(self,list):
        """this will sort the data by using bubble sort method while performing sort data"""
        # print("Success")
        for j in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i][9].upper() > list[i + 1][9].upper():
                    list[i], list[i + 1] = list[i + 1], list[i]
        # print('the sorted list is ', list)
        return list

    def bubble_phone_descending(self,list):
        """this will sort the data by using bubble sort method while performing sort data"""
        # print("Success")
        for j in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i][9].upper() < list[i + 1][9].upper():
                    list[i], list[i + 1] = list[i + 1], list[i]
        # print('the sorted list is ', list)
        return list

    def sort_by_registration_ascending(self):
        """this will sort the registration date in ascending order, here data is extracted from database and then
        all the data containing id are sent to bubble_sort_ascending() methods to sort that data and
        lastly those data are again inserted into table in sorted form"""
        query = "select * from employees;"
        data = self.db_connection.select(query)
        print(data)
        sort_list = []
        for values in data:
            sort_list.append(values)
        # print(sort_list[0])
        sorted_list = self.bubble_registration_ascending(sort_list)
        # messagebox.showinfo("Sorted", "Data is Sorted in Descending order By Name")
        if len(sorted_list) != 0:
            self.employee_tree.delete(*self.employee_tree.get_children())
            for values in sorted_list:
                data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
                             values[8],
                             values[9], values[10], values[11], values[12], values[13], values[14]]
                self.employee_tree.insert('', END, values=data_list)

    def sort_by_registration_descending(self):
        """this will sort registration date in descending order, here data is extracted from database and then
        all the data containing id are sent to bubble_sort_descending() methods to sort that data and
        lastly those data are again inserted into table in sorted form"""
        # print("i am in sort by name in descending order")
        query = "select * from employees;"
        data = self.db_connection.select(query)
        print(data)
        sort_list = []
        for values in data:
            sort_list.append(values)
        # print(sort_list[0])
        sorted_list = self.bubble_registration_descending(sort_list)
        # messagebox.showinfo("Sorted", "Data is Sorted in Descending order By Name")
        if len(sorted_list) != 0:
            self.employee_tree.delete(*self.employee_tree.get_children())
            for values in sorted_list:
                data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
                             values[8],
                             values[9], values[10], values[11], values[12], values[13], values[14]]
                self.employee_tree.insert('', END, values=data_list)


    def bubble_registration_ascending(self,list):
        """this will sort the data by using bubble sort method while performing sort data"""
        # print("Success")
        for j in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i][14] > list[i + 1][14]:
                    list[i], list[i + 1] = list[i + 1], list[i]
        # print('the sorted list is ', list)
        return list

    def bubble_registration_descending(self,list):
        """this will sort the data by using bubble sort method while performing sort data"""
        # print("Success")
        for j in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i][14] < list[i + 1][14]:
                    list[i], list[i + 1] = list[i + 1], list[i]
        # print('the sorted list is ', list)
        return list

    # =======================================================================
    # ========================Sorting Ended==================================
    # =======================================================================



    def clear_search(self, events):
        """handles the left mouse click events while searching for data in order to remove pre inserted data
        automatically"""
        self.search_entry.delete(0, "end")

    def clear_sindate(self, events):
        """handles the left mouse click events while searching for date in data in order to remove pre inserted data
        automatically"""
        self.search_in_date_entry.delete(0, "end")

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


class UpdateEmployeeForm(Frontend.employee_registration.EmployeeRegisterForm):
    """inherits EmployeeRegisterForm class and overrides the functionality by configuring the submit button
    from performing add employee to update employees. this class get the list of data that is selected on employee tree
    view and insert those data automatically into the respected fields, it do not allow the admin to update username
    of the user and restricts to change the password displaying error message as only user can change their password"""
    def __init__(self, wind):
        super().__init__(wind)
        Frontend.employee_registration.Clock(wind)
        a = ManageEmployee.list_of_tree
        # print(a)
        try:
            self.email_entry.insert(0, a[3])
            self.f_name_entry.insert(0, a[1])
            self.l_name_entry.insert(0, a[2])
            self.dob_entry.delete(0, END)
            self.dob_entry.insert(0, a[4])
            self.gender_combo.set(a[5])
            self.address_entry.insert(0, a[6])
            # self.contact_entry.insert(0, a[7])
            self.job_type_combo.set(a[8])
            self.register_as_combo.set(a[11])
            self.qualification_entry.insert(0, a[10])
            self.department_combo.set(a[9])
            self.submit.configure(command=self.validation)
            self.txt = f" You are updating {a[3]}"
        except IndexError as msg:
            print(msg)
        if self.count <= len(self.txt):
            self.count = 0
            self.text = ''
            self.heading.config(text=self.text)
        self.heading.place(x=150, y=0, width=800)

    def validation(self):
        """validates if username and password is being tried to change or not, if yes proper message is being
        displayed else when all field are filled data is being updated by calling another method"""
        if self.username_entry.get() != "":
            messagebox.showerror("Error", "Username can not be changed")
        elif self.password_entry.get() != "" or self.c_password_entry.get() != "":
            messagebox.showerror("Error", "Only User have access to change their password")
        else:
            self.update()

    def update(self):
        """updates the data of employees from entry fields"""
        try:
            obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_student_database.get_database())

            get_id = ManageEmployee.get_id
            data_id= get_id[0]
            # print(data_id)
            obj_employee_database = Model_class.employee_registration.EmployeeRegistration(self.username_entry.get(),
                                                                                           self.email_entry.get(),
                                                                                           self.password_entry.get(),
                                                                                           self.f_name_entry.get(),
                                                                                           self.l_name_entry.get(),
                                                                                           self.dob_entry.get(),
                                                                                           self.gender_combo.get(),
                                                                                           self.address_entry.get(),
                                                                                           self.contact_entry.get(),
                                                                                           self.job_type_combo.get(),
                                                                                           self.register_as_combo.get(),
                                                                                           self.qualification_entry.get(),
                                                                                           self.department_combo.get(),
                                                                                           self.reg_date)
            query = "update employees set email=%s,f_name=%s, l_name=%s,dob=%s,gender=%s,address=%s,contact_no=%s," \
                    "job_type=%s, registered_as=%s, qualification=%s, department=%s where employee_id=%s"

            values = (obj_employee_database.get_email(), obj_employee_database.get_f_name(),
                      obj_employee_database.get_l_name(), obj_employee_database.get_dob(),
                      obj_employee_database.get_gender(), obj_employee_database.get_address(),
                      obj_employee_database.get_contact(), obj_employee_database.get_job(),
                      obj_employee_database.get_reg_as(), obj_employee_database.get_qualification(),
                      obj_employee_database.get_department(), data_id)

            self.db_connection.update(query, values)

            ask=messagebox.askyesnocancel("Success", f"Data having \n Email={values[0]} \n Updated Successfully\n"
                                                 f"Do you want to Go Employee Dashboard")
            if ask is True:
                win = Toplevel()
                Frontend.manage_employee.ManageEmployee(win)
                self.window.withdraw()
                win.deiconify()

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error",f"Error due to{msg}")


class FetchEmployeeForm(Frontend.employee_registration.EmployeeRegisterForm):
    """inherits EmployeeRegisterForm and extend the functionality by fetching the data of selected employee in order to let
    user add employees by grabbing their data directly into the registration form which will save time of the admin"""
    def __init__(self, wind):
        super().__init__(wind)
        Frontend.employee_registration.Clock(wind)
        a = ManageEmployee.list_of_tree
        # print(a)
        try:
            # self.email_entry.insert(0, a[3])
            self.f_name_entry.insert(0, a[1])
            self.l_name_entry.insert(0, a[2])
            self.dob_entry.delete(0, END)
            self.dob_entry.insert(0, a[4])
            self.gender_combo.set(a[5])
            self.address_entry.insert(0, a[6])
            self.contact_entry.insert(0, a[7])
            self.job_type_combo.set(a[8])
            self.register_as_combo.set(a[11])
            self.qualification_entry.insert(0,a[10])
            self.department_combo.set(a[9])
        except IndexError as msg:
            print(msg)


class AddAdmin(Frontend.database_connected.DatabaseConnected):
    def __init__(self, wind):
        super().__init__(wind)
        self.txt = "Add New Admin"
        self.back_button = ImageTk.PhotoImage \
            (file='images\\back.png')
        self.login_button.configure(image = self.back_button, command = self.go_to_employee)
        if self.count <= len(self.txt):
            self.count = 0
            self.text = ''
            self.heading.config(text=self.text)
        self.heading.place(x=470, y=60, width=450)

    def go_to_employee(self):
        win = Toplevel()
        Frontend.manage_employee.ManageEmployee(win)
        self.window.withdraw()
        win.deiconify()


def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    ManageEmployee(window)
    window.mainloop()


if __name__ == '__main__':
    win()
