def get_num_words(doc):
    return len(doc.split())

def count_characters(doc):
    char_dict = {}
    for char in doc:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def char_dict_list(dict):
    char_as_list = []
    for key, value in dict.items():
        char_as_list.append({"char": key, "num": value})
    char_as_list.sort(reverse=True, key=sort_on)
    return char_as_list

def sort_on(dict):
    return dict["num"]