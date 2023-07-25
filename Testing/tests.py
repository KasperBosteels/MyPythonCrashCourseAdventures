import unittest
from code_to_test1 import get_formatted_name, get_formatted_address
class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
class CityNamesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_address = get_formatted_address('santiago', 'chile')
        self.assertEqual(formatted_address, 'Santiago Chile')
    def test_city_country_population(self):
        formatted_address = get_formatted_address('santiago', 'chile', '5000000')
        self.assertEqual(formatted_address, 'Santiago Chile With A Total Of 5000000 People.')


if __name__ == '__main__':
    unittest.main()
