class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} sits...")

    def roll_over(self):
        print(f"{self.name} rolls over...")

my_dog = Dog("Attenburough", 11)
my_dog.sit()
my_dog.roll_over()
my_dog.sit()

your_dog = Dog("Jeremiah", 7)
your_dog.sit()
your_dog.roll_over()
your_dog.sit()