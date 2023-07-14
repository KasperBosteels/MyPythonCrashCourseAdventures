from User_Class import User
from Privileges_Class import Privileges

class Admin(User):
    def __init__(self,first_name, last_name, age, location,privileges):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges(privileges)
