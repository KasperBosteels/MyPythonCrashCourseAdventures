
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

r = Restaurant("Gallipoli","italian")
r.open_restaurant()
r.describe_restuarant()
r.number_served = 10
print(r.number_served)
r.set_number_served(20)
print(r.number_served)
r.increment_number_served(12)
print(r.number_served)
r2 = Restaurant("Herman","Asian")
r2.open_restaurant()
r2.describe_restuarant()
r3 = Restaurant("fish","american")
r3.open_restaurant()
r3.describe_restuarant()