def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_count_letters(text)
    letter_list = get_sorted_list_from_dict(num_letters)
    # print(f"{num_words} words found in the document")
    # print(letter_list)
    print_report(book_path,num_words,letter_list)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_count_letters(text):
    lower_text = text.lower()
    letter_dict = {}
    for letter in lower_text:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else :
            letter_dict[letter] = 1
    return letter_dict

def get_sorted_list_from_dict(dict):
    letter_list = []
    for key,val in dict.items():
        if key.isalpha():
            letter_list.append({"name":key,"num":val})
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list

def print_report(book,word_count,letter_list):
    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document")
    print("")
    for letter in letter_list:

        print(f"The '{letter['name']}' character was found {letter['num']} times")
    
    print("--- End report ---")
    

def sort_on(dict):
    return dict["num"]


main()