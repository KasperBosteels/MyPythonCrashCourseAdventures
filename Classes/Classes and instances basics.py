
class Restaurant:
    def __init__(self, name,type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restuarant(self):
        print(f"This restaurant is called {self.restaurant_name}\nand servs mainly {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

r = Restaurant("Gallipoli","italian")
r.open_restaurant()
r.describe_restuarant()
r2 = Restaurant("Herman","Asian")
r2.open_restaurant()
r2.describe_restuarant()
r3 = Restaurant("fish","american")
r3.open_restaurant()
r3.describe_restuarant()

