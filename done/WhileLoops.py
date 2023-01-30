topping = ""
selectedToppings=[]
while topping!="quit":
    topping = input("What topping would you like on your pizza: ")
    if topping == "quit":
        print("your pizza has the following toppings:")
        for spice in selectedToppings:
            print(spice)
        break
    else:
        selectedToppings.append(topping)
        continue

active = True
age = 0
while active:
    age = int(input("What is your age:"))
    if age <=10:
        print("You are free to go in.")
    if age <= 15:
        print("The price is 7.98 euro.")
    if age > 15:
        print("You pay fill price of 14 euro.")
        break