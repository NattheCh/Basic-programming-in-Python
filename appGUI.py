from tkinter import *

window = Tk()

window.title('Colour word')
window.geometry('200x150')
label = Label(window, text='Enter the word from colours'.center(50))
label.grid(column=0, row=0)
txt = Entry(window, width=20)
txt.grid(column=0, row=1)
pressButton = Button(window, text='Confirm')
pressButton.grid(column=0, row=2)

window.mainloop()