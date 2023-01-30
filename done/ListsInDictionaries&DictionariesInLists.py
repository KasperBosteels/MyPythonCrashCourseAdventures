person1 = {
    'name':"Kasper Bosteels",
    'age':24,
    'favColor':"green"
}
person2 = {
    'name':"James Doe",
    'age':22,
    "favColor":"pink"
}
person3 = {
    "name":"Danniele doe",
    "age":18,
    'favColor':"black"
}
friends = [person3,person2,person1]
for friend in friends:
    print("\n")
    for k,v in friend.items():
        print(f"{k}: {v}")

pet1 = {
    'species':"dog",
    'name':"Ruffles",
    "owner":"Garry"
}
pet2={
    'species':"parrot",
    'name':"Shaquila",
    'owner':"Ben"
}
pet3={
    'species':"cat",
    "name":"fanny",
    "owner":'fanny is her own boss'
}
pets =[pet3,pet2,pet1]
for pet in pets:
    print("\n")
    for k,v in pet.items():
        print(f"{k}: {v}")

favourite_places={
    'james':["market","saloon","store"],
    "Kasper":["cinema","bed","parties"],
    "Danniele":["home","cathouse","school"]
}

for k,v in favourite_places.items():

    print(f"\n{k}'s favorite places are:")
    for place in v:
        print(f"{place},")

cities = [
    { 'name':"Antwerp", 'fun fact':"Coke Capital of Europe"},
    {"name":"Amsterdam","fun fact":"Drug war raging"},
    {'name':"Kiev", 'fun fact':"Standing strong against the russians"}
]
for city in cities:
    print("\n")
    for k,v in city.items():
        print(f"{k}: {v}")