
from operator import itemgetter
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = wordcount(text)
    number_of_letters = countcharacters(text)
    number_of_letters_total = list_of_letter(number_of_letters)
   # print(f"{num_words} words found in the document")
   # print(f"{number_of_letters} letters found in the document")
   # print(f"{num_words} words found in the document")
   # print(f"{number_of_letters_total} letters found in the document")
   # print(str(number_of_letters_total[1].keys())[12])
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for letters in number_of_letters_total:
        print(f"The '{str(letters.keys())[12]}' character was found {letters[str(letters.keys())[12]]} times")
    print ("--- End report ---")    
        



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

def get_count(letter_dict):
        return list(letter_dict.values())[0]

def list_of_letter(dict):
    list_of_letters = []
    for letter in dict:
        if letter.isalpha():
            is_alpha = {letter : dict[letter]}
            list_of_letters.append(is_alpha) 
    list_of_letters.sort(reverse=True, key=get_count)
    return list_of_letters
main()