class Contact:

    def __init__(self, id, fullname, email, phone):
        self.id = id
        self.fullname = fullname
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Contact(id={self.id}, fullname={self.fullname}, email={self.email}, phone={self.phone})"