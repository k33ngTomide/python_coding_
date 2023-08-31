from tkinter import *

root = Tk()

root.title = "Simple Calculator"

entry = Entry(root, width=50, borderwidth=7)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_add(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def button_clear():
    entry.delete(0, END)


f_num = 0


def button_add_number():
    first_number = entry.get()
    global f_num
    f_num = int(first_number)
    entry.delete(0, END)


def button_equals():
    second_number = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(f_num + int(second_number)))


button_1 = Button(root, text="1", pady=20, padx=40, command=lambda: button_add(1))
button_2 = Button(root, text="2", pady=20, padx=40, command=lambda: button_add(2))
button_3 = Button(root, text="3", pady=20, padx=40, command=lambda: button_add(3))
button_4 = Button(root, text="4", pady=20, padx=40, command=lambda: button_add(4))
button_5 = Button(root, text="5", pady=20, padx=40, command=lambda: button_add(5))
button_6 = Button(root, text="6", pady=20, padx=40, command=lambda: button_add(6))
button_7 = Button(root, text="7", pady=20, padx=40, command=lambda: button_add(7))
button_8 = Button(root, text="8", pady=20, padx=40, command=lambda: button_add(8))
button_9 = Button(root, text="9", pady=20, padx=40, command=lambda: button_add(9))
button_0 = Button(root, text="0", pady=20, padx=40, command=lambda: button_add(0))
button_adding = Button(root, text="+", pady=20, padx=40, command=lambda: button_add_number())
button_cleared = Button(root, text="Clear", pady=20, padx=85, command=button_clear)
button_equal = Button(root, text="=", pady=20, padx=99, command=lambda: button_equals())

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_adding.grid(row=5, column=0)
button_cleared.grid(row=5, column=1, columnspan=2)
button_equal.grid(row=4, column=1, columnspan=2)

root.mainloop()
