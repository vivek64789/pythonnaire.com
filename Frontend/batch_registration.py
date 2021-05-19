from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageDraw
from ttkthemes import themed_tk as tk
from datetime import *
import time
from math import *
import random
import Backend.connection
import Model_class.batch_registration
from tkinter import messagebox
import Frontend.manage_batch


class BatchRegisterForm:
    """allows admin to register batch, it validates, if that batch code and name already exists or not, if
    it  exists then proper error message is thrown to let them know that these batch already exists. all the validations
    of entry fields are done here for registration form so that in order to add batch all fields are required.
    """
    def __init__(self, wind):
        self.window = wind
        self.window.title('BATCH REGISTRATION FORM - COLLEGE MANAGEMENT SYSTEM')
        self.window.geometry('1366x786+0+0')
        self.window.config(bg="#f29844")

        # ======================Backend connection=============
        self.db_connection = Backend.connection.DatabaseConnection()

        # creating frame for Register
        # self.img = img
        # self.dummylabel = Label(self.window, image=self.img)
        # self.dummylabel.place(x=30, y=30)

        self.reg_frame = Frame(self.window, bg="#ffffff", width=1300, height=680)
        self.reg_frame.place(x=30, y=30)

        self.txt = "Batch Registration Form"
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

        self.batch_frame = LabelFrame(self.reg_frame, text="Batch Details", bg="white", fg="#4f4e4d", height=380,
                                      width=800, borderwidth=2.4,
                                      font=("yu gothic ui", 13, "bold"))
        self.batch_frame.config(highlightbackground="red")
        self.batch_frame.place(x=100, y=170)

        # ========================================================================
        # ============================Key Bindings====================================
        # ========================================================================

        self.window.bind("<Return>", self.click_enter_submit)

        # # ========================================================================
        # # ============================Batch ID label====================================
        # # ========================================================================
        #
        # self.batch_id_label = Label(self.batch_frame, text="Batch ID ", bg="white", fg="#4f4e4d",
        #                             font=("yu gothic ui", 13, "bold"))
        # self.batch_id_label.place(x=160, y=25)
        #
        # self.batch_id_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
        #                             font=("yu gothic ui semibold", 12))
        # self.batch_id_entry.place(x=370, y=252, width=374)  # trebuchet ms
        #
        # self.batch_id_line = Canvas(self.window, width=374, height=1.5, bg="#bdb9b1", highlightthickness=0)
        # self.batch_id_line.place(x=370, y=274)

        # ========================================================================
        # ===========================batch Name==================================
        # ========================================================================

        self.batch_name_label = Label(self.batch_frame, text="Batch Name ", bg="white", fg="#4f4e4d",
                                      font=("yu gothic ui", 13, "bold"))
        self.batch_name_label.place(x=160, y=65)

        self.batch_name_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                      font=("yu gothic ui semibold", 12))
        self.batch_name_entry.place(x=400, y=292, width=345)  # trebuchet ms

        self.batch_name_line = Canvas(self.window, width=345, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.batch_name_line.place(x=400, y=314)

        # ========================================================================
        # ===========================batch YEAR ==================================
        # ========================================================================
        date = time.strftime("%Y")

        self.batch_year_label = Label(self.batch_frame, text="Batch Year ", bg="white", fg="#4f4e4d",
                                      font=("yu gothic ui", 13, "bold"))
        self.batch_year_label.place(x=160, y=115)

        self.batch_year_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                      font=("yu gothic ui semibold", 12))
        self.batch_year_entry.place(x=390, y=342, width=355)  # trebuchet ms

        self.batch_year_line = Canvas(self.window, width=355, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.batch_year_line.place(x=390, y=364)
        self.batch_year_entry.insert(0, date)

        # ========================================================================
        # ===========================batch Intake==================================
        # ========================================================================
        self.window.option_add("*TCombobox*Listbox*Foreground", '#f29844')

        self.batch_intake_label = Label(self.batch_frame, text="Batch Intake ", bg="white", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
        self.batch_intake_label.place(x=160, y=165)

        self.batch_intake_combo = ttk.Combobox(self.batch_frame, font=('yu gothic ui semibold', 12, 'bold'),
                                               state='readonly',
                                               width=35)
        self.batch_intake_combo['values'] = ("January", "February", "March", "April", "May", "June", "July", "August",
                                             "September", "October", "November", "December")
        self.batch_intake_combo.current(0)
        self.batch_intake_combo.place(x=270, y=167)
        # self.batch_intake_line.place(x=410, y=424)

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

        self.submit = Button(self.batch_frame, image=self.submit_img,
                             font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                             , borderwidth=0, background="white", cursor="hand2",command=self.validation)
        self.submit.place(x=90, y=267)

        self.clear_img = ImageTk.PhotoImage \
            (file='images\\clear.png')
        self.clear_button = Button(self.batch_frame, image=self.clear_img,
                                   font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                   , borderwidth=0, background="white", cursor="hand2",
                                   command=self.click_clear_button)
        self.clear_button.place(x=250, y=270)

        self.back_img = ImageTk.PhotoImage \
            (file='images\\back.png')
        self.back_button = Button(self.batch_frame, image=self.back_img,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2", command=self.click_back_button)
        self.back_button.place(x=410, y=270)

        self.exit_img = ImageTk.PhotoImage \
            (file='images\\exit.png')
        self.exit_button = Button(self.batch_frame, image=self.exit_img,
                                  font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2", command=self.exit)
        self.exit_button.place(x=570, y=270)

    def click_clear_button(self):
        self.batch_name_entry.delete(0, END)
        self.batch_year_entry.delete(0, END)
        self.batch_intake_combo.current(0)

    def click_back_button(self):
        """returns ManageStudent class if clicked on back button"""
        win = Toplevel()
        Frontend.manage_batch.ManageBatch(win)
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
        """this will validate if the batch code and name of entry fields are already in database table named
        batch or not if return True, error message is thrown displaying batch code/name already exists"""
        try:
            obj_batch_database = Model_class.batch_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_batch_database.get_database())

            query = "select * from batch;"
            data = self.db_connection.select(query)
            # print(data)
            self.name_list = []
            for values in data:
                name_data_list = values[1]
                self.name_list.append(name_data_list)
                # print(name_data_list)
        except BaseException as msg:
            print(msg)

        if self.batch_name_entry.get() == "" or self.batch_year_entry.get() == "":
            messagebox.showwarning("Warning", "All Fields are Required\n Please fill all required fields")

        elif self.batch_name_entry.get() in self.name_list:
            messagebox.showerror("Already Exists", f"{self.batch_name_entry.get()} Batch Already Exists")

        else:
            self.click_submit()

    def click_submit(self):
        """initialize when click submit button, which will take data from entry box
        and insert those data into student table after successful validation of those data"""
        try:
            obj_batch_database = Model_class.batch_registration.GetDatabase('use cms;')
            self.db_connection.create(obj_batch_database.get_database())

            obj_batch_database = Model_class.batch_registration.BatchRegistration(self.batch_name_entry.get(),
                                                                                  self.batch_year_entry.get(),
                                                                                  self.batch_intake_combo.get(),
                                                                                  self.reg_date)
            query = 'insert into batch (batch_name,batch_year,batch_intake,reg_date) values (%s,%s,%s,%s);'
            values = (obj_batch_database.get_name(),obj_batch_database.get_year(),
                      obj_batch_database.get_intake(),obj_batch_database.get_reg_date())
            # print(values)
            self.db_connection.insert(query, values)
            # print(values)
            messagebox.showinfo("Success", f"Batch Registered Successfully\n Batch Name={values[0]},\n "
                                           f"Batch Year={values[1]}")

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error", "There is some error Submitting Credentials ")

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
    BatchRegisterForm(window)
    Clock(window)
    window.mainloop()


if __name__ == '__main__':
    win()
