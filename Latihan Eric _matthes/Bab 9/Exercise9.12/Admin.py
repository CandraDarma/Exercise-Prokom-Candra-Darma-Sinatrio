

from User import User       


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