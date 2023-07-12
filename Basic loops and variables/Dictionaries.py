Person= {"eyes": 2, "language":"french","name":"David"}
print(Person)
People={
    "Jake":"fishing",
    "Timothy":"swimming",
    "Patric":"eating",
    "Alex":"footbal"
}
for key, value in People.items():
    print(f"the favourite activity of {key} is {value}")

for name in People.keys():
    print(name)

Rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states',
    'yangtze': 'china',
    'yellow': 'china',
    'mekong': 'vietnam',
    'congo': 'democratic republic of the congo',
    'amur': 'russia',
    'len': 'russia',
    'niger': 'nigeria',
}
for river, country in Rivers.items():
    print(f"The {river} runs through {country}")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}.")

people_to_poll = ["jen", "sarah", "edward", "phil", "kasper"]

for person in people_to_poll:
    if person in favorite_languages.keys():
        print(f"Thank you for taking the poll, {person.title()}.")
    else:
        print(f"{person.title()}, what's your favorite programming language?")

aliens = []
colors = ["green,","yellow","purpl","gray"]
speeds = ["slow","medium","fast"]
for alien_number in range(30):
    new_alien = {"color":colors[alien_number%4],"points":alien_number,"speed":[speeds[alien_number%3]]}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)