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


restaurant = Restaurant("Warung Sate Pak Slamet", "sate")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()