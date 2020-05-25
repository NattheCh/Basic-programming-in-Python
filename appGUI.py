from tkinter import *

window = Tk()


window.title('Colour word')
window.geometry('200x150')
label = Label(window, text='Enter the color - blue'.center(50))
label.grid(column=0, row=0)
txtColor = Entry(window, width=20)
txtColor.grid(column=0, row=1)
def clicked():
    if txtColor.get() == 'blue':
        label.configure(text='Button checked'.center(50))
    else:
        label.configure(text='Not correct'.center(50))


pressButton = Button(window, text='Confirm', command=clicked)
pressButton.grid(column=0, row=2)

window.mainloop()