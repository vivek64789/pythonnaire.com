from tkinter import *
from tkinter import colorchooser
from tkinter import ttk
from PIL import ImageTk, Image, ImageDraw
from datetime import *
import time
from math import *
import Backend.connection
import Model_class.student_registration
from tkinter import messagebox
import os


# creating window
class Dashboard:
    def __init__(self, wind):
        self.window = wind
        self.window.title('WELCOME TO COLLEGE MANAGEMENT SYSTEM')
        self.window.iconbitmap('images\\logo.ico')
        self.window.geometry('1366x786+0+0')

        # defining frames for dashboard

        self.frame_sidebar = Frame(self.window, bg="red", bd=5, relief=GROOVE, width=120, height=685)
        self.frame_sidebar.place(x=0, y=50)

        # =================================Sub frames of sidebar========================================

        self.frame_home = Frame(self.frame_sidebar, bg="red", bd=5, relief=GROOVE, width=115, height=85)
        self.frame_home.place(x=0, y=0)

        self.frame_m_student = Frame(self.frame_sidebar, bg="red", bd=5, relief=GROOVE, width=115, height=85)
        self.frame_m_student.place(x=0, y=85)

        self.frame_m_emp = Frame(self.frame_sidebar, bg="red", bd=5, relief=GROOVE, width=115, height=85)
        self.frame_m_emp.place(x=0, y=170)

        self.frame_m_course = Frame(self.frame_sidebar, bg="red", bd=5, relief=GROOVE, width=115, height=85)
        self.frame_m_course.place(x=0, y=255)

        self.frame_view_student = Frame(self.frame_sidebar, bg="red", bd=5, relief=GROOVE, width=115, height=85)
        self.frame_view_student.place(x=0, y=340)

        self.frame_view_all = Frame(self.frame_sidebar, bg="red", bd=5, relief=GROOVE, width=115, height=85)
        self.frame_view_all.place(x=0, y=425)

        self.frame_change_password = Frame(self.frame_sidebar, bg="red", bd=5, relief=GROOVE, width=115, height=85)
        self.frame_change_password.place(x=0, y=510)

        self.frame_exit_dash = Frame(self.frame_sidebar, bg="red", bd=5, relief=GROOVE, width=115, height=85)
        self.frame_exit_dash.place(x=0, y=595)

        # ======================title bar====================================

        self.frame_titleBar = Frame(self.window, bg="red", bd=5, relief=GROOVE, width=1366, height=60)
        self.frame_titleBar.place(x=0, y=0)

        # defining Label for title bar
        self.title_logo = Label(self.frame_titleBar, text="LOGO", bg="red",
                                font=("Halvetica", 25, "bold"))
        self.title_logo.place(x=10, y=5)

        self.title_label = Label(self.frame_titleBar, text="COLLEGE MANAGEMENT SYSTEM", bg="red",
                                 font=("Halvetica", 20, "bold"))
        self.title_label.place(x=200, y=10)

        self.title_clock_label = Label(self.frame_titleBar, text="DIGITAL CLOCK WITH DATE", bg="red",
                                       font=("Halvetica", 10, "bold"))
        self.title_clock_label.place(x=800, y=15)

        self.title_active_account = Label(self.frame_titleBar, text="demo@gmail.com", bg="red",
                                          font=("Halvetica", 10, "bold"))
        self.title_active_account.place(x=1000, y=15)

        # Defining Button for title bar
        self.title_color_picker = Button(self.frame_titleBar, text="Choose skin color", bg="red"
                                         , font=("Halvetica", 10, "bold"),
                                         bd=5, relief=GROOVE, cursor="hand2", command=self.choose_color)
        self.title_color_picker.place(x=1130, y=10)

        # self.s_color=s_color
        self.title_logout_button = Button(self.frame_titleBar, text="Logout", bg="red"
                                          , font=("Halvetica", 10, "bold"),
                                          bd=5, relief=GROOVE, cursor="hand2")
        self.title_logout_button.place(x=1280, y=10)

        # Defining button for sidebar
        self.sidebar_home_button = Button(self.frame_home, text="Home", bg="red"
                                          , font=("Halvetica", 10, "bold"),
                                          bd=5, relief=GROOVE, cursor="hand2")
        self.sidebar_home_button.place(x=25, y=20)

        self.sidebar_m_student_button = Button(self.frame_m_student, text=" Manage \nStudent ", bg="red"
                                               , font=("Halvetica", 10, "bold"),
                                               bd=5, relief=GROOVE, cursor="hand2")
        self.sidebar_m_student_button.place(x=15, y=15)

        self.sidebar_home_button = Button(self.frame_home, text="Home", bg="red"
                                          , font=("Halvetica", 10, "bold"),
                                          bd=5, relief=GROOVE, cursor="hand2")
        self.sidebar_home_button.place(x=25, y=20)

    def choose_color(self):
        self.my_color = colorchooser.askcolor()[1]
        print(self.my_color)

        self.frame_sidebar = Frame(self.window, bg=self.my_color, bd=5, relief=GROOVE, width=120, height=685)
        self.frame_sidebar.place(x=0, y=50)

        # =================================Sub frames of sidebar========================================

        self.frame_home = Frame(self.frame_sidebar, bg=self.my_color, bd=5, relief=GROOVE, width=115, height=85)
        self.frame_home.place(x=0, y=0)

        self.frame_m_student = Frame(self.frame_sidebar, bg=self.my_color, bd=5, relief=GROOVE, width=115, height=85)
        self.frame_m_student.place(x=0, y=85)

        self.frame_m_emp = Frame(self.frame_sidebar, bg=self.my_color, bd=5, relief=GROOVE, width=115, height=85)
        self.frame_m_emp.place(x=0, y=170)

        self.frame_m_course = Frame(self.frame_sidebar, bg=self.my_color, bd=5, relief=GROOVE, width=115, height=85)
        self.frame_m_course.place(x=0, y=255)

        self.frame_view_student = Frame(self.frame_sidebar, bg=self.my_color, bd=5, relief=GROOVE, width=115, height=85)
        self.frame_view_student.place(x=0, y=340)

        self.frame_view_all = Frame(self.frame_sidebar, bg=self.my_color, bd=5, relief=GROOVE, width=115, height=85)
        self.frame_view_all.place(x=0, y=425)

        self.frame_change_password = Frame(self.frame_sidebar, bg=self.my_color, bd=5, relief=GROOVE, width=115,
                                           height=85)
        self.frame_change_password.place(x=0, y=510)

        self.frame_exit_dash = Frame(self.frame_sidebar, bg=self.my_color, bd=5, relief=GROOVE, width=115, height=85)
        self.frame_exit_dash.place(x=0, y=595)

        # ======================title bar====================================

        self.frame_titleBar = Frame(self.window, bg=self.my_color, bd=5, relief=GROOVE, width=1366, height=60)
        self.frame_titleBar.place(x=0, y=0)

        # defining Label for title bar
        self.title_logo = Label(self.frame_titleBar, text="LOGO", bg=self.my_color,
                                font=("Halvetica", 25, "bold"))
        self.title_logo.place(x=10, y=5)

        self.title_label = Label(self.frame_titleBar, text="COLLEGE MANAGEMENT SYSTEM", bg=self.my_color,
                                 font=("Halvetica", 20, "bold"))
        self.title_label.place(x=200, y=10)

        self.title_clock_label = Label(self.frame_titleBar, text="DIGITAL CLOCK WITH DATE", bg=self.my_color,
                                       font=("Halvetica", 10, "bold"))
        self.title_clock_label.place(x=800, y=15)

        self.title_active_account = Label(self.frame_titleBar, text="demo@gmail.com", bg=self.my_color,
                                          font=("Halvetica", 10, "bold"))
        self.title_active_account.place(x=1000, y=15)

        # Defining Button for title bar
        self.title_color_picker = Button(self.frame_titleBar, text="Choose skin color", bg=self.my_color
                                         , font=("Halvetica", 10, "bold"),
                                         bd=5, relief=GROOVE, cursor="hand2", command=self.choose_color)
        self.title_color_picker.place(x=1130, y=10)

        # self.s_color=s_color
        self.title_logout_button = Button(self.frame_titleBar, text="Logout", bg=self.my_color
                                          , font=("Halvetica", 10, "bold"),
                                          bd=5, relief=GROOVE, cursor="hand2")
        self.title_logout_button.place(x=1280, y=10)

        # Defining button for sidebar
        self.sidebar_home_button = Button(self.frame_home, text="Home", bg=self.my_color
                                          , font=("Halvetica", 10, "bold"),
                                          bd=5, relief=GROOVE, cursor="hand2")
        self.sidebar_home_button.place(x=25, y=20)

        self.sidebar_m_student_button = Button(self.frame_m_student, text=" Manage \nStudent ", bg=self.my_color
                                               , font=("Halvetica", 10, "bold"),
                                               bd=5, relief=GROOVE, cursor="hand2")
        self.sidebar_m_student_button.place(x=15, y=15)

        self.sidebar_home_button = Button(self.frame_home, text="Home", bg=self.my_color
                                          , font=("Halvetica", 10, "bold"),
                                          bd=5, relief=GROOVE, cursor="hand2")
        self.sidebar_home_button.place(x=25, y=20)


def win():
    window = Tk()
    Dashboard(window)
    window.mainloop()


if __name__ == '__main__':
    win()
