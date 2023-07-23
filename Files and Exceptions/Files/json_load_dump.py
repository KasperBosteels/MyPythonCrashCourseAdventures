import json

number = [2,4,6,7,8,11]
filename = "numbers.json"
with open("../other_text_files/"+filename, 'w') as f:
    json.dump(number, f)


with open("../other_text_files/"+filename) as f:
    numbers = json.load(f)
    print(numbers)