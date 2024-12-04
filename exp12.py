import tkinter as dev

from tkinter import messagebox

def onBtnClick():
    userInput = entry.get()
    messagebox.showwarning('Input', (f'You entered {userInput}'))

root = dev.Tk()
root.title('Simple GUI Application')
root.geometry('300x150')

label = dev.Label(root, text = 'Enter Kuch bhi')
label.pack(pady=10)

entry = dev.Entry(root, width=90)
entry.pack(pady=10)

button = dev.Button(root, text='Submit', command=onBtnClick)
button.pack(pady=10)

root.mainloop()