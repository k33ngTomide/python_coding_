from tkinter import simpledialog, messagebox

from contact_log_app.contact import Contact
from contact_log_app.contact_log_impl import ContactLogImpl


class ContactControllerTkinter:
    def __init__(self, master):
        self.contactLog = ContactLogImpl()

        self.master = master
        self.master.title("Contact Management App")

        # Create and place widgets here

    def welcome_contact(self):
        options = [
            "Add Contact",
            "Update Contact",
            "Delete Contact",
            "Find Contact",
            "Exit"
        ]

        user_input = simpledialog.askinteger("Welcome", "Enter option (1-5)", minvalue=1, maxvalue=5)

        if user_input == 1:
            self.add_contact()
        elif user_input == 2:
            self.update_contact()
        elif user_input == 3:
            self.delete_contact()
        elif user_input == 4:
            self.find_contact()
        elif user_input == 5:
            self.exit_app()
        else:
            self.display_info("Invalid Input, try again.")
            self.welcome_contact()

    def exit_app(self):
        self.display_info("Thank you for using this app")
        self.master.destroy()

    def find_contact(self):
        contact_id = simpledialog.askinteger("Find Contact", "Enter Contact ID")
        found_contact = self.contactLog.find_by_id(contact_id)
        self.display_info(str(found_contact))

    def delete_contact(self):
        contact_id = simpledialog.askinteger("Delete Contact", "Enter Contact ID")
        found_contact = self.contactLog.find_by_id(contact_id)
        self.contactLog.delete(found_contact)
        self.display_info("Contact Deleted Successfully")

    def update_contact(self):
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

        new_updated_contact = self.contactLog.save(updated_contact)
        self.display_info("Contact Updated Successfully" + "\n" + str(new_updated_contact))

    def add_contact(self):
        name = simpledialog.askstring("Add Contact", "Enter name")
        address = simpledialog.askstring("Add Contact", "Enter Address")
        email = simpledialog.askstring("Add Contact", "Enter E-mail")
        telephone = simpledialog.askstring("Add Contact", "Enter phone number")

        contact = Contact()
        contact.set_name(name)
        contact.set_address(address)
        contact.set_email(email)
        contact.set_telephone(telephone)
        saved_contact = self.contactLog.save(contact)
        self.display_info("Contact Saved Successfully" + "\n" + str(saved_contact))

    def display_info(self, message):
        messagebox.showinfo("Information", message)
