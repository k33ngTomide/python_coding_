

class Contact:
    def __init__(self):
        self.contact_id = 0
        self.name = ""
        self.address = ""
        self.telephone = ""
        self.email = ""

    def get_contact_id(self):
        return self.contact_id

    def set_contact_id(self, contact_id):
        self.contact_id = contact_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_telephone(self):
        return self.telephone

    def set_telephone(self, telephone):
        self.telephone = telephone

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Contact):
            return False
        return (self.contact_id == other.contact_id and
                self.name == other.name and
                self.address == other.address and
                self.telephone == other.telephone and
                self.email == other.email)

    def __str__(self):
        stars = '^' * 30
        return f"""
           {stars}
           Contact Id: {self.get_contact_id()}
           Contact Name: {self.get_name()}
           Address: {self.get_address()}
           Telephone: {self.get_telephone()}
           E-mail: {self.get_email()}
           {stars}"""
