
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nNama         : {self.restaurant_name}")
        print(f"Cuisine type : {self.cuisine_type}")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type="es krim"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanila", "cokelat", "stroberi"]

    def display_flavors(self):
        print(f"\nRasa yang tersedia di {self.restaurant_name}:")

        for flavor in self.flavors:
            print(f" {flavor}")



stand = IceCreamStand("Toko Es Krim Pak Alex")


stand.describe_restaurant()
stand.display_flavors()
