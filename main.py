
from tkinter import *


def add_numbers():
    res = int(e1.get()) + int(e2.get())
    myText.set(res)


def delete():
    e1.delete(0, END)
    e2.delete(0, END)


master = Tk()
myText = StringVar()
Label(master, text="First").grid(row=0, sticky=W)

Label(master, text="Second").grid(row=1, sticky=W)
Label(master, text="Result:").grid(row=3, sticky=W)
result = Label(master, text="", textvariable=myText).grid(row=3, column=1, sticky=W)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


b = Button(master, text="Add", command=add_numbers, bg='Green', fg='white')
b1 = Button(master, text="clear", command=delete, bg='Blue', fg='white')
b2 = Button(master, text="Exit", command=master.destroy, bg='Red', fg='white')
b.grid(row=5, column=1, sticky=W + E + N + S, padx=5, pady=5)
b1.grid(row=5, column=2, sticky=W + E + N + S, padx=5, pady=5)
b2.grid(row=5, column=3, sticky=W + E + N + S, padx=5, pady=5)

mainloop()
