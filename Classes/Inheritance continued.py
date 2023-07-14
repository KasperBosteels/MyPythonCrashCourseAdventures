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

Robertos = IceCreamStand("Robertos", "Ice Cream")
Robertos.display_flavors()

class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print(f"First name: {self.first_name}\nLast name: {self.last_name}\nAge: {self.age}\nLocation: {self.location}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")

class Privileges:
    def __init__(self,privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f"Privileges: {self.privileges}")

class Admin(User):
    def __init__(self,first_name, last_name, age, location,privileges):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges(privileges)

new_admin = Admin("John", "Doe", 30, "New York", ["can add post", "can delete post", "can ban user"])
new_admin.describe_user()
new_admin.privileges.show_privileges()

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odomeater(self):
        print(f"This car has {self.odometer_reading} kilometers on it.")

    def update_odometer(self,kilometers):
        if kilometers > self.odometer_reading:
            self.odometer_reading = kilometers
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,kilometers):
        self.odometer_reading += kilometers

    def fill_gas_tank(self):
        print("This car needs a gas tank!")

class Battery:
    def __init__(self,battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} kilometers on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

class ElectricalCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

Tesla = ElectricalCar("Tesla","Model S",2020)
Tesla.battery.get_range()
Tesla.battery.upgrade_battery()
Tesla.battery.get_range()