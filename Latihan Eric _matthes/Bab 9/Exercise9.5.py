
class User:
    def __init__(self, firstName, LastName, PhoneNumber):
        self.firstName = firstName
        self.LastName = LastName
        self.PhoneNumber = PhoneNumber
        self.login_attempts = 0

    def describe_profil(self):
        fullName = f"{self.firstName.title()} {self.LastName.title()}"
        print(f"\nNama          : {fullName}")
        print(f"PhoneNumber   : {self.PhoneNumber}")

    def increment_login_attempts(self):
        """Tambah percobaan login sebanyak 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Kembalikan percobaan login ke 0."""
        self.login_attempts = 0


# Membuat objek User
user = User("budi", "santoso", "0895363607864")

user.describe_profil()

# Looping percobaan login
print("\n=== SISTEM LOGIN ===")
while True:
    pilihan = input("\nApakah ingin mencoba login? (y/n): ").lower()

    if pilihan == "y":
        user.increment_login_attempts()
        print(f"Percobaan login ke: {user.login_attempts}")

    elif pilihan == "n":
        break

    else:
        print("Pilihan tidak valid! Masukkan y atau n.")

# Menampilkan total percobaan login
print(f"\nTotal percobaan login: {user.login_attempts}")

# Reset login attempts
user.reset_login_attempts()
print(f"Percobaan login setelah reset: {user.login_attempts}")
