from tkinter import *

Window = Tk()
Window.title('ПР-14:Liana Kolodzheieva')
Window.geometry('600x400')
Window.resizable(0, 0)

def fun1(event):
    Window['bg'] = 'aqua'
    Lab = Label(Window, text='Ви натиснули на кнопку №1', font='Times 20', fg='blue')
    Lab.place(x=150, y=150)
    
def fun2(event):
    Window['bg'] = 'yellow'
    Lab = Label(Window, text='Ви натиснули на кнопку №2', font='Times 20', fg='green')
    Lab.place(x=150, y=150)


But1 = Button(Window, width=10, height=2, bg='violet', text='Kнoпка 1', fg='red', font='Times 12')
But1.place(x=40, y=250)
But1.bind('<Button-1>', fun1)

But2 = Button(Window, width=10, height=2, bg='violet', text='Kнoпка 2', fg='red', font='Times 12')
But2.place(x=400, y=250)
But2.bind('<Button-1>', fun2)

Window.mainloop()
