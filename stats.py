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

