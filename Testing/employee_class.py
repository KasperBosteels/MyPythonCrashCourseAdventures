class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = ''
        self.last_name = ''
        self.salary = 0
        self.email = ''

    def give_raise(self, amount = 300):
        self.salary += amount
        return self.salary
