class User:
    """Membuat Profil Nama"""
    def __init__(self, firstName, LastName, PhoneNumber):
        self.firstName = firstName
        self.LastName = LastName
        self.PhoneNumber = PhoneNumber

    def describe_profil(self):
        fullName = f"{self.firstName.title()} {self.LastName.title()}"
        print(f"\nNama  : {fullName}")
        print(f"PhoneNumber : {self.PhoneNumber}")

    def greet_user(self):
         print(f"Halo, {self.firstName.title()}! Selamat datang kembali.")

user_1 = User("budi", "santoso", "083344227688")
user_2 = User("Candra", "Darma", "0895363607864")
user_3 = User("Valiant", "Darma", "081234567811")

for user in (user_1, user_2, user_3):
    user.describe_profil()
    user.greet_user()

        
