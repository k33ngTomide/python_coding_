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
            raise IncorrectPasswordException("Password doesn't Match, try again")
        diaries.add(user_input, password)
        result_label.config(text="Diary created Successfully, proceed to login", font="Courier 15", fg="green")

    except (UsernameExistsException, IncorrectPasswordException, ValueError) as error:
        messagebox.showerror("Error Message", f"{error}")
        result_label.config(text=f"{error}", font="Courier 15 bold", fg="red")


def log_in():
    global username

    try:

        user_input = simpledialog.askstring("Log in", "Enter Username: ")
        password = simpledialog.askstring("Log in", "Enter password: ")

        diaries.find_by_username(user_input).validate_password(password)
        username = user_input
        result_label.config(text="Login successful", font="Courier 15", fg="green")
        root.iconify()
        welcome()

    except (DiaryNotFoundException, IncorrectPasswordException) as error:
        result_label.config(text=f"{error}", font="Arial 15 bold", fg="red")


def close_diary():
    root.destroy()


def add_entry_extension():
    new_entry = Tk()
    new_entry.title("Add Entry")

    entry = Entry(new_entry, width=60)
    entry.pack()

    new_widget = Text(new_entry, width=60, height=15, borderwidth=6)
    new_widget.pack()

    def save_entry():
        title = entry.get()
        body = new_widget.get("1.0", "end-1c")

        diaries.find_by_username(username).create_entry(title, body)
        # registered.save_entry(user_id, title, body)
        new_entry.destroy()
        messagebox.showinfo("Entry Id ", f"Your Entry Id is "
                                         f"{diaries.find_by_username(username).get_number_of_entries()}")

    save_button = Button(new_entry, text="Save entry", command=save_entry)
    save_button.pack()

    add_entry_label = Label(new_entry, text="")
    add_entry_label.pack()


def welcome():
    def add_entry():

        try:
            add_entry_extension()

        except DiaryNotFoundException as error:
            new_label.config(text=f"{error}", font="Arial 10 bold", fg="red")

    def find_entry():
        try:
            entry_id = simpledialog.askstring("Find Entry", "Enter entry id number: ")

            entry_details = (diaries.find_by_username(username).findEntry(entry_id).get_entry_details())
            messagebox.showinfo("Entry Detail", f"{entry_details}")

        except (EntryNotFoundException, DiaryNotFoundException) as error:
            new_label.config(text=f"{error}", font="Arial 15 bold", fg="red")

    def update_entry():

        entry_id = simpledialog.askstring("Update Entry", "Enter entry id number: ")
        new_entry = Tk()
        new_entry.title("Update Entry")

        entry = Entry(new_entry, width=60)
        entry.pack()

        new_widget = Text(new_entry, width=60, height=15, borderwidth=6)
        new_widget.pack()

        def save_entry():
            title = entry.get()
            body = new_widget.get("1.0", "end-1c")

            try:
                diaries.find_by_username(username).update_entry(entry_id, title, body)
                new_entry.destroy()
            except (DiaryNotFoundException, EntryNotFoundException) as error:
                new_label.config(text=f"{error}", font="Arial 15 bold", fg="red")

        save_button = Button(new_entry, text="Save Update", command=save_entry)
        save_button.pack()

        add_entry_label = Label(new_entry, text="")
        add_entry_label.pack()

    def delete_entry():

        try:
            entry_id = simpledialog.askstring("Delete Entry", "Enter entry id number: ")
            diaries.find_by_username(username).delete_entry(entry_id)

            messagebox.showinfo("Delete Entry", "Deleting entry... \nDeleted Successfully")

        except (DiaryNotFoundException, EntryNotFoundException) as error:
            new_label.config(text=f"{error}", font="Arial 15 bold", fg="red")

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

    def view_entry():
        global username
        try:
            password = simpledialog.askstring("View All Entries", "Enter password: ")

            diaries.find_by_username(username).validate_password(password)
            every_entry = diaries.find_by_username(username).view_all_entries()
            messagebox.showinfo("All Entries", f"{every_entry}")

        except (EntryNotFoundException, DiaryNotFoundException, IncorrectPasswordException) as error:
            new_label.config(text=f"{error}", font="Arial 15 bold", fg="red")

    win = tk.Tk()

    win.title("Diary Main Page")
    win.geometry("750x750")

    new_label = Label(win, text="Welcome to your Diary", font="Courier 18 bold")
    new_label.pack(pady=20, padx=25)

    add_entry = Button(win, pady=30, padx=30, text="Add Entry", command=add_entry)
    add_entry.pack()

    find_entry = Button(win, pady=30, padx=30, text="Find Entry", command=find_entry)
    find_entry.pack()

    update_entry = Button(win, pady=30, padx=30, text="Update Entry", command=update_entry)
    update_entry.pack()

    view_entry = Button(win, pady=30, padx=30, text="View All Entries", command=view_entry)
    view_entry.pack()

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

            diaries.find_by_username(username).unlock_diary(password)

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
