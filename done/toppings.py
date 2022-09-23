requested_toppings = ["shrooms","pizza","beer","bears","beats","E-girls"]
available_topings= ["shrooms","waffles","beer","bears","beats"]

if requested_toppings:
    for requested_toppings in requested_toppings:
        if(requested_toppings not in available_topings):
            print(f"sorry we are all out of {requested_toppings}")
        else:
            print(f"adding {requested_toppings}.")
else:
    print("Are you sure you want a plain pizza?")

print("\nfinished creating your pizza!")
