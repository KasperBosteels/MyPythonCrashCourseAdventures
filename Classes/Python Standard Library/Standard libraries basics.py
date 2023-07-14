from random import randint,choice

class Die:
    def __init__(self):
        self.value = 6

    def roll_die(self):
        self.value = randint(1, 6)
        print(self.value)

die = Die()
for i in range(10):
    die.roll_die()


ticket = []
for i in range(10):
    ticket.append(randint(1, 100))
    if i <=4:
        ticket.append(choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']))
print(f"If you ticket contains {ticket} you won the lottery!")

counter = 0
myTicket = []

while myTicket != ticket:
    if counter >= 10000000:
        print("You will never win the lottery!")
        break
    counter += 1
    myTicket = []
    for i in range(10):
        myTicket.append(randint(1, 100))
        if i <=4:
            myTicket.append(choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']))

print(f"It took you {counter} tries to win the lottery!")