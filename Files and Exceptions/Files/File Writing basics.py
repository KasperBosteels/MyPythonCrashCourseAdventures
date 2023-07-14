filename = "programming.txt"
filepath = "../other_text_files/"
with open(filepath+filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

with open(filepath+filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")


username = input("What is your name? ")
with open(filepath+"guest.txt", 'w') as file_object:
    file_object.write(username)

while True:
    username = input("What is your name? ")
    if username == 'q':
        break
    else:
        with open(filepath+"guest_book.txt", 'a') as file_object:
            file_object.write(username+"\n")
            print("Hi "+username+", you've been added to the guest book!")

with open(filepath+"guest_book.txt", 'r') as file_object:
    for line in file_object:
        reason = input(f"{line.strip()} why do you like programming?")
        with open(filepath+"reasons.txt", 'a') as file_object:
            file_object.write(line+" like programming because: "+reason+"\n")