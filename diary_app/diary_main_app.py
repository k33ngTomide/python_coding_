import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.simpledialog as simpledialog

from diary_app.diaries import Diaries
from diary_app.exceptions_list import *

diaries = Diaries()
username = ""
security_number = "0"


def create_account():

    try:
        user_input = simpledialog.askstring("Register", "Enter Username: ")
        password = simpledialog.askstring("Register", "Enter password: ")
        confirm_password = simpledialog.askstring("Register", "Confirm password: ")
        if password != confirm_password:
            raise IncorrectPasswordException("Password doesnot Match, try again")
        diaries.add(user_input, password)
        result_label.config(text="Diary created Successfully, proceed to login", font="Courier 10", fg="green")

    except (UsernameExistsException, IncorrectPasswordException, ValueError) as error:
        messagebox.showerror("Error Message", f"{error}")
        result_label.config(text=f"{error}", font="Courier 10", fg="red")


def log_in():
    global username

    try:

        user_input = simpledialog.askstring("Register", "Enter Username: ")
        password = simpledialog.askstring("Register", "Enter password: ")
        diaries.find_by_username(user_input).validate_password(password)
        username = user_input
        result_label.config(text="Login successful", font="Courier 10", fg="green")
        root.iconify()
        welcome()

    except (DiaryNotFoundException, IncorrectPasswordException) as error:
        result_label.config(text=f"{error}", font="Arial 10", fg="red")


def close_diary():
    root.destroy()


def welcome():
    def add_entry():
        try:
            title = simpledialog.askstring("Title", "Enter the title: ")
            body = simpledialog.askstring("Body", "Enter the body: ")

            diaries.find_by_username(username).create_entry(title, body)
        except DiaryNotFoundException as error:
            new_label.config(text=f"{error}", font="Arial 10", fg="red")

    def find_entry():
        try:
            entry_id = simpledialog.askstring("Find Entry", "Enter entry id number: ")
            diaries.find_by_username(username).findEntry(entry_id)

        except EntryNotFoundException as error:
            new_label.config(text=f"{error}", font="Arial 10", fg="red")

    def update_entry():

        try:
            entry_id = simpledialog.askstring("Update Entry", "Enter entry id number: ")
            title = simpledialog.askstring("Title", "Enter the title: ")
            body = simpledialog.askstring("Body", "Enter the body: ")
            diaries.find_by_username(username).update_entry(entry_id, title, body)
        except DiaryNotFoundException as error:
            new_label.config(text=f"{error}", font="Arial 10", fg="red")

    def delete_entry():
        entry_id = simpledialog.askstring("Delete Entry", "Enter entry id number: ")
        diaries.find_by_username(username).delete_entry(username)
    def lock_diary():
        global security_number

        sec_number = random.randint(10, 999)
        win.destroy()
        messagebox.showinfo("Security Number",
                            f"Your security number is {sec_number}")
        security_number = str(sec_number)
        locked()

    def exit_diary():
        win.destroy()
        root.destroy()
        exit(1)

    win = tk.Tk()
    win.title("Diary Main Page")
    win.geometry("750x750")
    new_label = Label(win, text=" Welcome to your Diary", font="Courier 18 bold")
    new_label.pack(pady=20, padx=25)
    add_entry = Button(win, pady=30, padx=30, text="Add Entry", command=add_entry)
    add_entry.pack()
    find_entry = Button(win, pady=30, padx=30, text="Find Entry", command=find_entry)
    find_entry.pack()
    update_entry = Button(win, pady=30, padx=30, text="Update Entry", command=update_entry)
    update_entry.pack()
    delete_entry = Button(win, pady=30, padx=30, text="Delete Entry", command=delete_entry)
    delete_entry.pack()
    lock = Button(win, pady=30, padx=30, text="Lock Diary", command=lock_diary)
    lock.pack()
    exit_diary = Button(win, pady=30, padx=30, text="Close Diary", command=exit_diary)
    exit_diary.pack()


def locked():
    global username, security_number
    diaries.find_by_username(username).lock_diary()

    def unlock():
        try:
            password = simpledialog.askstring("Unlock", "Enter password: ")

            diaries.find_by_username(username).validate_password(password)
            secure = simpledialog.askstring("Unlock", "Enter Security Number: ")

            if security_number != secure:
                raise SecurityNumberException("Incorrect Security Number")

            welcome()
            new_root.destroy()
        except (IncorrectPasswordException, SecurityNumberException) as error:
            unlock_button_label.config(text=f"{error}", font="Arial 10", fg="red")

    new_root = tk.Tk()
    new_root.title("Unlock Diary")

    new_root.geometry("300x300")

    new_root_label = Label(new_root, text="Diary is Locked \nUnlock to access Diary", font="Courier 12 bold")
    new_root_label.pack()

    unlock_button = Button(new_root, pady=30, padx=30, text="Unlock",
                           command=unlock, font="Courier 12 bold")
    unlock_button.pack()
    unlock_button_label = Label(new_root, text="", font=("Arial", 14))
    unlock_button_label.pack()


root = tk.Tk()
root.title("Chronicle Diary")

root.geometry("750x750")

label = Label(root, text="""Hi, Welcome to Chronicle Diary.
Chronicle helps you document your
day-to-day experiences,social commentary,
complaints, poems, prose, illicit thoughts
and contents.""", font="Courier 12 bold")
label.pack(pady=20, padx=25)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

create_button = Button(root, pady=30, padx=30, text="Create Diary Account",
                       command=create_account, font="Courier 12 bold")
create_button.pack()
login = Button(root, pady=30, padx=30, text="Log in", command=log_in, font="Courier 12 bold")
login.pack()
close_button = Button(root, pady=30, padx=30, text="Close", command=close_diary, font="Courier 12 bold")
close_button.pack()

root.mainloop()
