from tkinter import *
from PIL import Image,ImageTk
import random

class ConnectDatabase:
    def __init__(self,window):
        self.window = window
        self.window.geometry("1366x720+0+0")
        self.window.title("Database Connection Form")
        # self.window.iconbitmap('images/icon.ico')
        self.window.resizable(False,False)
        self.database_frame = ImageTk.PhotoImage\
            (file='images\\connect_database_frame.png')

        self.image_panel = Label(self.window,image=self.database_frame)
        self.image_panel.pack(fill='both',expand='yes')

        self.txt = "Connect Database Here"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d","#f29844", "red2"]
        self.heading = Label(self.window,text=self.txt, font=("yu gothic ui", 30, "bold"),bg="white",fg="black",bd=5,relief=FLAT)
        self.heading.place(x=470,y=40,width=450)
        self.slider()
        self.heading_color()

        #     ==================Declaring Labels


        # ==================Host Label and Entry==================
        self.host_label = Label(self.window,text="Host Name",bg="white",fg="#4f4e4d",font=("yu gothic ui", 13, "bold"))
        self.host_label.place(x=495, y=130)

        self.host_entry = Entry(self.window, relief=FLAT,bg = "white",fg ="#6b6a69",font=("yu gothic ui semibold", 12))
        self.host_entry.place(x=530,y=163,width=380)

        # ==================Port Label and Entry==================
        self.port_label = Label(self.window, text="Port", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
        self.port_label.place(x=495, y=225)

        self.port_entry = Entry(self.window, relief=FLAT, bg="white", fg="#6b6a69", font=("yu gothic ui semibold", 12))
        self.port_entry.place(x=530, y=253, width=380)

        # ==================Username Label and Entry==================
        self.username_label = Label(self.window, text="Username", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=495, y=318)

        self.username_entry = Entry(self.window, relief=FLAT, bg="white", fg="#6b6a69", font=("yu gothic ui semibold", 12))
        self.username_entry.place(x=530, y=348, width=380)

        # ==================Password Label and Entry==================
        self.password_label = Label(self.window, text="Password", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=495, y=410)

        self.password_entry = Entry(self.window, relief=FLAT, bg="white", fg="#6b6a69", font=("yu gothic ui semibold", 12))
        self.password_entry.place(x=530, y=440, width=380)

        #============Placing Button============

        self.submit = ImageTk.PhotoImage\
            (file='images\\submit.png')

        self.submit_button = Button(self.window,image=self.submit, relief = FLAT, borderwidth=0, background="white", activebackground="white", cursor="hand2")
        self.submit_button.place(x=500,y=520)

        self.login = ImageTk.PhotoImage \
            (file='images\\login.png')

        self.login_button = Button(self.window, image=self.login, relief=FLAT, borderwidth=0, background="white",
                                    activebackground="white", cursor="hand2")
        self.login_button.place(x=640, y=523)

        self.exit = ImageTk.PhotoImage \
            (file='images\\exit.png')

        self.exit_button = Button(self.window, image=self.exit, relief=FLAT, borderwidth=0, background="white",
                                    activebackground="white", cursor="hand2")
        self.exit_button.place(x=780, y=523)

    def slider(self):
        if self.count>=len(self.txt):
            self.count = -1
            self.text = ''
            self.heading.config(text=self.text)

        else:
            self.text = self.text+self.txt[self.count]
            self.heading.config(text=self.text)

        self.count+=1

        self.heading.after(100,self.slider)

    def heading_color(self):
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)












def win():
    window = Tk()
    ConnectDatabase(window)
    window.mainloop()

if __name__ == '__main__':
    win()

