from tkinter import *
from time import strftime


window = Tk()

window.geometry('1500x1500')
window.state('zoomed')
window.resizable(0, 0)

window.title("Alarm Clock")

window.configure(background='black')

def get_time():
    """Updates the label with the current time every 1 second."""
    current_time = strftime("%H : %M : %S %p")
    lbl.configure(text=current_time)
    lbl.after(1000, get_time)


def show_alarm_entry():
    """Shows Alarm entry box"""
    text = Entry(window)
    text.pack(side=LEFT, padx=10, pady=10, anchor=SW)


# def alarm(text.get()):
#     """Alarm function"""



lbl = Label(window, font=("Apple Braille", 60), bg='black', fg='white')
lbl.pack(side=TOP, pady=190, anchor=CENTER)

alarm_btn = Button(window, text='Alarm', bg="grey", fg='white', width=71, height=10, command=show_alarm_entry)
alarm_btn.pack(side=LEFT, padx=50, pady=100, anchor=SW)

snooze_btn = Button(window, text="Snooze", bg="grey", fg='white', width=71, height=10)
snooze_btn.pack(side=RIGHT, padx=50, pady=100, anchor=SE)


get_time()

window.mainloop()
