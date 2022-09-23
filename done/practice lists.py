usernames = ["1","2","3,","4","5","5","6","6",",6","7","788","989","admin"]

if(usernames):
    for username in usernames:
        if(username == "admin"):
            print("Hello admin")
        else:
            print(f"greetings {username}")
else:
    print("list is empty")
#//////////////////////////////////////////////////////////////////////
current_users = ["Jan","Jaap","Gert","Tomas","Jeremy","Eric"]
new_users = ["Gregory","Frans","Clarkson","Gert","Bert"]
current_users_lower = []
for current_user in current_users:
    current_users_lower.append(current_user.lower())
for new_user in new_users:
    if(new_user.lower() in current_users_lower):
        print(f"this username is already taken '{new_user}'")
    else:
        print(f"{new_user} is available for you")

#///////////////////////////////////////////
numbers= [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    if(number > 3):
        print(f"{number}th")
    elif(number < 3):
        print(f"{number}st")
    else:
        print(f"{3}rd")

