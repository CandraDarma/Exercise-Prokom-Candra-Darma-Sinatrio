class Restaurant:
    """Model sederhana sebuah restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0          # nilai awal: belum ada pelanggan

    def describe_restaurant(self):
        print(f"{self.restaurant_name} menyajikan masakan "
              f"{self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka!")

    def set_number_served(self, number_served):
        """Atur jumlah pelanggan yang sudah dilayani."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Tambahkan jumlah pelanggan yang dilayani."""
        self.number_served += additional_served


restaurant = Restaurant("Warung Sate Pak Slamet", "sate")

print(f"Pelanggan dilayani: {restaurant.number_served}")

restaurant.number_served = 12               # ubah lewat atribut langsung
print(f"Pelanggan dilayani: {restaurant.number_served}")

restaurant.set_number_served(20)                    # ubah lewat method
print(f"Pelanggan dilayani: {restaurant.number_served}")

restaurant.increment_number_served(35)      # tambah 35 pelanggan
print(f"Pelanggan dilayani: {restaurant.number_served}")