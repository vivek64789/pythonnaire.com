from tkinter import *
from tkinter import ttk
from tkcalendar import *
from PIL import ImageTk
from ttkthemes import themed_tk as tk
import random
import Backend.connection
import Model_class.student_registration
from tkinter import messagebox
import Frontend.connect_database
import Frontend.forgot_password
import Frontend.login_form
import Frontend.admin_dashboard
import Frontend.batch_registration
import Model_class.batch_registration


class ManageBatch:
    """Allows Admin to manage batch; add, update, delete, fetch the data, here, admin can view all the details of
    batch and have various option to perform, they can search them by different functionality, such as batch_id,
    name, and also they can search data such as id, name from one date to another.
    searching can be performed even just by providing the character that the batch detail may contain and it will
    fetch all the data regarding that. this was done by using wild card feature of MySQL after grabbing all the data
    and then performing bubble sort on that and later sent to binary search method if data exists then all the data
    were inserted on the batch tree view. to make sorting possible, bubble sort method is used. also this method
    is used to sort the data in order to search"""
    list_of_tree = []
    get_id = []

    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x720+0+0")
        self.window.title("Batch Management Dashboard - College Management System")
        self.window.iconbitmap('images\\logo.ico')
        self.window.resizable(False, False)
        self.manage_student_frame = ImageTk.PhotoImage \
            (file='images\\student_frame.png')
        self.image_panel = Label(self.window, image=self.manage_student_frame)
        self.image_panel.pack(fill='both', expand='yes')

        self.db_connection = Backend.connection.DatabaseConnection()

        self.txt = "Batch Management Dashboard"
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

        personal_frame = LabelFrame(left_view_frame, text="Batch Management Options", bg="white", fg="#4f4e4d",
                                    height=465,
                                    width=303, borderwidth=2.4,
                                    font=("yu gothic ui", 13, "bold"))
        personal_frame.config(highlightbackground="red")
        personal_frame.place(x=5, y=45)

        # ========================================================================
        # ============================Add Batch button===============================
        # ========================================================================

        self.add_batch = ImageTk.PhotoImage \
            (file='images\\add_batch.png')
        self.add_batch_button = Button(personal_frame, image=self.add_batch, relief=FLAT, borderwidth=0,
                                       activebackground="white", bg="white", cursor="hand2",
                                       command=self.click_add_batch)
        self.add_batch_button.place(x=8, y=100)
        # self.add_student_button.place(x=36, y=295)

        # ========================================================================
        # ============================Update batch button===============================
        # ========================================================================

        self.update_batch = ImageTk.PhotoImage \
            (file='images\\update_batch.png')
        self.update_batch_button = Button(personal_frame, image=self.update_batch, relief=FLAT, borderwidth=0,
                                          activebackground="white", bg="white", cursor="hand2",
                                          command=self.tree_event_handle)
        self.update_batch_button.place(x=8, y=165)
        # self.update_student_button.place(x=36, y=355)

        # ========================================================================
        # ============================Delete batch button===============================
        # ========================================================================

        self.delete_batch = ImageTk.PhotoImage \
            (file='images\\delete_batch.png')
        self.delete_batch_button = Button(personal_frame, image=self.delete_batch, relief=FLAT, borderwidth=0,
                                          activebackground="white", bg="white", cursor="hand2",command= self.click_delete_batch)
        self.delete_batch_button.place(x=8, y=230)

        # self.delete_student_button.place(x=36, y=405)

        # ========================================================================
        # ============================Goto Main dashboard button===============================
        # ========================================================================

        self.goto_dashboard = ImageTk.PhotoImage \
            (file='images\\goto_dashboard.png')
        self.goto_dashboard_button = Button(personal_frame, image=self.goto_dashboard, relief=FLAT, borderwidth=0,
                                            activebackground="white", bg="white", cursor="hand2",
                                            command=self.click_go_to_dashboard)
        self.goto_dashboard_button.place(x=8, y=295)

        # =======================================================================
        # ========================Starting Tree View=============================
        # =======================================================================
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('yu gothic ui', 10, "bold"), foreground="red")

        scroll_x = Scrollbar(self.tree_view_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.tree_view_frame, orient=VERTICAL)
        self.batch_tree = ttk.Treeview(self.tree_view_frame,
                                       columns=(
                                           "BATCH ID", "BATCH NAME", "BATCH YEAR", "BATCH INTAKE", "REGISTRATION DATE"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.batch_tree.xview)
        scroll_y.config(command=self.batch_tree.yview)

        # ==========================TreeView Heading====================
        self.batch_tree.heading("BATCH ID", text="BATCH ID")
        self.batch_tree.heading("BATCH NAME", text="BATCH NAME")
        self.batch_tree.heading("BATCH YEAR", text="BATCH YEAR")
        self.batch_tree.heading("BATCH INTAKE", text="BATCH INTAKE")
        self.batch_tree.heading("REGISTRATION DATE", text="REGISTRATION DATE")
        self.batch_tree["show"] = "headings"

        # ==========================TreeView Column====================
        self.batch_tree.column("BATCH ID", width=50)
        self.batch_tree.column("BATCH NAME", width=150)
        self.batch_tree.column("BATCH YEAR", width=100)
        self.batch_tree.column("BATCH INTAKE", width=100)
        self.batch_tree.column("REGISTRATION DATE", width=100)
        self.batch_tree.pack(fill=BOTH, expand=1)
        self.batch_tree.bind("<Delete>", self.click_delete_key)
        self.batch_tree.bind("<Button-3>", self.do_popup)
        self.batch_tree.bind("<Double-Button-1>", self.tree_double_click)
        self.batch_tree.bind("<Return>", self.tree_double_click)
        self.search_start()
        self.search_by.current(0)
        self.click_view_all()

    def click_view_all(self):
        """it will show all the data contains on the batch table of cms database, when clicked by default this method
        is called while initializing the class ManageBatch. Exception is handled to avoid run time error which may
        cause by user."""
        try:
            obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_student_database.get_database())

            query = "select * from batch;"
            data = self.db_connection.select(query)
            # print(data)
            self.batch_tree.delete(*self.batch_tree.get_children())
            for values in data:
                data_list = [values[0], values[1], values[2], values[3], values[4]]
                print(data_list)
                self.batch_tree.insert('', END, values=data_list)

        except BaseException as msg:
            print(msg)

    def click_go_to_dashboard(self):
        """returns AdminDashboard class when clicked go to dashboard"""
        win = Toplevel()
        Frontend.admin_dashboard.AdminDashboard(win)
        self.window.withdraw()
        win.deiconify()

    def click_add_batch(self):
        """returns BatchRegisterForm class when clicked go to add batch button, where admin can add new batch
        to the database"""
        win = Toplevel()
        Frontend.batch_registration.BatchRegisterForm(win)
        Frontend.batch_registration.Clock(win)
        self.window.withdraw()
        win.deiconify()

    def tree_double_click(self, events):
        """Double click of mouse events is being handled here, and tree_event_handle() methods is being called"""
        self.tree_event_handle()

    def tree_event_handle(self):
        try:
            obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_student_database.get_database())

            tree_view_content = self.batch_tree.focus()
            tree_view_items = self.batch_tree.item(tree_view_content)
            # print(tree_view_items)
            tree_view_values = tree_view_items['values']
            tree_view_id = tree_view_items['values'][0]
            # print(tree_view_id)
            ManageBatch.list_of_tree.clear()
            ManageBatch.get_id.clear()
            ManageBatch.get_id.append(tree_view_id)
            for i in tree_view_values:
                ManageBatch.list_of_tree.append(i)

            ask = messagebox.askyesno("Confirm",
                                      f"Do you want to Update Student having id {tree_view_id}")
            if ask is True:
                self.click_update_batch()

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error",
                                 "There is some error updating the data\n Make sure you have Selected the data")

    def click_update_batch(self):
        """calls UpdateBatchForm class when clicked on update Batch button"""
        win_ = Toplevel()
        UpdateBatchForm(win_)
        self.window.withdraw()
        win_.deiconify()

    def click_delete_key(self, events):
        """delete key of keyboard events is being handled here, and click_delete_batch() methods is being called"""
        self.click_delete_batch()

    def click_delete_batch(self):
        """when clicked delete batch, it will require to select the batch and after selecting and
        performing the delete method, it will ask the admin either they are sure they want to delete that batch
        or not if yes then batch containing that id in batch table is deleted."""
        try:
            obj_batch_registration_database = Model_class.batch_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_batch_registration_database.get_database())

            batch_view_content = self.batch_tree.focus()
            batch_view_items = self.batch_tree.item(batch_view_content)
            batch_view_values = batch_view_items['values'][0]
            ask = messagebox.askyesno("Warning",
                                      f"Are you sure you want to delete batch having id {batch_view_values}")
            if ask is True:
                query = "delete from batch where batch_id=%s;"
                self.db_connection.delete(query, (batch_view_values,))
                messagebox.showinfo("Success", f" batch id {batch_view_values} deleted Successfully")

                self.click_view_all()
            else:
                pass

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error",
                                 "There is some error deleting the data\n Make sure you have Selected the data")

    def do_popup(self, event):
        """does popup menu when clicked right click on tree view, where there will be three option to choose from
        if chosen update it will call update method and similar to that for remaining menus"""
        popup = Menu(self.window, tearoff=0)
        popup.add_command(label="UPDATE", command=self.tree_event_handle)
        popup.add_separator()
        popup.add_command(label="DELETE", command=self.click_delete_batch)
        popup.add_separator()
        popup.add_command(label="FETCH", command=self.click_fetch_batch)

        try:
            popup.tk_popup(event.x_root, event.y_root, 0)
        finally:
            # make sure to release the grab (Tk 8.0a1 only)
            popup.grab_release()

    def click_fetch_batch(self):
        """when chosen fetch batch from popup menu, this methods will be executed which will grab all the
        information of that batch into list and calls get_fetch_batch() methods when output is True"""
        try:
            obj_batch_database = Model_class.batch_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_batch_database.get_database())

            tree_view_content = self.batch_tree.focus()
            tree_view_items = self.batch_tree.item(tree_view_content)
            # print(tree_view_items)
            tree_view_values = tree_view_items['values']
            tree_view_id = tree_view_items['values'][0]
            ManageBatch.list_of_tree.clear()
            for i in tree_view_values:
                ManageBatch.list_of_tree.append(i)
            # print(ManageStudent.list_of_tree)
            # print(tree_view_values)

            ask = messagebox.askyesno("Confirm",
                                      f"Do you want to Fetch Student having id {tree_view_id}")
            if ask is True:
                self.get_fetch_batch()

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error",
                                 "There is some error fetching the data\n Make sure you have Selected the data")

    def get_fetch_batch(self):
        """calls FetchBatchForm class when clicked on fetch option of popup menu"""
        win_ = Toplevel()
        FetchBatchForm(win_)
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
        """this class methods sort the integer value of user input such as id"""
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
                    for child in self.batch_tree.get_children():
                        val = self.batch_tree.item(child)["values"][0]
                        search_list.append(val)

                    # print(search_list)

                    output = self.binary_search(search_list, int(self.search_entry.get()))
                    # print(output)
                    if output:
                        messagebox.showinfo("Found", f"batch having id {output} found")

                        obj_batch_database = Model_class.batch_registration.GetDatabase('use cms;')
                        self.db_connection.create(obj_batch_database.get_database())

                        query = "select * from batch where batch_id=%s;"
                        # print(output)
                        data = self.db_connection.search(query, (output,))
                        # print(data)
                        # self.batch_tree.delete(*self.batch_tree.get_children())

                        for values in data:
                            data_list = [values[0], values[1], values[2], values[3], values[4]]

                            self.batch_tree.delete(*self.batch_tree.get_children())
                            self.batch_tree.insert('', END, values=data_list)

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
                    for child in self.batch_tree.get_children():
                        val = self.batch_tree.item(child)["values"][1]
                        search_list.append(val)
                    # print(search_list)

                    sorted_list = self.bubble_sort(search_list)

                    self.output = self.binary_search(sorted_list, self.search_entry.get())
                    # print(output)
                    if self.output:
                        messagebox.showinfo("Found", f"batch having Name '{self.output}' found")

                        obj_batch_database = Model_class.batch_registration.GetDatabase('use cms;')
                        self.db_connection.create(obj_batch_database.get_database())

                        query = "select * from batch where batch_name LIKE '" + str(self.output) + "%'"
                        # print(output)
                        data = self.db_connection.select(query)
                        # print(data)
                        self.batch_tree.delete(*self.batch_tree.get_children())

                        for values in data:
                            data_list = [values[0], values[1], values[2], values[3], values[4]]

                            # self.batch_tree.delete(*self.batch_tree.get_children())
                            self.batch_tree.insert('', END, values=data_list)

                    else:
                        messagebox.showerror("Error", " Name Not found\n Relevant Name are Extracted")

                        obj_batch_database = Model_class.batch_registration.GetDatabase('use cms;')
                        self.db_connection.create(obj_batch_database.get_database())

                        query = "select * from batch where batch_name LIKE '%" + str(self.search_entry.get()) + "%'"
                        # print(output)
                        data = self.db_connection.select(query)
                        # print(data)
                        self.batch_tree.delete(*self.batch_tree.get_children())

                        for values in data:
                            data_list = [values[0], values[1], values[2], values[3], values[4]]

                            # self.batch_tree.delete(*self.batch_tree.get_children())
                            self.batch_tree.insert('', END, values=data_list)

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
                    obj_batch_database = Model_class.batch_registration.GetDatabase('use cms;')
                    self.db_connection.create(obj_batch_database.get_database())

                    query = "select * from batch where batch_name LIKE '%" + str(
                        self.search_in_date_entry.get()) + "%'  AND reg_date between %s and %s OR batch_year LIKE '%" + str(
                        self.search_in_date_entry.get()) + "%' AND reg_date between %s and %s"

                    # query = "select * from batch where batch_name LIKE '%" + str(self.search_in_date_entry.get()) + "%' AND reg_date between %s and %s"
                    # query = "select * from batch where reg_date between %s and %s"
                    # query = "select * from batch where batch_name LIKE '%" + str(self.search_entry.get()) + "%' and reg_date between %s and %s"
                    # print(output)
                    data = self.db_connection.search(query,
                                                     (self.search_fdate_entry.get(), self.search_tdate_entry.get(),
                                                      self.search_fdate_entry.get(), self.search_tdate_entry.get()))
                    print(data)
                    if data:
                        self.batch_tree.delete(*self.batch_tree.get_children())

                        for values in data:
                            data_list = [values[0], values[1], values[2], values[3], values[4]]

                            # self.batch_tree.delete(*self.batch_tree.get_children())
                            self.batch_tree.insert('', END, values=data_list)

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

        if self.search_by.get() == "Batch ID":
            self.search_start()
            self.search_button.configure(command=self.search_by_id_start)

        if self.search_by.get() == "Batch Name":
            self.search_start()
            self.search_button.configure(command=self.search_by_name_start)

        if self.search_by.get() == "Date":
            self.search_date()
            self.search_date_button.configure(command=self.search_by_date_start)

        # ======================================================================
        # =====================================searching END====================
        # ======================================================================

    def search_start(self):
        """here search frame, label, combobox are written which is shown while admin views batch dashboard"""

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
                                      width=15, textvariable=self.search_by_var)
        self.search_by['values'] = ('Search by', 'Batch ID', 'Batch Name', 'Date')
        self.search_by.place(x=145, y=3)
        # self.search_by.current(0)
        self.search_by.bind('<<ComboboxSelected>>', self.start_search_combo)

        self.search_start_frame = Frame(self.window, bg="white")
        self.search_start_frame.place(x=698, y=105, height=35, width=449)
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
        """here search date frame, label, calender events are written which is shown while admin view batch
        dashboard"""
        self.search_date_frame = Frame(self.window, bg="white")
        self.search_date_frame.place(x=696, y=105, height=35, width=539)

        self.search_date_img = ImageTk.PhotoImage \
            (file='images\\search.png')
        self.search_date_button = Button(self.search_date_frame, image=self.search_date_img, relief=FLAT, borderwidth=0,
                                         activebackground="white", bg="white", cursor="hand2")
        self.search_date_button.place(x=457, y=5)

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
        self.search_in_date_entry.place(x=240, y=3, width=210)  # trebuchet ms
        self.search_in_date_entry.bind("<1>", self.clear_sindate)

        self.search_in_date_line = Canvas(self.search_date_frame, width=210, height=1.5, bg="#bdb9b1",
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
        self.sort_by['values'] = ('Sort by', 'Batch ID', 'Batch Name', 'Date')
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

        self.sort_img = ImageTk.PhotoImage \
            (file='images\\sort.png')
        self.sort_button = Button(self.sort_start_frame, image=self.sort_img, relief=FLAT, borderwidth=0,
                                  activebackground="white", bg="white", cursor="hand2")
        self.sort_button.place(x=619, y=5)

    def start_sort_combo(self, events):
        """handles the sort by comobobox events of sort_by attribute and calls methods when validation is filled"""
        if self.sort_by.get() == "Sort by" or self.sort_by.get() == "Department ID" or self.sort_by.get() == "Department Name":
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
        self.sort_date_in['values'] = ('Ascending Order', 'Descending Order', 'Recent Registration',
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

    def sort_by_start(self, events):
        """events for combobox in order to sort the data starts here"""
        if self.sort_by.get() == "Sort by":
            self.sort_button.configure(command=self.sort_by_id_ascending)
            self.sort_by_id_ascending()

        if self.sort_by.get() == "Batch ID" and self.sort_in.get() == "Ascending Order":
            self.sort_button.configure(command=self.sort_by_id_ascending)
            self.sort_by_id_ascending()

        if self.sort_by.get() == "Batch ID" and self.sort_in.get() == "Descending Order":
            self.sort_button.configure(command=self.sort_by_id_descending)
            self.sort_by_id_descending()

        if self.sort_by.get() == "Batch Name" and self.sort_in.get() == "Ascending Order":
            self.sort_button.configure(command=self.sort_by_name_ascending)
            self.sort_by_name_ascending()

        if self.sort_by.get() == "Batch Name" and self.sort_in.get() == "Descending Order":
            self.sort_button.configure(command=self.sort_by_name_descending)
            self.sort_by_name_descending()

        if self.sort_by.get() == "Date" and self.sort_in.get() == "Ascending Order":
            self.sort_button.configure(command=self.sort_by_registration_ascending)
            self.sort_by_registration_ascending()

        if self.sort_by.get() == "Date" and self.sort_in.get() == "Descending Order":
            self.sort_button.configure(command=self.sort_by_registration_descending)
            self.sort_by_registration_descending()

    def sort_by_id_ascending(self):
        """this will sort the id in ascending order, here data is extracted from database and then
        all the data containing id are sent to bubble_sort_ascending() methods to sort that data and
        lastly those data are again inserted into table in sorted form"""
        query = "select * from batch;"
        data = self.db_connection.select(query)
        sort_list = []
        for values in data:
            sort_list.append(values)
        # print(sort_list)
        sorted_list = self.bubble_sort_ascending(sort_list)
        # messagebox.showinfo("Sorted", "Data is sorted in Ascending order by ID")
        if len(sorted_list) != 0:
            self.batch_tree.delete(*self.batch_tree.get_children())
            for values in sorted_list:
                data_list = [values[0], values[1], values[2], values[3], values[4]]
                self.batch_tree.insert('', END, values=data_list)

    def bubble_sort_ascending(self, list):
        """this will sort the data by using bubble sort method while performing sort data"""
        for j in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i] > list[i + 1]:
                    list[i], list[i + 1] = list[i + 1], list[i]
        print('the sorted list is ', list)
        return list

    def sort_by_id_descending(self):
        """ this will sort the id in descending order, here data is extracted from database and then
        all the data containing id are sent to bubble_sort_descending() methods to sort that data and
        lastly those data are again inserted into table in sorted form"""
        query = "select * from batch;"
        data = self.db_connection.select(query)
        sort_list = []
        for values in data:
            sort_list.append(values)
        # print(sort_list)
        sorted_list = self.bubble_sort_descending(sort_list)
        # messagebox.showinfo("Sorted", "Data is Sorted in Descending order By ID")
        if len(sorted_list) != 0:
            self.batch_tree.delete(*self.batch_tree.get_children())
            for values in sorted_list:
                data_list = [values[0], values[1], values[2], values[3], values[4]]
                self.batch_tree.insert('', END, values=data_list)

    def bubble_sort_descending(self, list):
        """this will sort the data by using bubble sort method while performing sort data"""
        for j in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i] < list[i + 1]:
                    list[i], list[i + 1] = list[i + 1], list[i]
        print('the sorted list is ', list)
        return list

    def sort_by_name_ascending(self):
        """this will sort name in ascending order, here data is extracted from database and then
        all the data containing id are sent to bubble_sort_ascending() methods to sort that data and
        lastly those data are again inserted into table in sorted form"""
        # print("I am in sort by name in ascending order")
        query = "select * from batch;"
        data = self.db_connection.select(query)
        print(data)
        sort_list = []
        for values in data:
            sort_list.append(values)
        # print(sort_list[0])
        sorted_list = self.bubble_name_ascending(sort_list)
        # messagebox.showinfo("Sorted", "Data is Sorted in Descending order By Name")
        if len(sorted_list) != 0:
            self.batch_tree.delete(*self.batch_tree.get_children())
            for values in sorted_list:
                data_list = [values[0], values[1], values[2], values[3], values[4]]
                self.batch_tree.insert('', END, values=data_list)

    def sort_by_name_descending(self):
        """this will sort the name in descending order, here data is extracted from database and then
        all the data containing id are sent to bubble_sort_descending() methods to sort that data and
        lastly those data are again inserted into table in sorted form"""
        # print("i am in sort by name in descending order")
        query = "select * from batch;"
        data = self.db_connection.select(query)
        print(data)
        sort_list = []
        for values in data:
            sort_list.append(values)
        # print(sort_list[0])
        sorted_list = self.bubble_name_descending(sort_list)
        # messagebox.showinfo("Sorted", "Data is Sorted in Descending order By Name")
        if len(sorted_list) != 0:
            self.batch_tree.delete(*self.batch_tree.get_children())
            for values in sorted_list:
                data_list = [values[0], values[1], values[2], values[3], values[4]]
                self.batch_tree.insert('', END, values=data_list)

    def bubble_name_ascending(self, list):
        """this will sort the data by using bubble sort method while performing sort data"""
        print("Success")
        for j in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i][1].upper() > list[i + 1][1].upper():
                    list[i], list[i + 1] = list[i + 1], list[i]
        print('the sorted list is ', list)
        return list

    def bubble_name_descending(self, list):
        """this will sort the data by using bubble sort method while performing sort data"""
        print("Success")
        for j in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i][1].upper() < list[i + 1][1].upper():
                    list[i], list[i + 1] = list[i + 1], list[i]
        print('the sorted list is ', list)
        return list

    def sort_by_registration_ascending(self):
        """this will sort the registration date in ascending order, here data is extracted from database and then
        all the data containing id are sent to bubble_sort_ascending() methods to sort that data and
        lastly those data are again inserted into table in sorted form"""
        query = "select * from batch;"
        data = self.db_connection.select(query)
        print(data)
        sort_list = []
        for values in data:
            sort_list.append(values)
        # print(sort_list[0])
        sorted_list = self.bubble_registration_ascending(sort_list)
        # messagebox.showinfo("Sorted", "Data is Sorted in Descending order By Name")
        if len(sorted_list) != 0:
            self.batch_tree.delete(*self.batch_tree.get_children())
            for values in sorted_list:
                data_list = [values[0], values[1], values[2], values[3], values[4]]
                self.batch_tree.insert('', END, values=data_list)

    def sort_by_registration_descending(self):
        """this will sort registration date in descending order, here data is extracted from database and then
        all the data containing id are sent to bubble_sort_descending() methods to sort that data and
        lastly those data are again inserted into table in sorted form"""
        # print("i am in sort by name in descending order")
        query = "select * from batch;"
        data = self.db_connection.select(query)
        print(data)
        sort_list = []
        for values in data:
            sort_list.append(values)
        # print(sort_list[0])
        sorted_list = self.bubble_registration_descending(sort_list)
        # messagebox.showinfo("Sorted", "Data is Sorted in Descending order By Name")
        if len(sorted_list) != 0:
            self.batch_tree.delete(*self.batch_tree.get_children())
            for values in sorted_list:
                data_list = [values[0], values[1], values[2], values[3], values[4]]
                self.batch_tree.insert('', END, values=data_list)

    def bubble_registration_ascending(self, list):
        """this will sort the data by using bubble sort method while performing sort data"""
        for j in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i][4] > list[i + 1][4]:
                    list[i], list[i + 1] = list[i + 1], list[i]
        # print('the sorted list is ', list)
        return list

    def bubble_registration_descending(self, list):
        """this will sort the data by using bubble sort method while performing sort data"""
        # print("Success")
        for j in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i][4] < list[i + 1][4]:
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


