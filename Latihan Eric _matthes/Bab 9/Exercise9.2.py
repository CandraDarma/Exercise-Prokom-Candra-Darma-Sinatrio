class Restaurant:
    """Model sederhana sebuah restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        """Simpan nama restoran dan jenis masakannya."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Tampilkan nama restoran dan jenis masakannya."""
        print(f"{self.restaurant_name} menyajikan masakan "
              f"{self.cuisine_type}.")

    def open_restaurant(self):
        """Tampilkan pesan bahwa restoran sedang buka."""
        print(f"{self.restaurant_name} sedang buka!")


restaurant_1= Restaurant("Warung Sate Pak Slamet", "sate")
restaurant_2= Restaurant("Warung Bakso Pal Alex", "Bakso")
restaurant_3= Restaurant("Warung Nasi Goreng Pak Bagong", "Nasi Goreng")

print(restaurant_1.restaurant_name)
print(restaurant_2.restaurant_name)
print(restaurant_3.restaurant_name)
print(restaurant_1.cuisine_type)
print(restaurant_2.cuisine_type)
print(restaurant_3.cuisine_type)
