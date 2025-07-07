def count_file_words(file_text):
    total_words = 0
    text_list = file_text.split()
    total_words = len(text_list)
    return total_words

def count_file_characters(file_text):
    letter_dict = {}
    for words in file_text:
        if words.lower() in letter_dict:
            letter_dict[words.lower()] += 1
        else:
            letter_dict[words.lower()] = 1
    
    return letter_dict

def sort_key(list):
    return list["num"]


def dict_to_list(file_dict):
    list_dicts = []
    for values in file_dict:
        dict_pair = {}
        dict_pair["char"] = values
        dict_pair["num"] = file_dict[values]
        list_dicts.append(dict_pair)
    list_dicts.sort(key=sort_key, reverse=True)
    return list_dicts


