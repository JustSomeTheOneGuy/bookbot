def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    word_count = get_word_count(book)
    char_count = get_character_count(book)
    sorted_list = list_of_dictionaries(char_count)
    
    sorted_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words were found in this document")
    print()

    for l in sorted_list:
        print(f"The '{l["char"]} character was found {l["num"]} times")

    print("--- End report ---")

   


def sort_on(dict):
    return dict["num"]

def list_of_dictionaries(dict):
    list_dict = []
    for d in dict:
        if d.isalpha():
            list_dict.append({"char" : d, "num" : dict[d]})
    return list_dict

def get_character_count(text):
     character_count = {}
     check = text.lower()
     for c in check:
        if c in character_count:
            character_count[c] += 1
        else:
            character_count[c] = 1
     return character_count

def get_word_count(text):
    word_count = text.split()
    return len(word_count)
    
def get_book_text(path):
     with open(path) as f:
         file_contents = f.read()
     return file_contents

main()



      






