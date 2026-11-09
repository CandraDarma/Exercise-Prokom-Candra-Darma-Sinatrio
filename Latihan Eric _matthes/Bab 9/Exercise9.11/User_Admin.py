

class User:
  

    def __init__(self, first_name, last_name, location, occupation, email):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.occupation = occupation
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"\nNama      : {full_name}")
        print(f"Lokasi    : {self.location.title()}")
        print(f"Pekerjaan : {self.occupation}")
        print(f"Email     : {self.email}")


class Privileges:
  

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Hak akses administrator:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
  

    def __init__(self, first_name, last_name, location, occupation, email):
        super().__init__(first_name, last_name, location, occupation, email)
        self.privileges = Privileges()