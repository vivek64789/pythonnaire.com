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
import Frontend.student_registration
import Frontend.login_form
from tkinter import messagebox
import os


class Welcome:
    def __init__(self, window, img, instructor,student,admin):
        self.window = window
        self.window.geometry("1366x720+0+0")
        self.window.title("WELCOME TO STUDENT MANAGEMENT SYSTEM")
        self.window.iconbitmap('D:\\Softwarica study material\\Semester 2\\Introduction to Algorithm\\'
                               'Coding_and_Algorithms\\190352_Bibekanand_kushwaha_Sem_2_Final_assignment\\im'
                               'ages\\logo.ico')
        self.window.resizable(False, False)
        self.background_img = img
        self.image_panel = Label(self.window, image=self.background_img)
        self.image_panel.pack(fill='both', expand='yes')

        self.student = student
        self.student_button = Button(self.window, image=self.student, relief=FLAT, borderwidth=0,
                                     activebackground="white", bg="white",cursor="hand2")
        self.student_button.place(x=244, y=210)

        self.instructor = instructor
        self.instructor_button = Button(self.window, image=self.instructor, relief=FLAT, borderwidth=0,
                                       activebackground="white", bg="white",cursor="hand2")
        self.instructor_button.place(x=609, y=210)

        self.admin = admin
        self.admin_button = Button(self.window, image=self.admin, relief=FLAT, borderwidth=0,
                                     activebackground="white", bg="white",cursor="hand2",command=self.admin_login)
        self.admin_button.place(x=969, y=210)

        self.reg_student_button = Button(self.window, image=self.student, relief=FLAT, borderwidth=0,
                                     activebackground="white", bg="white",cursor="hand2")
        self.reg_student_button.place(x=419, y=545)

        self.reg_instructor_button = Button(self.window, image=self.instructor, relief=FLAT, borderwidth=0,
                                        activebackground="white", bg="white",cursor="hand2")
        self.reg_instructor_button.place(x=794, y=545)

    def student_login(self):
        pass

    def instructor_login(self):
        pass

    def admin_login(self):
        window=Tk()
        Frontend.login_form.Login(window)

    def student_register(self):
        window=Tk()
        Frontend.student_registration.Register_form(window)

    def instructor_register(self):
        pass


def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    img = ImageTk.PhotoImage(Image.open("D:\\Softwarica study material\\Semester 2\\Introduction to "
                                        "Algorithm\\Coding_and_Algorithms\\190352_Bibekana"
                                        "nd_kushwaha_Sem_2_Final_assignment\\images\\welcome_frame.png"))

    instructor = ImageTk.PhotoImage(Image.open("D:\\Softwarica study material\\Semester 2\\Introduction to "
                                               "Algorithm\\Coding_and_Algorithms\\190352_Bibekana"
                                               "nd_kushwaha_Sem_2_Final_assignment\\images\\instructor.png"))

    student = ImageTk.PhotoImage(Image.open("D:\\Softwarica study material\\Semester 2\\Introduction to "
                                               "Algorithm\\Coding_and_Algorithms\\190352_Bibekana"
                                               "nd_kushwaha_Sem_2_Final_assignment\\images\\student.png"))

    admin = ImageTk.PhotoImage(Image.open("D:\\Softwarica study material\\Semester 2\\Introduction to "
                                            "Algorithm\\Coding_and_Algorithms\\190352_Bibekana"
                                            "nd_kushwaha_Sem_2_Final_assignment\\images\\admin.png"))

    Welcome(window, img, instructor,student,admin)
    window.mainloop()


if __name__ == '__main__':
    win()
