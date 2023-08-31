import tkinter as tk
from tkinter import *
from tkinter import messagebox


def show_message():
    messagebox.showinfo("Info", "This is an information message.")


def show_error():
    messagebox.showerror("Error", "An error occurred!")


def show_warning():
    messagebox.showwarning("Warning", "This is a warning message.")


root = tk.Tk()
root.title("PyCharm JOptionPane Example")

info_button = tk.Button(root, text="Show Info", command=show_message, padx=50, pady=20, background="blue",fg= "white")
info_button.pack()

e = Entry(root, width=60)

error_button = tk.Button(root, text="Show Error", command=show_error, padx=50, pady=20, bg="black", fg= "green")
error_button.pack()

warning_button = tk.Button(root, text="Show Warning", command=show_warning, padx=50, pady=20, bg="red", fg= "white" )
warning_button.pack()

root.mainloop()
