with open('../pi_digits.txt') as file_object:
    contents = file_object.read().rstrip()
    print(contents)
    print(len(contents))

with open('../pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

with open ('../other_text_files/pi.txt') as pi_object:
    pi_string = pi_object.read().rstrip()
    dob = len(input("what is your birthyear:"))
    if str(dob) in pi_string:
        print("Your birthday appears in the first million digits of pi!")
    else:
        print("Your birthday does not appear in the first million digits of pi.")

