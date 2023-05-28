from tkinter import *

def sob():
    if var.get() == 1:
        Lb = Label (bg='red', text='червоний')
    if var.get() == 2:
        Lb = Label (bg='yellow', text='Жовтий')
    if var.get() == 3:
        Lb = Label (bg='green', tеxt='зелений')

        Lb.place(x=120, y=20, width=140, height=120)

window = Tk()
window.title('ПР-15:Ліана Колоджеєва')
window.geometry('400x200')
var = IntVar()

var1 = Radiobutton(text='червоний', variable=var, value=1, command=sob)
var1.place(x=20, y=20)

var2 = Radiobutton(text='Xовтий', variable=var, value=2, command=sob)
var2.place(x=20, y=60)

var3 = Radiobutton(text='зелений', variable=var, value=3, command=sob)
var3.place(x=20, y=100)

window.mainloop()
