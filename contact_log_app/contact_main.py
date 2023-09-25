from tkinter import *
from tkinter import simpledialog, messagebox

from contact_log_app.contact import Contact
from contact_log_app.contact_log_impl import ContactLogImpl


def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter name")
    address = simpledialog.askstring("Add Contact", "Enter Address")
    email = simpledialog.askstring("Add Contact", "Enter E-mail")
    telephone = simpledialog.askstring("Add Contact", "Enter phone number")

    contact.set_name(name)
    contact.set_address(address)
    contact.set_email(email)
    contact.set_telephone(telephone)
    saved_contact = contact_space.save(contact)
    display_info("Contact Saved Successfully" + "\n" + str(saved_contact))


def display_info(message):
    messagebox.showinfo("Information", message)


def delete_contact():
    contact_id = simpledialog.askinteger("Delete Contact", "Enter Contact ID")
    found_contact = contact_space.find_by_id(contact_id)
    contact_space.delete(found_contact)
    display_info("Contact Deleted Successfully")

def update_contact():
    contact_id = simpledialog.askinteger("Update Contact", "Enter Contact ID")
    name = simpledialog.askstring("Update Contact", "Enter new name")
    address = simpledialog.askstring("Update Contact", "Enter new Address")
    email = simpledialog.askstring("Update Contact", "Enter new email")
    telephone = simpledialog.askstring("Update Contact", "Enter new phone number")

    updated_contact = Contact()
    updated_contact.set_contact_id(contact_id)
    updated_contact.set_name(name)
    updated_contact.set_address(address)
    updated_contact.set_email(email)
    updated_contact.set_telephone(telephone)

    new_updated_contact = contact_space.save(updated_contact)
    display_info("Contact Updated Successfully" + "\n" + str(new_updated_contact))


def find_contact():
    contact_id = simpledialog.askinteger("Find Contact", "Enter Contact ID")
    found_contact = contact_space.find_by_id(contact_id)
    display_info(str(found_contact))


def exit_contact():

    display_info("Thank you for using this app")
    root.destroy()


if __name__ == '__main__':

    contact = Contact()
    contact_space = ContactLogImpl()
    root = Tk()
    root.title("Contact Log")
    root.geometry("1000x500")

    root_label = Label(root, text="""CONTACT LOG
    We Keep your contact like it is ours""", font="Courier 25 bold")
    root_label.pack()

    add_contact = Button(root, text="Add Contact", padx=50, pady=20, font="Courier 15", command=add_contact)
    add_contact.pack(padx=50, pady=50)

    update_contact = Button(root, text="Update Contact", padx=50, pady=20, font="Courier 15", command=update_contact)
    update_contact.pack(padx=50, pady=50)

    delete_contact = Button(root, text="Delete Contact", padx=50, pady=20, font="Courier 15", command=delete_contact)
    delete_contact.pack(padx=50, pady=50)

    find_contact = Button(root, text="Find Contact", padx=50, pady=20, font="Courier 15", command=find_contact)
    find_contact.pack(padx=50, pady=50)

    exit_button = Button(root, text="Exit", padx=50, pady=20, font="Courier 15", command=exit_contact)
    exit_button.pack(padx=50, pady=50)

    root.mainloop()
