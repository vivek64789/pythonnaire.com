# # # # import time
# # # # try:
# # # #     # python 2.x
# # # #     import Tkinter as tk
# # # # except ImportError:
# # # #     # python 3.x
# # # #     import tkinter as tk
# # # #
# # # # class Example(tk.Frame):
# # # #     def __init__(self, *args, **kwargs):
# # # #         tk.Frame.__init__(self, *args, **kwargs)
# # # #
# # # #         self.text = tk.Text(self, height=6, width=40)
# # # #         self.vsb = tk.Scrollbar(self, orient="vertical", command=self.text.yview)
# # # #         self.text.configure(yscrollcommand=self.vsb.set)
# # # #         self.vsb.pack(side="right", fill="y")
# # # #         self.text.pack(side="left", fill="both", expand=True)
# # # #
# # # #         self.add_timestamp()
# # # #
# # # #     def add_timestamp(self):
# # # #         self.text.insert("end", time.ctime() + "\n")
# # # #         self.text.see("end")
# # # #         self.after(1000, self.add_timestamp)
# # # #
# # # # if __name__ == "__main__":
# # # #     root =tk.Tk()
# # # #     frame = Example(root)
# # # #     frame.pack(fill="both", expand=True)
# # # #     root.mainloop()
# # # # # #
# # # # # # from tkinter import *
# # # # # # from tkinter import ttk
# # # # # # from ttkthemes import themed_tk as tk
# # # # # # from PIL import Image, ImageTk
# # # # # #
# # # # # # # #
# # # # # # # # class Test:
# # # # # # # #     def __init__(self,win):
# # # # # # # #         self.window = win
# # # # # # # #         self.window.geometry("1366x720+0+0")
# # # # # # # #         self.window.title("Dashboard")
# # # # # # # #         self.window.iconbitmap('images\\logo.ico')
# # # # # # # #         self.window.resizable(False, False)
# # # # # # # #         self.admin_dashboard_frame = ImageTk.PhotoImage \
# # # # # # # #             (file='images\\admin_frame.png')
# # # # # # # #         self.image_panel = Label(self.window, image=self.admin_dashboard_frame)
# # # # # # # #         self.image_panel.pack(fill='both', expand='yes')
# # # # # # # #
# # # # # # # #     def click_view(self):
# # # # # # # #         view_frame = Frame(self.window, bg="white")
# # # # # # # #         view_frame.place(x=145, y=105, height=576, width=1181)
# # # # # # # #
# # # # # # # #         self.view_dashboard_frame = ImageTk.PhotoImage \
# # # # # # # #             (file='images\\view_frame.png')
# # # # # # # #         self.view_panel = Label(view_frame, image=self.view_dashboard_frame, bg="white")
# # # # # # # #         self.view_panel.pack(fill='both', expand='yes')
# # # # # # # #
# # # # # # # #         # ========================================================================
# # # # # # # #         # ============================Displaying Student Information==============
# # # # # # # #         # ========================================================================
# # # # # # # #
# # # # # # # #         self.student_view_label = Label(view_frame, text="View Students Information ", bg="white", fg="#4f4e4d",
# # # # # # # #                                         font=("yu gothic ui", 13, "bold"))
# # # # # # # #         self.student_view_label.place(x=170, y=6)
# # # # # # # #
# # # # # # # #         self.view_student_frame = Frame(view_frame, bg="white")
# # # # # # # #         self.view_student_frame.place(x=10, y=40, height=526, width=575)
# # # # # # # #
# # # # # # # #         style = ttk.Style()
# # # # # # # #         style.configure("Treeview.Heading", font=('yu gothic ui', 10, "bold"), foreground="red")
# # # # # # # #
# # # # # # # #         scroll_y = Scrollbar(self.view_student_frame, orient=VERTICAL)
# # # # # # # #         scroll_x = Scrollbar(self.view_student_frame, orient=HORIZONTAL)
# # # # # # # #         self.view_student_tree = ttk.Treeview(self.view_student_frame,
# # # # # # # #                                               columns=(
# # # # # # # #                                                   "STUDENT ID", "STUDENT NAME", "SECTION", "PHONE NO."),
# # # # # # # #                                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
# # # # # # # #         scroll_x.pack(side=BOTTOM, fill=X)
# # # # # # # #         scroll_y.pack(side=RIGHT, fill=Y)
# # # # # # # #         scroll_x.config(command=self.view_student_tree.xview)
# # # # # # # #         scroll_y.config(command=self.view_student_tree.yview)
# # # # # # # #
# # # # # # # #         # ==========================TreeView Heading====================
# # # # # # # #         self.view_student_tree.heading("STUDENT ID", text="STUDENT ID")
# # # # # # # #         self.view_student_tree.heading("STUDENT NAME", text="STUDENT NAME")
# # # # # # # #         self.view_student_tree.heading("SECTION", text="SECTION")
# # # # # # # #         self.view_student_tree.heading("PHONE NO.", text="PHONE NO.")
# # # # # # # #         self.view_student_tree["show"] = "headings"
# # # # # # # #
# # # # # # # #         # ==========================TreeView Column====================
# # # # # # # #         self.view_student_tree.column("STUDENT ID", width=50)
# # # # # # # #         self.view_student_tree.column("STUDENT NAME", width=150)
# # # # # # # #         self.view_student_tree.column("SECTION", width=100)
# # # # # # # #         self.view_student_tree.column("PHONE NO.", width=100)
# # # # # # # #         self.view_student_tree.pack(fill=BOTH, expand=1)
# # # # # # # #
# # # # # # # # def win():
# # # # # # # #     window = tk.ThemedTk()
# # # # # # # #     window.get_themes()
# # # # # # # #     window.set_theme("arc")
# # # # # # # #     Test(window)
# # # # # # # #     window.mainloop()
# # # # # # # #
# # # # # # # #
# # # # # # # # if __name__ == '__main__':
# # # # # # # #     win()
# # # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #         # ========================================================================
# # # # # # #         # =========================Displaying Department Information==============
# # # # # # #         # ========================================================================
# # # # # # #
# # # # # # #         self.view_department_frame = Frame(view_frame, bg="white")
# # # # # # #         self.view_department_frame.place(x=595, y=40, height=250, width=575)
# # # # # # #
# # # # # # #         self.department_view_label = Label(view_frame, text="View Department Information ", bg="white", fg="#4f4e4d",
# # # # # # #                                          font=("yu gothic ui", 13, "bold"))
# # # # # # #         self.department_view_label.place(x=770, y=6)
# # # # # # #
# # # # # # #         scroll_y_e = Scrollbar(self.view_department_frame, orient=VERTICAL)
# # # # # # #         scroll_x_e = Scrollbar(self.view_department_frame, orient=HORIZONTAL)
# # # # # # #         self.view_department_tree = ttk.Treeview(self.view_department_frame,
# # # # # # #                                                columns=(
# # # # # # #                                                    "DEPARTMENT ID", "DEPARTMENT NAME", "DEPARTMENT CODE"),
# # # # # # #                                                xscrollcommand=scroll_x_e.set, yscrollcommand=scroll_y_e.set)
# # # # # # #         scroll_x_e.pack(side=BOTTOM, fill=X)
# # # # # # #         scroll_y_e.pack(side=RIGHT, fill=Y)
# # # # # # #         scroll_x_e.config(command=self.view_department_tree.xview)
# # # # # # #         scroll_y_e.config(command=self.view_department_tree.yview)
# # # # # # #
# # # # # # #         # ==========================TreeView Heading====================
# # # # # # #         self.view_department_tree.heading("DEPARTMENT ID", text="DEPARTMENT ID")
# # # # # # #         self.view_department_tree.heading("DEPARTMENT NAME", text="DEPARTMENT NAME")
# # # # # # #         self.view_department_tree.heading("DEPARTMENT CODE", text="DEPARTMENT CODE")
# # # # # # #         self.view_department_tree["show"] = "headings"
# # # # # # #
# # # # # # #         # ==========================TreeView Column====================
# # # # # # #         self.view_department_tree.column("DEPARTMENT ID", width=50)
# # # # # # #         self.view_department_tree.column("DEPARTMENT NAME", width=150)
# # # # # # #         self.view_department_tree.column("DEPARTMENT CODE", width=100)
# # # # # # #         self.view_department_tree.pack(fill=BOTH, expand=1)
# # # # #
# # # # #
# # # # # from tkinter import *
# # # # #
# # # # #
# # # # # class AutoScrollListBox_demo:
# # # # #     def __init__(self, master):
# # # # #         frame = Frame(master, width=500, height=400, bd=1)
# # # # #         frame.pack()
# # # # #
# # # # #         self.listbox_log = Listbox(frame, height=4)
# # # # #         self.scrollbar_log = Scrollbar(frame)
# # # # #
# # # # #         self.scrollbar_log.pack(side=RIGHT, fill=Y)
# # # # #         self.listbox_log.pack(side=LEFT, fill=Y)
# # # # #
# # # # #         self.listbox_log.configure(yscrollcommand=self.scrollbar_log.set)
# # # # #         self.scrollbar_log.configure(command=self.listbox_log.yview)
# # # # #
# # # # #         b = Button(text="Add", command=self.onAdd)
# # # # #         b.pack()
# # # # #
# # # # #         # Just to show unique items in the list
# # # # #         self.item_num = 0
# # # # #
# # # # #     def onAdd(self):
# # # # #         # Insert a new item at the end of the list
# # # # #         self.listbox_log.insert(END, "test %s" % (str(self.item_num)))
# # # # #
# # # # #         # Clear the current selected item
# # # # #         self.listbox_log.select_clear(self.listbox_log.size() - 2)
# # # # #
# # # # #         # Select the new item
# # # # #         self.listbox_log.select_set(END)
# # # # #
# # # # #         # Set the scrollbar to the end of the listbox
# # # # #         self.listbox_log.yview(END)
# # # # #
# # # # #         self.item_num += 1
# # # # #
# # # # #
# # # # # root = Tk()
# # # # # all = AutoScrollListBox_demo(root)
# # # # # root.title('AutoScroll ListBox Demo')
# # # # # root.mainloop()
# # #
# # # # generate random integer values
# # # from random import seed
# # # from random import randint
# # # import smtplib
# # #
# # # server = smtplib.SMTP_SSL ("smtp.gmail.com", 465)
# # #
# # # server.login("tkintercms@gmail.com","tkinter@12345")
# # #
# # # server.sendmail ("tkintercms@gmail.com","anandkushwaha2074@gmail.com","Hello")
# # # server.quit()
# # #
# # # # seed random number generator
# # # seed(6)
# # # # generate some integers
# # #
# # # value = randint(100000,999999)
# # # print(value)
# #
# #
# #
# #
# # from tkinter import *
# # from tkinter import ttk
# # from tkcalendar import *
# # from PIL import ImageTk, Image, ImageDraw
# # from ttkthemes import themed_tk as tk
# # from datetime import *
# # import time
# # from math import *
# # import random
# # import Backend.connection
# # import Model_class.student_registration
# # import Model_class.database_connected
# # from tkinter import messagebox
# # import Frontend.login_form
# #
# # from random import seed
# # from random import randint
# # import smtplib
# #
# # import os
# #
# #
# # class OtpVerification:
# #     def __init__(self, window):
# #         self.window = window
# #         self.window.geometry("1366x720+0+0")
# #         self.window.title("Forgot Password Form")
# #         self.window.iconbitmap('images\\logo.ico')
# #         self.window.resizable(False, False)
# #
# #         self.db_connection = Backend.connection.DatabaseConnection()
# #
# #         self.login_frame = ImageTk.PhotoImage \
# #             (file='images\\otp_verification_frame.png')
# #         self.image_panel = Label(self.window, image=self.login_frame)
# #         # self.image_panel = Label(self.window, image=ph)
# #         # self.image_panel.image = ph
# #         self.image_panel.pack(fill='both', expand='yes')
# #
# #
# #
# # def win():
# #     window = Tk()
# #     # window.get_themes()
# #     # window.set_theme("arc")
# #     OtpVerification(window)
# #     window.mainloop()
# #
# #
# # if __name__ == '__main__':
# #     win()
#
# import tkinter as tk
#
# class PasswordTest(object):
#     ''' Password Entry Demo '''
#     def __init__(self):
#         root = tk.Tk()
#         root.title("Password Entry Demo")
#
#         self.entry = e = tk.Entry(root)
#         e.pack()
#         e.bind("<Key>", self.entry_cb)
#
#         b = tk.Button(root, text="show", command=self.button_cb)
#         b.pack()
#
#         root.mainloop()
#
#     def entry_cb(self, event):
#         #print(`event.char`, event.keycode, event.keysym )
#         self.entry.config(show='')
#         #Hide text after 1000 milliseconds
#         self.entry.after(1000, lambda: self.entry.config(show='*'))
#
#     def button_cb(self):
#         print('Contents:', repr(self.entry.get()))
#
# PasswordTest()
import time

c_time = time.strftime('%H:%M:%S')
c_date = time.strftime('%Y/%m/%d')
print(c_time)
print(c_date)