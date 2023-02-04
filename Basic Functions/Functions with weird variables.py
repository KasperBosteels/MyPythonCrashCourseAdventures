

def make_sandwich (*ingredients):
    for ingredient in ingredients:
        print(f"your sandwich will contain {ingredient}")

make_sandwich("tomate","salad","cucumber","mayo")

user_profile = {
    "name":"Kasper",
    "lastname":"Bosteels",
    "loves":"Javascript",
    "age":24,
    "color":"green"
}
def build_user (firstname,lastname,**profile_info):
     profile_info["firstname"]= firstname
     profile_info["lastname"] = lastname
     return profile_info

newUser = build_user("Kasper","Bosteels",favourite_color="green", loves="food and sleeping")
print (newUser)

all_cars = []
def build_car (model,manufacturer,**car_details):
    car_details["model"]=model
    car_details["manufacturer"]=manufacturer
    all_cars.append(car_details)
    return all_cars

new_carList = build_car("Astra","Opel",hp=600,safety="failed",EV=False)
print (new_carList)