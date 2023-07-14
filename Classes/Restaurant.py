class Restaurant:
    def __init__(self, name,type):
        self.restaurant_name = name
        self.cuisine_type = type
        number_served = 0

    def set_number_served(self, number):
        self.number_served = number
    def increment_number_served(self, number):
        self.number_served += number

    def describe_restuarant(self):
        print(f"This restaurant is called {self.restaurant_name}\nand servs mainly {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

class IceCreamStand (Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ["vanilla", "chocolate", "strawberry", "mint"]

    def display_flavors(self):
        print(f"Flavors: {self.flavors}")
