# # # # # from tkinter import *
# # # # # from tkinter import ttk
# # # # # from tkcalendar import *
# # # # # from PIL import ImageTk, Image, ImageDraw
# # # # # from ttkthemes import themed_tk as tk
# # # # # from datetime import *
# # # # # import time
# # # # # from math import *
# # # # # import random
# # # # # import Backend.connection
# # # # # import Model_class.student_registration
# # # # # from tkinter import messagebox
# # # # # import os
# # # # #
# # # # #
# # # # # class Login:
# # # # #     def __init__(self, window):
# # # # #         self.window = window
# # # # #         self.window.geometry("1366x720+0+0")
# # # # #         self.window.title("Login Form")
# # # # #         self.window.iconbitmap('D:\\Softwarica study material\\Semester 2\\Introduction to Algorithm\\'
# # # # #                                'Coding_and_Algorithms\\190352_Bibekanand_kushwaha_Sem_2_Final_assignment\\im'
# # # # #                                'ages\\logo.ico')
# # # # #         self.window.resizable(False, False)
# # # # #         self.login_frame = ImageTk.PhotoImage \
# # # # #             (file='D:\\Softwarica study material\\Semester 2\\Introduction to Algorithm\\'
# # # # #                   'Coding_and_Algorithms\\190352_Bibekanand_kushwaha_Sem_2_Final_assignment\\im'
# # # # #                   'ages\\login_frame.png')
# # # # #         self.image_panel = Label(self.window, image=self.login_frame)
# # # # #         self.image_panel.pack(fill='both', expand='yes')
# # # # #
# # # # #         self.txt = "Welcome to Login Page"
# # # # #         self.count = 0
# # # # #         self.text = ''
# # # # #         self.color = ["#4f4e4d", "#f29844", "red2"]
# # # # #         self.heading = Label(self.window, text=self.txt, font=('yu gothic ui', 30, "bold"), bg="white",
# # # # #                              fg='black',
# # # # #                              bd=5,
# # # # #                              relief=FLAT)
# # # # #         self.heading.place(x=460, y=70, width=450)
# # # # #         self.slider()
# # # # #         self.heading_color()
# # # # #
# # # # #         # ========================================================================
# # # # #         # ============================Username====================================
# # # # #         # ========================================================================
# # # # #
# # # # #         self.username_label = Label(self.window, text="Username ", bg="white", fg="#4f4e4d",
# # # # #                                     font=("yu gothic ui", 13, "bold"))
# # # # #         self.username_label.place(x=495, y=220)
# # # # #
# # # # #         self.username_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
# # # # #                                     font=("yu gothic ui semibold", 12), show="*")
# # # # #         self.username_entry.place(x=530, y=255, width=380)  # trebuchet ms
# # # # #
# # # # #         # ========================================================================
# # # # #         # ============================Password====================================
# # # # #         # ========================================================================
# # # # #
# # # # #         self.password_label = Label(self.window, text="Password ", bg="white", fg="#4f4e4d",
# # # # #                                     font=("yu gothic ui", 13, "bold"))
# # # # #         self.password_label.place(x=495, y=335)
# # # # #
# # # # #         self.password_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
# # # # #                                     font=("yu gothic ui semibold", 12), show="*")
# # # # #         self.password_entry.place(x=530, y=370, width=380)  # trebuchet ms
# # # # #
# # # # #         # ========================================================================
# # # # #         # ============================Login button================================
# # # # #         # ========================================================================
# # # # #
# # # # #         self.login = ImageTk.PhotoImage \
# # # # #             (file='D:\\Softwarica study material\\Semester 2\\Introduction to Algorithm\\'
# # # # #                   'Coding_and_Algorithms'
# # # # #                   '\\190352_Bibekanand_kushwaha_Sem_2_Final_assignment\\im'
# # # # #                   'ages\\login.png')
# # # # #
# # # # #         self.login_button = Button(self.window, image=self.login,
# # # # #                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
# # # # #                                    , borderwidth=0, background="white", cursor="hand2")
# # # # #         self.login_button.place(x=640, y=450)
# # # # #
# # # # #         # ========================================================================
# # # # #         # ============================Forgot password=============================
# # # # #         # ========================================================================
# # # # #
# # # # #         self.forgot_label = Label(self.window, text="Forgot ", bg="white", fg="#4f4e4d",
# # # # #                                   font=("yu gothic ui", 13, "bold underline"))
# # # # #         self.forgot_label.place(x=767, y=413)
# # # # #
# # # # #         self.forgot_button = Button(self.window, text="Password ?",
# # # # #                                     font=("yu gothic ui", 13, "bold underline"), fg="red", relief=FLAT,
# # # # #                                     activebackground="white"
# # # # #                                     , borderwidth=0, background="white", cursor="hand2")
# # # # #         self.forgot_button.place(x=820, y=410)
# # # # #
# # # # #         # ========================================================================
# # # # #         # ========================Database Label and button=======================
# # # # #         # ========================================================================
# # # # #
# # # # #         self.database_label = Label(self.window, text="* Please connect database first: ", bg="white", fg="#4f4e4d",
# # # # #                                     font=("yu gothic ui", 13, "bold underline"))
# # # # #         self.database_label.place(x=490, y=623)
# # # # #
# # # # #         self.database_img = ImageTk.PhotoImage \
# # # # #             (file='D:\\Softwarica study material\\Semester 2\\Introduction to Algorithm\\'
# # # # #                   'Coding_and_Algorithms\\190352_Bibekanand_kushwaha_Sem_2_Final_assignment\\im'
# # # # #                   'ages\\connect_database.png')
# # # # #         self.database_button = Button(self.window, image=self.database_img,
# # # # #                                       font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
# # # # #                                       , borderwidth=0, background="white", cursor="hand2")
# # # # #         self.database_button.place(x=750, y=620)
# # # # #
# # # # #     def slider(self):
# # # # #         if self.count >= len(self.txt):
# # # # #             self.count = -1
# # # # #             self.text = ''
# # # # #             self.heading.config(text=self.text)
# # # # #
# # # # #         else:
# # # # #             self.text = self.text + self.txt[self.count]
# # # # #             self.heading.config(text=self.text)
# # # # #         self.count += 1
# # # # #
# # # # #         self.heading.after(100, self.slider)
# # # # #
# # # # #     def heading_color(self):
# # # # #         fg = random.choice(self.color)
# # # # #         self.heading.config(fg=fg)
# # # # #         self.heading.after(50, self.heading_color)
# # # # #
# # # # #
# # # # # def win():
# # # # #     window = tk.ThemedTk()
# # # # #     window.get_themes()
# # # # #     window.set_theme("arc")
# # # # #     Login(window)
# # # # #     window.mainloop()
# # # # #
# # # # #
# # # # # if __name__ == '__main__':
# # # # #     win()
# # # #
# # # # # creating popup menu in tkinter
# # # # import tkinter
# # # #
# # # #
# # # # class A:
# # # #     # creates parent window
# # # #     def __init__(self):
# # # #
# # # #         self.root = tkinter.Tk()
# # # #         self.root.geometry('500x500')
# # # #
# # # #         self.frame1 = tkinter.Label(self.root,
# # # #                                     width=400,
# # # #                                     height=400,
# # # #                                     bg='#AAAAAA')
# # # #         self.frame1.pack()
# # # #
# # # #     # create menu
# # # #     def popup(self):
# # # #         self.popup_menu = tkinter.Menu(self.root,
# # # #                                        tearoff=0)
# # # #
# # # #         self.popup_menu.add_command(label="say hi",
# # # #                                     command=lambda: self.hey("hi"))
# # # #
# # # #         self.popup_menu.add_command(label="say hello",
# # # #                                     command=lambda: self.hey("hello"))
# # # #         self.popup_menu.add_separator()
# # # #         self.popup_menu.add_command(label="say bye",
# # # #                                     command=lambda: self.hey("bye"))
# # # #
# # # #     # display menu on right click
# # # #     def do_popup(self, event):
# # # #         try:
# # # #             self.popup_menu.tk_popup(event.x_root,
# # # #                                      event.y_root)
# # # #         finally:
# # # #             self.popup_menu.grab_release()
# # # #
# # # #     def hey(self, s):
# # # #         self.frame1.configure(text=s)
# # # #
# # # #     def run(self):
# # # #         self.popup()
# # # #         self.root.bind("<Button-3>", self.do_popup)
# # # #         tkinter.mainloop()
# # # #
# # # #
# # # # a = A()
# # # # a.run()
# # # #
# # #
# # # from tkinter import *
# # #
# # # root = Tk()
# # #
# # # w = Label(root, text="Right-click to display menu", width=40, height=20)
# # # w.pack()
# # #
# # # # create a menu
# # # popup = Menu(root, tearoff=0)
# # # popup.add_command(label="Next") # , command=next) etc...
# # # popup.add_command(label="Previous")
# # # popup.add_separator()
# # # popup.add_command(label="Home")
# # #
# # # def do_popup(event):
# # #     # display the popup menu
# # #     try:
# # #         popup.tk_popup(event.x_root, event.y_root, 0)
# # #     finally:
# # #         # make sure to release the grab (Tk 8.0a1 only)
# # #         popup.grab_release()
# # #
# # # w.bind("<Button-3>", do_popup)
# # #
# # # b = Button(root, text="Quit", command=root.destroy)
# # # b.pack()
# # #
# # # mainloop()
# #
# #
# # from tkinter import *
# #
# # root = Tk()
# #
# # w = Label(root, text="Right-click to display menu", width=40, height=20)
# # w.place(x=0)
# # f = None # Tracking F to see if it is None or not.
# #
# # def function1():
# #     global f
# #     print('function1 activated')
# #     # add this to the end of the function to destroy the frame and reset f
# #     if f != None:
# #         f.destroy()
# #         f = None
# #
# # def open_popup(event):
# #     global f
# #     # if f is None then create frame and button else don't
# #     if f == None:
# #         f = Frame(root,width=80,height=60,background='green')
# #         f.place(x=event.x, y=event.y)
# #         b2 = Button(f,text='function',command=function1)
# #         b2.pack()
# #     else:
# #         print("Can't open popup menu")
# #
# #
# # w.bind("<Button-3>", open_popup)
# # b = Button(root, text="Quit", command=root.destroy)
# # b.pack()
# #
# # root.mainloop()
# #
#
#
# from tkinter import *
#
# root = Tk()
#
# w = Label(root, text="Right-click to display menu", width=40, height=20)
# w.pack()
#
#
# def function1():
#     print('function1 activated')
#     try:
#         f.place_forget()
#     except:
#         pass
# # create a menu
# f = Frame(root,width=80,height=60,background='green')
# b2 = Button(f,text='function',command=function1)
# b2.place(x=0,y=5)
#
# def open_popup(event):
#     try:
#         f.place(x=event.x, y=event.y)
#         root.after(1)
#         f.focus_set()
#     except:
#         pass
#
# def close_popup(event):
#     try:
#         f.place_forget()
#         root.after(1)
#         w.unbind_all("<Button-1>")
#     except:
#         pass
#
# def enable_depopup(event):
#     w.bind_all("<Button-1>",close_popup)
#
# def disable_depopup(event):
#     w.unbind_all("<Button-1>")
#
# w.bind("<Button-3>", open_popup)
# w.bind("<Motion>", enable_depopup)
# f.bind("<Motion>", disable_depopup)
#
# b = Button(root, text="Quit", command=root.destroy)
# b.pack()
# root.mainloop()