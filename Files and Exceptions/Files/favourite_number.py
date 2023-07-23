import json

try:
    with open ("../other_text_files/favourite_number.json") as f:
        favourite_number = json.load(f)
        print("I know your favourite number! It's " + str(favourite_number) + "!")
except FileNotFoundError:
    favourite_number = input("What is your favourite number? ")
    with open ("../other_text_files/favourite_number.json", 'w') as f:
        json.dump(favourite_number, f)
        print("We'll remember your favourite number is " + str(favourite_number) + "!")