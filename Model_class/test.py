from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from datetime import *
import time
from math import *
import Backend.connection
import Model_class.student_registration
from tkinter import messagebox

window=Tk()
window.title('COLLEGE MANAGEMENT SYSTEM')
window.geometry('1366x786+0+0')
user_logo = ImageTk.PhotoImage(Image.open("D:\\Softwarica study material\\Semester 2\\Introduction to "
                                                       "Algorithm\\Coding_and_Algorithms"
                                                       "\\190352_Bibekanand_kushwaha_Sem_2_Final_assignment\\images"
                                                       "\\user.png"))
user_label = Label(window, image=user_logo)
user_label.place(x=100, y=100,width=256,height=256)

window.mainloop()
