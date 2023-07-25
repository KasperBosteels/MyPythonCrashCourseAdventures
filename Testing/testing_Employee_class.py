import unittest
from employee_class import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.my_employee = Employee('John', 'Doe', 50000)

    def test_give_default_raise(self):
        pre_raise_salary = self.my_employee.salary
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, pre_raise_salary + 300)

    def test_give_custom_raise(self):
        pre_raise_salary = self.my_employee.salary
        self.my_employee.give_raise(1000)
        self.assertEqual(self.my_employee.salary, pre_raise_salary + 1000)

if __name__ == '__main__':
    unittest.main()