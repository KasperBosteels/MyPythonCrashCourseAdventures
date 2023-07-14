from Admin_Class import *
from Restaurant import IceCreamStand

new_admin = Admin("John", "Doe", 30, "New York", ["can add post", "can delete post", "can ban user"])
new_admin.describe_user()
new_admin.privileges.show_privileges()

Robertos = IceCreamStand("Robertos", "Ice Cream")
Robertos.display_flavors()
