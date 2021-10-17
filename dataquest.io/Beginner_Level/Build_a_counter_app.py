from tkinter import Label, Button, Tk
from tkinter import font


window = Tk()

window.geometry('500x500')

window.title("Counter")

window.count = 0

def increment():
    window.count += 1
    lbl.configure(text=window.count)


def reset():
    window.count = 0
    lbl.configure(text=window.count)


lbl = Label(window, text="0", font=("Apple Braille", 60))
lbl.grid(column=0, row=0)

btn1 = Button(window, text="Start", command=increment)
btn1.grid(column=0, row=1)

btn2 = Button(window, text="Reset", command=reset)
btn2.grid(column=1, row=1)

btn1['font'] = btn2['font'] = font.Font(size=30)

window.mainloop()