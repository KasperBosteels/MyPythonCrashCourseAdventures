sandwichOrders = ["vegetarian","pastrami","croissant","panini","pastrami","meat","pastrami"]
finishedOrders = []
active= True

if "pastrami" in sandwichOrders:
    print("We are all out of pastrami.")
    while 'pastrami' in sandwichOrders:
        sandwichOrders.remove("pastrami")


while active:
    if len(sandwichOrders) == 0:
        break
    verification = input(f"Is {sandwichOrders[0]} finished [y/n]:")
    if verification == "y":
        currentSandwich = sandwichOrders.pop(0)
        finishedOrders.append(currentSandwich)
        continue
    else:
        continue
for sandwich in finishedOrders:
    print(sandwich + " was finished.")
active = True
Vacation=[]
while active:
    place = input("Where would you love to go on a vacation: ")
    Vacation.append(place)
    isContinue = input("Would you like to add another location: ")
    if isContinue == "y":
        continue
    else:
        break
for places in Vacation:
    print(places)