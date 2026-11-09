class User:

    def __init__(self, first_name, last_name, location, occupation, email):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.occupation= occupation
        self.email= email

    def describe_user(self):
        fullName = f"{self.first_name} {self.last_name}"
        print(f"\nNama : {fullName}")
        print(f"lokasi : {self.location}")
        print(f"perihal : {self.occupation}")
        print(f"Email : {self.email}")




class Privileges:
    """Kumpulan hak akses seorang administrator."""

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Tampilkan daftar hak akses."""
        print("Hak akses administrator:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Administrator: jenis khusus dari User."""

    def __init__(self, first_name, last_name, location, occupation, email):
        super().__init__(first_name, last_name, location, occupation, email)
        self.privileges = Privileges()  # instance sebagai atribut


admin = Admin("Candra", "Darma","Salatiga", "admin forum", "candradarma@gmail.com")
admin.describe_user()
admin.privileges.show_privileges()