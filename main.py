def main():
    path_to_book = "books/frankenstein.txt"
    book_text = get_contents(path_to_book)
    word_count = count_words(book_text)
    letter_dictionary = count_letters(book_text)
    sorted_ltr_list = dict_builder(letter_dictionary)
    sorted_ltr_list.sort(reverse=True, key=sort_on)
    book_report(word_count, sorted_ltr_list, path_to_book)

def get_contents(path):
    with open(path) as f:
        return f.read()

def count_words(sample_text):
    word_list = sample_text.split()
    return len(word_list)

def count_letters(sample_text):
    all_lower = sample_text.lower()
    letters = {}
    for ltr in all_lower:
        if ltr.isalpha():
            if ltr not in letters:
                letters[ltr] = 1
            else:
                letters[ltr] += 1
    return letters

def dict_builder(dictionary):
    dict_list = []
    for ltr in dictionary:
        dict_list.append({
            "name": ltr,
            "num": dictionary[ltr]
        })
    return dict_list

def sort_on(dictionary):
    return dictionary["num"]

def book_report(words, ltr_list, path):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in this book")
    print("")
    for dict in ltr_list:
        print(f"The '{dict['name']}' character was found {dict['num']} times")
    print("--- End report ---")

main()