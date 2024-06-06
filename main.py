def main():
    path_to_book = "books/frankenstein.txt"
    book_text = get_contents(path_to_book)
    print(f"{count_words(book_text)} words in this book")
    print(count_letters(book_text))

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
        if ltr not in letters:
            letters[ltr] = 1
        else:
            letters[ltr] += 1
    return letters

main()