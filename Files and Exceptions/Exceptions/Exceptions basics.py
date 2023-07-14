try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    number_one = input("First number: ")
    if number_one == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(number_one) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

try:
    with open("cats.txt", encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print("File not found!")
else:
    print(contents)