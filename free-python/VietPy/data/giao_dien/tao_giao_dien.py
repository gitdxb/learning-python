from tkinter import *

window=Tk()

window.wm_title("Quét email die")

my_label = Label(window, text = "Nhập hotmail:   ")
my_label.grid(row = 0, column = 0)
hotmail = Entry(window)
hotmail.grid(row = 0, column = 1)

def hotmail():
    print("2")
b1=Button(window,text="  Random Mail", width=10, height=2, command=hotmail)
b1.grid(row=0,column=2)



window.mainloop()