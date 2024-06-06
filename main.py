def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = wordcount(text)
    print(f"{num_words} words found in the document")

def wordcount(text):
    words = text.split()
    number = 0
    for  word in words:
        number += 1
    return number

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()