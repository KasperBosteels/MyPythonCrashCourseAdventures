person_i_know = {
    'name':'James',
    'username':'DistressforJames',
    'age':22
}
for k,v in person_i_know.items():
    print(f"{k}: {v}")

favoriteNumbers = {
    'William':3,
    "James":11,
    "Steve":35,
    "Fred":22
}
for k,v in favoriteNumbers.items():
    print(f"The favorite number of {k} is {v}")


programmingTerms = {
    'OOP':'object oriented programming is a way of developing software in a way that sees every piece of code as an object or maximum reusability.',
    'Polymorphisme':'is a term within OOP that describes the relation between inherited objects and how to structure them in development',
    'Refactoring':'Is the changing of code to fix bugs or more generally to implement changes in your code for a new context in your development enviroment',
    'stack':'Stack is the current technologies you are working with, or the current technologies you are knowledgable with.'
}
for k,v in programmingTerms.items():
    print(f"{k}\n{v}")