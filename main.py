def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = wordcount(text)
    number_of_letters = countcharacters(text)
    print(f"{num_words} words found in the document")
    print(f"{number_of_letters} letters found in the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()    

def wordcount(text):
    words = text.split()
    number = 0
    for  word in words:
        number += 1
    return number

def countcharacters(text):
    letters = {}
    for i in range(0,len(text)):
        lowered_string = text[i].lower()
        if lowered_string in letters:
            character_number = letters[lowered_string] +1
            letters[lowered_string] = character_number
        else:
            letters[lowered_string] = 1   
    return letters   

main()