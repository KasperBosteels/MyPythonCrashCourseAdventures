car = input("what kind of car would you like to rent: ")
print(f"Let me see if i can find a {car} for you.")

amount = input("How many people are in your dinner group: ")
if int(amount)>8:
    print("You will have to wait for a table large enough.")
else:
    print("Your table is ready.")

multipleoften = input("your number: ")
if int(multipleoften) % 10 ==0:
    print("That number is a multiple of ten")
else:
    print("That number is not a multiple of ten")