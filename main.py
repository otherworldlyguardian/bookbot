from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_name = sys.argv[1]
    book_text = get_book_text(path_name)
    num_words = get_num_words(book_text)
    char_list = char_dict_list(count_characters(book_text))
    # print(char_list)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_name}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in char_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")

main()