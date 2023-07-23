try:
    with open('../other_text_files/cats.txt', encoding='utf-8') as cats:
        for line in cats.readlines():
            print(line.rstrip())
    with open("../other_text_files/dogs.txt", encoding='utf-8') as dogs:
        for line in dogs.readlines():
            print(line.rstrip())
except FileNotFoundError:
    pass

