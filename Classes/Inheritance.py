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


class ElectricalCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")


tesla = ElectricalCar("tesla","model s",2019)
print(tesla.get_descriptive_name())
tesla.battery.describe_battery()
tesla.battery.get_range()
tesla.fill_gas_tank()

ferrari = Car("ferrari","f40",1990)
print(tesla.get_descriptive_name())
ferrari.fill_gas_tank()

