name = ["Dani","William","Kaiser","Ducc"]
print(f"this is the name of a person {name[1].title()}")
name[1] = "merian webster".title()
print("changing wiliams name now...")
print(name)
name.append(" Koran waifu ")
print(name[4].lstrip().rstrip().title())
name.insert(3,"Sasha Grey")
print(name[3])
del name[0]
print(name)
print(name.pop())
print(name)
name.remove("Ducc")
print(name)


#guest list
guests = ["albert Einstein","the Little Mermaid","King leopold 1"]
print(f"Ayo smart man {guests[0].title()} git over here i got dem foods...")
print(f"get yo butt over here {guests[1].lower()}")
print(f"{guests[2].title()} i got dunkin' donuts")
print(f"{guests[1].lower()} can't come anymore cus not a mermaid")
print("ill invite boba fet instead")
guests[1] = "Boba fet"
guests.sort(reverse=False);
print(guests)
exit()