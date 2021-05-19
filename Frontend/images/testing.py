# # # # # # from tkinter import *
# # # # # #
# # # # # #
# # # # # # win=Tk()
# # # # # # win.geometry("1000x700")
# # # # # # win.configure(bg="white")
# # # # # #
# # # # # # a=Entry(win,bd=0, highlightthickness=0, relief='flat', bg="white")
# # # # # # a.config(highlightbackground="red",highlightcolor="red")
# # # # # # a.place(x=100,y=100)
# # # # # #
# # # # # # # b=LabelFrame(win,text="label", height=200, width=200,borderwidth=5, font=("arial",10, "bold"))
# # # # # # # b.config(highlightbackground="green")
# # # # # # # b.place(x=200,y=100)
# # # # # #
# # # # # # win.mainloop()
# # # # # # # from tkinter import *
# # # # # # # root = Tk()
# # # # # # # e = Entry(highlightthickness=2)
# # # # # # # e.config(highlightbackground = "red", highlightcolor= "red")
# # # # # # # e.pack()
# # # # # # # root.mainloop()
# # # # # #
# # # # #
# # # # #
# # # # # import tkinter as tk      # py2
# # # # # # import tkinter as tk    # py3
# # # # #
# # # # # class Example(tk.Frame):
# # # # #     def __init__(self, parent):
# # # # #         tk.Frame.__init__(self, parent)
# # # # #         f1 = GradientFrame(self, borderwidth=1, relief="sunken")
# # # # #         f2 = GradientFrame(self, "green", "blue", borderwidth=1, relief="sunken")
# # # # #         f1.pack(side="top", fill="both", expand=True)
# # # # #         f2.pack(side="bottom", fill="both", expand=True)
# # # # #
# # # # # class GradientFrame(tk.Canvas):
# # # # #     '''A gradient frame which uses a canvas to draw the background'''
# # # # #     def __init__(self, parent, color1="red", color2="black", **kwargs):
# # # # #         tk.Canvas.__init__(self, parent, **kwargs)
# # # # #         self._color1 = color1
# # # # #         self._color2 = color2
# # # # #         self.bind("<Configure>", self._draw_gradient)
# # # # #
# # # # #     def _draw_gradient(self, event=None):
# # # # #         '''Draw the gradient'''
# # # # #         self.delete("gradient")
# # # # #         width = self.winfo_width()
# # # # #         height = self.winfo_height()
# # # # #         limit = width
# # # # #         (r1,g1,b1) = self.winfo_rgb(self._color1)
# # # # #         (r2,g2,b2) = self.winfo_rgb(self._color2)
# # # # #         r_ratio = float(r2-r1) / limit
# # # # #         g_ratio = float(g2-g1) / limit
# # # # #         b_ratio = float(b2-b1) / limit
# # # # #
# # # # #         for i in range(limit):
# # # # #             nr = int(r1 + (r_ratio * i))
# # # # #             ng = int(g1 + (g_ratio * i))
# # # # #             nb = int(b1 + (b_ratio * i))
# # # # #             color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
# # # # #             self.create_line(i,0,i,height, tags=("gradient",), fill=color)
# # # # #         self.lower("gradient")
# # # # #
# # # # # if __name__ == "__main__":
# # # # #     root = tk.Tk()
# # # # #     Example(root).pack(fill="both", expand=True)
# # # # #     root.mainloop()
# # # #
# # # # from PIL import Image
# # # # img=Image.new('RGBA',(400,400))
# # # # for i in range(900):
# # # #     for j in range(900):
# # # #         img.putpixel((i,j),(255,200,154))a
# # # # img.show()
# # #
# # # # adapted from http://wiki.tcl.tk/%0920152
# # # import tkinter as tk
# # # from tkinter import ttk
# # #
# # # focusBorderImageData = '''
# # #     R0lGODlhQABAAPcAAHx+fMTCxKSipOTi5JSSlNTS1LSytPTy9IyKjMzKzKyq
# # #     rOzq7JyanNza3Ly6vPz6/ISChMTGxKSmpOTm5JSWlNTW1LS2tPT29IyOjMzO
# # #     zKyurOzu7JyenNze3Ly+vPz+/OkAKOUA5IEAEnwAAACuQACUAAFBAAB+AFYd
# # #     QAC0AABBAAB+AIjMAuEEABINAAAAAHMgAQAAAAAAAAAAAKjSxOIEJBIIpQAA
# # #     sRgBMO4AAJAAAHwCAHAAAAUAAJEAAHwAAP+eEP8CZ/8Aif8AAG0BDAUAAJEA
# # #     AHwAAIXYAOfxAIESAHwAAABAMQAbMBZGMAAAIEggJQMAIAAAAAAAfqgaXESI
# # #     5BdBEgB+AGgALGEAABYAAAAAAACsNwAEAAAMLwAAAH61MQBIAABCM8B+AAAU
# # #     AAAAAAAApQAAsf8Brv8AlP8AQf8Afv8AzP8A1P8AQf8AfgAArAAABAAADAAA
# # #     AACQDADjAAASAAAAAACAAADVABZBAAB+ALjMwOIEhxINUAAAANIgAOYAAIEA
# # #     AHwAAGjSAGEEABYIAAAAAEoBB+MAAIEAAHwCACABAJsAAFAAAAAAAGjJAGGL
# # #     AAFBFgB+AGmIAAAQAABHAAB+APQoAOE/ABIAAAAAAADQAADjAAASAAAAAPiF
# # #     APcrABKDAAB8ABgAGO4AAJAAqXwAAHAAAAUAAJEAAHwAAP8AAP8AAP8AAP8A
# # #     AG0pIwW3AJGSAHx8AEocI/QAAICpAHwAAAA0SABk6xaDEgB8AAD//wD//wD/
# # #     /wD//2gAAGEAABYAAAAAAAC0/AHj5AASEgAAAAA01gBkWACDTAB8AFf43PT3
# # #     5IASEnwAAOAYd+PuMBKQTwB8AGgAEGG35RaSEgB8AOj/NOL/ZBL/gwD/fMkc
# # #     q4sA5UGpEn4AAIg02xBk/0eD/358fx/4iADk5QASEgAAAALnHABkAACDqQB8
# # #     AMyINARkZA2DgwB8fBABHL0AAEUAqQAAAIAxKOMAPxIwAAAAAIScAOPxABIS
# # #     AAAAAIIAnQwA/0IAR3cAACwAAAAAQABAAAAI/wA/CBxIsKDBgwgTKlzIsKFD
# # #     gxceNnxAsaLFixgzUrzAsWPFCw8kDgy5EeQDkBxPolypsmXKlx1hXnS48UEH
# # #     CwooMCDAgIJOCjx99gz6k+jQnkWR9lRgYYDJkAk/DlAgIMICZlizat3KtatX
# # #     rAsiCNDgtCJClQkoFMgqsu3ArBkoZDgA8uDJAwk4bGDmtm9BZgcYzK078m4D
# # #     Cgf4+l0skNkGCg3oUhR4d4GCDIoZM2ZWQMECyZQvLMggIbPmzQIyfCZ5YcME
# # #     AwFMn/bLLIKBCRtMHljQQcDV2ZqZTRDQYfWFAwMqUJANvC8zBhUWbDi5YUAB
# # #     Bsybt2VGoUKH3AcmdP+Im127xOcJih+oXsEDdvOLuQfIMGBD9QwBlsOnzcBD
# # #     hfrsuVfefgzJR599A+CnH4Hb9fcfgu29x6BIBgKYYH4DTojQc/5ZGGGGGhpU
# # #     IYIKghgiQRw+GKCEJxZIwXwWlthiQyl6KOCMLsJIIoY4LlQjhDf2mNCI9/Eo
# # #     5IYO2sjikX+9eGCRCzL5V5JALillY07GaOSVb1G5ookzEnlhlFx+8OOXZb6V
# # #     5Y5kcnlmckGmKaaMaZrpJZxWXjnnlmW++WGdZq5ZXQEetKmnlxPgl6eUYhJq
# # #     KKOI0imnoNbF2ScFHQJJwW99TsBAAAVYWEAAHEQAZoi1cQDqAAeEV0EACpT/
# # #     JqcACgRQAW6uNWCbYKcyyEwGDBgQwa2tTlBBAhYIQMFejC5AgQAWJNDABK3y
# # #     loEDEjCgV6/aOcYBAwp4kIF6rVkXgAEc8IQZVifCBRQHGqya23HGIpsTBgSU
# # #     OsFX/PbrVVjpYsCABA4kQCxHu11ogAQUIOAwATpBLDFQFE9sccUYS0wAxD5h
# # #     4DACFEggbAHk3jVBA/gtTIHHEADg8sswxyzzzDQDAAEECGAQsgHiTisZResN
# # #     gLIHBijwLQEYePzx0kw37fTSSjuMr7ZMzfcgYZUZi58DGsTKwbdgayt22GSP
# # #     bXbYY3MggQIaONDzAJ8R9kFlQheQQAAOWGCAARrwdt23Bn8H7vfggBMueOEG
# # #     WOBBAAkU0EB9oBGUdXIFZJBABAEEsPjmmnfO+eeeh/55BBEk0Ph/E8Q9meQq
# # #     bbDABAN00EADFRRQ++2254777rr3jrvjFTTQwQCpz7u6QRut5/oEzA/g/PPQ
# # #     Ry/99NIz//oGrZpUUEAAOw==
# # # '''
# # #
# # # borderImageData = '''
# # #     R0lGODlhQABAAPcAAHx+fMTCxKSipOTi5JSSlNTS1LSytPTy9IyKjMzKzKyq
# # #     rOzq7JyanNza3Ly6vPz6/ISChMTGxKSmpOTm5JSWlNTW1LS2tPT29IyOjMzO
# # #     zKyurOzu7JyenNze3Ly+vPz+/OkAKOUA5IEAEnwAAACuQACUAAFBAAB+AFYd
# # #     QAC0AABBAAB+AIjMAuEEABINAAAAAHMgAQAAAAAAAAAAAKjSxOIEJBIIpQAA
# # #     sRgBMO4AAJAAAHwCAHAAAAUAAJEAAHwAAP+eEP8CZ/8Aif8AAG0BDAUAAJEA
# # #     AHwAAIXYAOfxAIESAHwAAABAMQAbMBZGMAAAIEggJQMAIAAAAAAAfqgaXESI
# # #     5BdBEgB+AGgALGEAABYAAAAAAACsNwAEAAAMLwAAAH61MQBIAABCM8B+AAAU
# # #     AAAAAAAApQAAsf8Brv8AlP8AQf8Afv8AzP8A1P8AQf8AfgAArAAABAAADAAA
# # #     AACQDADjAAASAAAAAACAAADVABZBAAB+ALjMwOIEhxINUAAAANIgAOYAAIEA
# # #     AHwAAGjSAGEEABYIAAAAAEoBB+MAAIEAAHwCACABAJsAAFAAAAAAAGjJAGGL
# # #     AAFBFgB+AGmIAAAQAABHAAB+APQoAOE/ABIAAAAAAADQAADjAAASAAAAAPiF
# # #     APcrABKDAAB8ABgAGO4AAJAAqXwAAHAAAAUAAJEAAHwAAP8AAP8AAP8AAP8A
# # #     AG0pIwW3AJGSAHx8AEocI/QAAICpAHwAAAA0SABk6xaDEgB8AAD//wD//wD/
# # #     /wD//2gAAGEAABYAAAAAAAC0/AHj5AASEgAAAAA01gBkWACDTAB8AFf43PT3
# # #     5IASEnwAAOAYd+PuMBKQTwB8AGgAEGG35RaSEgB8AOj/NOL/ZBL/gwD/fMkc
# # #     q4sA5UGpEn4AAIg02xBk/0eD/358fx/4iADk5QASEgAAAALnHABkAACDqQB8
# # #     AMyINARkZA2DgwB8fBABHL0AAEUAqQAAAIAxKOMAPxIwAAAAAIScAOPxABIS
# # #     AAAAAIIAnQwA/0IAR3cAACwAAAAAQABAAAAI/wA/CBxIsKDBgwgTKlzIsKFD
# # #     gxceNnxAsaLFixgzUrzAsWPFCw8kDgy5EeQDkBxPolypsmXKlx1hXnS48UEH
# # #     CwooMCDAgIJOCjx99gz6k+jQnkWR9lRgYYDJkAk/DlAgIMICkVgHLoggQIPT
# # #     ighVJqBQIKvZghkoZDgA8uDJAwk4bDhLd+ABBmvbjnzbgMKBuoA/bKDQgC1F
# # #     gW8XKMgQOHABBQsMI76wIIOExo0FZIhM8sKGCQYCYA4cwcCEDSYPLOgg4Oro
# # #     uhMEdOB84cCAChReB2ZQYcGGkxsGFGCgGzCFCh1QH5jQIW3xugwSzD4QvIIH
# # #     4s/PUgiQYcCG4BkC5P/ObpaBhwreq18nb3Z79+8Dwo9nL9I8evjWsdOX6D59
# # #     fPH71Xeef/kFyB93/sln4EP2Ebjegg31B5+CEDLUIH4PVqiQhOABqKFCF6qn
# # #     34cHcfjffCQaFOJtGaZYkIkUuljQigXK+CKCE3po40A0trgjjDru+EGPI/6I
# # #     Y4co7kikkAMBmaSNSzL5gZNSDjkghkXaaGIBHjwpY4gThJeljFt2WSWYMQpZ
# # #     5pguUnClehS4tuMEDARQgH8FBMBBBExGwIGdAxywXAUBKHCZkAIoEEAFp33W
# # #     QGl47ZgBAwZEwKigE1SQgAUCUDCXiwtQIIAFCTQwgaCrZeCABAzIleIGHDD/
# # #     oIAHGUznmXABGMABT4xpmBYBHGgAKGq1ZbppThgAG8EEAW61KwYMSOBAApdy
# # #     pNp/BkhAAQLcEqCTt+ACJW645I5rLrgEeOsTBtwiQIEElRZg61sTNBBethSw
# # #     CwEA/Pbr778ABywwABBAgAAG7xpAq6mGUUTdAPZ6YIACsRKAAbvtZqzxxhxn
# # #     jDG3ybbKFHf36ZVYpuE5oIGhHMTqcqswvyxzzDS/HDMHEiiggQMLDxCZXh8k
# # #     BnEBCQTggAUGGKCB0ktr0PTTTEfttNRQT22ABR4EkEABDXgnGUEn31ZABglE
# # #     EEAAWaeN9tpqt832221HEEECW6M3wc+Hga3SBgtMODBABw00UEEBgxdO+OGG
# # #     J4744oZzXUEDHQxwN7F5G7QRdXxPoPkAnHfu+eeghw665n1vIKhJBQUEADs=
# # # '''
# # #
# # # root = tk.Tk()
# # # style = ttk.Style()
# # # borderImage = tk.PhotoImage("borderImage", data=borderImageData)
# # # focusBorderImage = tk.PhotoImage("focusBorderImage", data=focusBorderImageData)
# # #
# # # style.element_create("RoundedFrame",
# # #                      "image", borderImage,
# # #                      ("focus", focusBorderImage),
# # #                      border=16, sticky="nsew")
# # # style.layout("RoundedFrame",
# # #              [("RoundedFrame", {"sticky": "nsew"})])
# # #
# # # frame1 = ttk.Frame(style="RoundedFrame", padding=10)
# # # text1 = tk.Text(frame1, borderwidth=0, highlightthickness=0, wrap="word",
# # #                 width=40, height=4)
# # # text1.pack(fill="both", expand=True)
# # #
# # # text1.bind("<FocusIn>", lambda event: frame1.state(["focus"]))
# # # text1.bind("<FocusOut>", lambda event: frame1.state(["!focus"]))
# # # text1.insert("end", "This widget has the focus")
# # #
# # # frame2 = ttk.Frame(style="RoundedFrame", padding=10)
# # # text2 = tk.Text(frame2, borderwidth=0, highlightthickness=0, wrap="word",
# # #                 width=40, height=4)
# # # text2.pack(fill="both", expand=True)
# # # text2.bind("<FocusIn>", lambda event: frame2.state(["focus"]))
# # # text2.bind("<FocusOut>", lambda event: frame2.state(["!focus"]))
# # # text2.insert("end", "This widget does not have the focus")
# # #
# # # root.configure(background="white")
# # # frame1.pack(side="top", fill="both", expand=True, padx=20, pady=20)
# # # frame2.pack(side="top", fill="both", expand=True, padx=20, pady=20)
# # #
# # # frame1.focus_set()
# # #
# # # root.mainloop()
# #
# #
# # """Ttk Frame with rounded corners.
# #
# # Based on an example by Bryan Oakley, found at: http://wiki.tcl.tk/20152"""
# # import tkinter
# # from tkinter import ttk
# #
# # root = tkinter.Tk()
# #
# # img1 = tkinter.PhotoImage("frameFocusBorder", data="""
# # R0lGODlhQABAAPcAAHx+fMTCxKSipOTi5JSSlNTS1LSytPTy9IyKjMzKzKyq
# # rOzq7JyanNza3Ly6vPz6/ISChMTGxKSmpOTm5JSWlNTW1LS2tPT29IyOjMzO
# # zKyurOzu7JyenNze3Ly+vPz+/OkAKOUA5IEAEnwAAACuQACUAAFBAAB+AFYd
# # QAC0AABBAAB+AIjMAuEEABINAAAAAHMgAQAAAAAAAAAAAKjSxOIEJBIIpQAA
# # sRgBMO4AAJAAAHwCAHAAAAUAAJEAAHwAAP+eEP8CZ/8Aif8AAG0BDAUAAJEA
# # AHwAAIXYAOfxAIESAHwAAABAMQAbMBZGMAAAIEggJQMAIAAAAAAAfqgaXESI
# # 5BdBEgB+AGgALGEAABYAAAAAAACsNwAEAAAMLwAAAH61MQBIAABCM8B+AAAU
# # AAAAAAAApQAAsf8Brv8AlP8AQf8Afv8AzP8A1P8AQf8AfgAArAAABAAADAAA
# # AACQDADjAAASAAAAAACAAADVABZBAAB+ALjMwOIEhxINUAAAANIgAOYAAIEA
# # AHwAAGjSAGEEABYIAAAAAEoBB+MAAIEAAHwCACABAJsAAFAAAAAAAGjJAGGL
# # AAFBFgB+AGmIAAAQAABHAAB+APQoAOE/ABIAAAAAAADQAADjAAASAAAAAPiF
# # APcrABKDAAB8ABgAGO4AAJAAqXwAAHAAAAUAAJEAAHwAAP8AAP8AAP8AAP8A
# # AG0pIwW3AJGSAHx8AEocI/QAAICpAHwAAAA0SABk6xaDEgB8AAD//wD//wD/
# # /wD//2gAAGEAABYAAAAAAAC0/AHj5AASEgAAAAA01gBkWACDTAB8AFf43PT3
# # 5IASEnwAAOAYd+PuMBKQTwB8AGgAEGG35RaSEgB8AOj/NOL/ZBL/gwD/fMkc
# # q4sA5UGpEn4AAIg02xBk/0eD/358fx/4iADk5QASEgAAAALnHABkAACDqQB8
# # AMyINARkZA2DgwB8fBABHL0AAEUAqQAAAIAxKOMAPxIwAAAAAIScAOPxABIS
# # AAAAAIIAnQwA/0IAR3cAACwAAAAAQABAAAAI/wA/CBxIsKDBgwgTKlzIsKFD
# # gxceNnxAsaLFixgzUrzAsWPFCw8kDgy5EeQDkBxPolypsmXKlx1hXnS48UEH
# # CwooMCDAgIJOCjx99gz6k+jQnkWR9lRgYYDJkAk/DlAgIMICZlizat3KtatX
# # rAsiCNDgtCJClQkoFMgqsu3ArBkoZDgA8uDJAwk4bGDmtm9BZgcYzK078m4D
# # Cgf4+l0skNkGCg3oUhR4d4GCDIoZM2ZWQMECyZQvLMggIbPmzQIyfCZ5YcME
# # AwFMn/bLLIKBCRtMHljQQcDV2ZqZTRDQYfWFAwMqUJANvC8zBhUWbDi5YUAB
# # Bsybt2VGoUKH3AcmdP+Im127xOcJih+oXsEDdvOLuQfIMGBD9QwBlsOnzcBD
# # hfrsuVfefgzJR599A+CnH4Hb9fcfgu29x6BIBgKYYH4DTojQc/5ZGGGGGhpU
# # IYIKghgiQRw+GKCEJxZIwXwWlthiQyl6KOCMLsJIIoY4LlQjhDf2mNCI9/Eo
# # 5IYO2sjikX+9eGCRCzL5V5JALillY07GaOSVb1G5ookzEnlhlFx+8OOXZb6V
# # 5Y5kcnlmckGmKaaMaZrpJZxWXjnnlmW++WGdZq5ZXQEetKmnlxPgl6eUYhJq
# # KKOI0imnoNbF2ScFHQJJwW99TsBAAAVYWEAAHEQAZoi1cQDqAAeEV0EACpT/
# # JqcACgRQAW6uNWCbYKcyyEwGDBgQwa2tTlBBAhYIQMFejC5AgQAWJNDABK3y
# # loEDEjCgV6/aOcYBAwp4kIF6rVkXgAEc8IQZVifCBRQHGqya23HGIpsTBgSU
# # OsFX/PbrVVjpYsCABA4kQCxHu11ogAQUIOAwATpBLDFQFE9sccUYS0wAxD5h
# # 4DACFEggbAHk3jVBA/gtTIHHEADg8sswxyzzzDQDAAEECGAQsgHiTisZResN
# # gLIHBijwLQEYePzx0kw37fTSSjuMr7ZMzfcgYZUZi58DGsTKwbdgayt22GSP
# # bXbYY3MggQIaONDzAJ8R9kFlQheQQAAOWGCAARrwdt23Bn8H7vfggBMueOEG
# # WOBBAAkU0EB9oBGUdXIFZJBABAEEsPjmmnfO+eeeh/55BBEk0Ph/E8Q9meQq
# # bbDABAN00EADFRRQ++2254777rr3jrvjFTTQwQCpz7u6QRut5/oEzA/g/PPQ
# # Ry/99NIz//oGrZpUUEAAOw==""")
# #
# # img2 = tkinter.PhotoImage("frameBorder", data="""
# # R0lGODlhQABAAPcAAHx+fMTCxKSipOTi5JSSlNTS1LSytPTy9IyKjMzKzKyq
# # rOzq7JyanNza3Ly6vPz6/ISChMTGxKSmpOTm5JSWlNTW1LS2tPT29IyOjMzO
# # zKyurOzu7JyenNze3Ly+vPz+/OkAKOUA5IEAEnwAAACuQACUAAFBAAB+AFYd
# # QAC0AABBAAB+AIjMAuEEABINAAAAAHMgAQAAAAAAAAAAAKjSxOIEJBIIpQAA
# # sRgBMO4AAJAAAHwCAHAAAAUAAJEAAHwAAP+eEP8CZ/8Aif8AAG0BDAUAAJEA
# # AHwAAIXYAOfxAIESAHwAAABAMQAbMBZGMAAAIEggJQMAIAAAAAAAfqgaXESI
# # 5BdBEgB+AGgALGEAABYAAAAAAACsNwAEAAAMLwAAAH61MQBIAABCM8B+AAAU
# # AAAAAAAApQAAsf8Brv8AlP8AQf8Afv8AzP8A1P8AQf8AfgAArAAABAAADAAA
# # AACQDADjAAASAAAAAACAAADVABZBAAB+ALjMwOIEhxINUAAAANIgAOYAAIEA
# # AHwAAGjSAGEEABYIAAAAAEoBB+MAAIEAAHwCACABAJsAAFAAAAAAAGjJAGGL
# # AAFBFgB+AGmIAAAQAABHAAB+APQoAOE/ABIAAAAAAADQAADjAAASAAAAAPiF
# # APcrABKDAAB8ABgAGO4AAJAAqXwAAHAAAAUAAJEAAHwAAP8AAP8AAP8AAP8A
# # AG0pIwW3AJGSAHx8AEocI/QAAICpAHwAAAA0SABk6xaDEgB8AAD//wD//wD/
# # /wD//2gAAGEAABYAAAAAAAC0/AHj5AASEgAAAAA01gBkWACDTAB8AFf43PT3
# # 5IASEnwAAOAYd+PuMBKQTwB8AGgAEGG35RaSEgB8AOj/NOL/ZBL/gwD/fMkc
# # q4sA5UGpEn4AAIg02xBk/0eD/358fx/4iADk5QASEgAAAALnHABkAACDqQB8
# # AMyINARkZA2DgwB8fBABHL0AAEUAqQAAAIAxKOMAPxIwAAAAAIScAOPxABIS
# # AAAAAIIAnQwA/0IAR3cAACwAAAAAQABAAAAI/wA/CBxIsKDBgwgTKlzIsKFD
# # gxceNnxAsaLFixgzUrzAsWPFCw8kDgy5EeQDkBxPolypsmXKlx1hXnS48UEH
# # CwooMCDAgIJOCjx99gz6k+jQnkWR9lRgYYDJkAk/DlAgIMICkVgHLoggQIPT
# # ighVJqBQIKvZghkoZDgA8uDJAwk4bDhLd+ABBmvbjnzbgMKBuoA/bKDQgC1F
# # gW8XKMgQOHABBQsMI76wIIOExo0FZIhM8sKGCQYCYA4cwcCEDSYPLOgg4Oro
# # uhMEdOB84cCAChReB2ZQYcGGkxsGFGCgGzCFCh1QH5jQIW3xugwSzD4QvIIH
# # 4s/PUgiQYcCG4BkC5P/ObpaBhwreq18nb3Z79+8Dwo9nL9I8evjWsdOX6D59
# # fPH71Xeef/kFyB93/sln4EP2Ebjegg31B5+CEDLUIH4PVqiQhOABqKFCF6qn
# # 34cHcfjffCQaFOJtGaZYkIkUuljQigXK+CKCE3po40A0trgjjDru+EGPI/6I
# # Y4co7kikkAMBmaSNSzL5gZNSDjkghkXaaGIBHjwpY4gThJeljFt2WSWYMQpZ
# # 5pguUnClehS4tuMEDARQgH8FBMBBBExGwIGdAxywXAUBKHCZkAIoEEAFp33W
# # QGl47ZgBAwZEwKigE1SQgAUCUDCXiwtQIIAFCTQwgaCrZeCABAzIleIGHDD/
# # oIAHGUznmXABGMABT4xpmBYBHGgAKGq1ZbppThgAG8EEAW61KwYMSOBAApdy
# # pNp/BkhAAQLcEqCTt+ACJW645I5rLrgEeOsTBtwiQIEElRZg61sTNBBethSw
# # CwEA/Pbr778ABywwABBAgAAG7xpAq6mGUUTdAPZ6YIACsRKAAbvtZqzxxhxn
# # jDG3ybbKFHf36ZVYpuE5oIGhHMTqcqswvyxzzDS/HDMHEiiggQMLDxCZXh8k
# # BnEBCQTggAUGGKCB0ktr0PTTTEfttNRQT22ABR4EkEABDXgnGUEn31ZABglE
# # EEAAWaeN9tpqt832221HEEECW6M3wc+Hga3SBgtMODBABw00UEEBgxdO+OGG
# # J4744oZzXUEDHQxwN7F5G7QRdXxPoPkAnHfu+eeghw665n1vIKhJBQUEADs=""")
# #
# # style = ttk.Style()
# #
# # style.element_create("RoundedFrame", "image", "frameBorder",
# #     ("focus", "frameFocusBorder"), border=16, sticky="nsew")
# #
# # style.layout("RoundedFrame", [("RoundedFrame", {"sticky": "nsew"})])
# # style.configure("TEntry", borderwidth=0)
# #
# # frame = ttk.Frame(style="RoundedFrame", padding=10)
# # frame.pack(fill='x')
# #
# # frame2 = ttk.Frame(style="RoundedFrame", padding=10)
# # frame2.pack(fill='both', expand=1)
# #
# # entry = ttk.Entry(frame, text='Test')
# # entry.pack(fill='x')
# # entry.bind("<FocusIn>", lambda evt: frame.state(["focus"]))
# # entry.bind("<FocusOut>", lambda evt: frame.state(["!focus"]))
# #
# # text = tkinter.Text(frame2, borderwidth=0, bg="white", highlightthickness=0)
# # text.pack(fill='both', expand=1)
# # text.bind("<FocusIn>", lambda evt: frame2.state(["focus"]))
# # text.bind("<FocusOut>", lambda evt: frame2.state(["!focus"]))
# #
# # root.mainloop()
#
#
# from tkinter import *
# from tkinter import font
#
# # root = Tk()
# # root.title('Font Families')
# # fonts=list(font.families())
# # fonts.sort()
# #
# # def populate(frame):
# #     '''Put in the fonts'''
# #     listnumber = 1
# #     for item in fonts:
# #         label = "listlabel" + str(listnumber)
# #         label = Label(frame,text=item,font=(item, 16)).pack()
# #         listnumber += 1
# #
# # def onFrameConfigure(canvas):
# #     '''Reset the scroll region to encompass the inner frame'''
# #     canvas.configure(scrollregion=canvas.bbox("all"))
# #
# # canvas = Canvas(root, borderwidth=0, background="#ffffff")
# # frame = Frame(canvas, background="#ffffff")
# # vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
# # canvas.configure(yscrollcommand=vsb.set)
# #
# # vsb.pack(side="right", fill="y")
# # canvas.pack(side="left", fill="both", expand=True)
# # canvas.create_window((4,4), window=frame, anchor="nw")
# #
# # frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
# #
# # populate(frame)
# #
# # root.mainloop()
#
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
#
# combostyle = ttk.Style()
#
# combostyle.theme_create('combostyle', parent='alt',
#                          settings = {'TCombobox':
#                                      {'configure':
#                                       {'selectbackground': 'blue',
#                                        'fieldbackground': 'red',
#                                        'background': 'green'
#                                        }}}
#                          )
# # ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
# combostyle.theme_use('combostyle')
#
# # show the current styles
# # print(combostyle.theme_names())
#
# combo = ttk.Combobox(root, values=['1', '2', '3'])
# combo['state'] = 'readonly'
# combo.pack()
#
# entry = tk.Entry(root)
# entry.pack()
#
# root.mainloop()

from tkinter import ttk
import tkinter
root = tkinter.Tk()

root.option_add("*TCombobox*Listbox*Background", 'green')

combo = ttk.Combobox().pack()
root.mainloop()