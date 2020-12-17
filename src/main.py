from tkinter import *
import os

def confirm():
    os.system(f'shutdown -s -t {txt.get()}')

def cancel():
    os.system('shutdown -a')
    
window = Tk()
window.title("PC Выключатор")
lbl = Label(window, text="Введи время до выключения в секундах")
lbl.grid(column=0, row=0)
txt = Entry(window,width=40)
txt.grid(column=0, row=1)
btn1 = Button(window, text="ОK!", command=confirm)
btn1.grid(column=0, row=2)
btn2 = Button(window, text="Cancel!", command=cancel)
btn2.grid(column=0, row=3)
window.mainloop()
