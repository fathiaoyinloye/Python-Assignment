class Guest:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email


    def set_name(self, guest_name):
            self.name = guest_name
    def set_phone_number(self, phone_number):
            self.phone_number = phone_number
    def set_email(self, email):
            self.email = email

    def get_name(self):
            return self.name
    def get_phone_number(self):
            return self.phone_number
    def get_email(self):
            return self.email
