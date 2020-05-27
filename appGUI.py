from tkinter import *

window = Tk()
window.title('Color check')
window.geometry('250x150')
window.resizable(0, 0)
label = Label(window, text='Enter the color')
label.pack()

basicColors = ['blue', 'red', 'green']


def clicked():
    if txtColor.get() in basicColors:
        answer.set('CORRECT!')
        labelAnswer.config(fg=txtColor.get(), font='Arial 13 bold')
    elif txtColor.get() == '':
        answer.set('Fill in the field')
        labelAnswer.config(fg='red', font='Arial 13 bold')
    else:
        answer.set('Incorrect')
        labelAnswer.config(fg='red', font='Arial 13 bold')


txtColor = Entry(window, width=20)
txtColor.pack()

pressButton = Button(window, text='Confirm', command=clicked)
pressButton.pack()

answer = StringVar()
labelAnswer = Label(window, textvariable=answer)
labelAnswer.pack()

window.mainloop()