class UpdateBatchForm(Frontend.batch_registration.BatchRegisterForm):
    """inherits BatchRegisterForm class and overrides the functionality by configuring the submit button
    from performing add batch to update batchs. this class get the list of data that is selected on batch tree
    view and insert those data automatically into the respected fields."""
    def __init__(self, wind):
        super().__init__(wind)
        Frontend.batch_registration.Clock(wind)
        a = ManageBatch.list_of_tree
        # print(a)
        try:
            self.batch_name_entry.insert(0, a[1])
            self.batch_year_entry.delete(0,END)
            self.batch_year_entry.insert(0, a[2])
            self.submit.configure(command=self.update)
            self.txt = f" You are updating Batch '{a[1]}'"
        except IndexError as msg:
            print(msg)
        if self.count <= len(self.txt):
            self.count = 0
            self.text = ''
            self.heading.config(text=self.text)
        self.heading.place(x=150, y=0, width=800)

    def update(self):
        """updates the data of batch from entry fields"""
        try:
            obj_batch_database = Model_class.batch_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_batch_database.get_database())

            get_id = ManageBatch.get_id
            data_id = get_id[0]
            # print(data_id)

            obj_batch_database = Model_class.batch_registration.BatchRegistration(self.batch_name_entry.get(),
                                                                                  self.batch_year_entry.get(),
                                                                                  self.batch_intake_combo.get(),
                                                                                  self.reg_date)
            query = "update batch set batch_name=%s,batch_year=%s, batch_intake=%s" \
                    " where batch_id=%s"

            values = (obj_batch_database.get_name(), obj_batch_database.get_year(),
                      obj_batch_database.get_intake(), data_id)

            self.db_connection.update(query, values)

            ask = messagebox.askyesnocancel("Success",
                                            f"Data having \n Batch Name={values[0]} \n Updated Successfully\n"
                                            f"Do you want to Go Batch Dashboard")
            if ask is True:
                win = Toplevel()
                Frontend.manage_batch.ManageBatch(win)
                self.window.withdraw()
                win.deiconify()

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error", f"Error due to{msg}")


class FetchBatchForm(Frontend.batch_registration.BatchRegisterForm):
    """inherits BatchRegisterForm and extend the functionality by fetching the data of selected batch in order to let
    user add batchs by grabbing their data directly into the registration form which will save time of the admin"""
    def __init__(self, wind):
        super().__init__(wind)
        Frontend.batch_registration.Clock(wind)
        a = ManageBatch.list_of_tree
        # print(a)
        try:
            self.batch_name_entry.insert(0, a[1])
            self.batch_year_entry.delete(0,END)
            self.batch_year_entry.insert(0, a[2])
            self.batch_intake_combo.insert(0, a[3])

        except IndexError as msg:
            print(msg)


def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    ManageBatch(window)
    window.mainloop()


if __name__ == '__main__':
    win()
