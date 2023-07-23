try:
    with open("../other_text_files/excerpt_from_the_green_girl_ebook.txt", encoding='utf-8') as excerpt:
        contents = excerpt.read()
        word_count = contents.lower().count("green")
        print(word_count)
except FileNotFoundError:
    print("File not found!")