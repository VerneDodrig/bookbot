from stats import count_file_words, count_file_characters, dict_to_list

def get_book_text(file_path):
    file_content = None
    with open(file_path) as path:
        file_content = path.read()
    return file_content


def main():
    character_list = dict_to_list(count_file_characters(get_book_text("./books/frankenstein.txt")))

    print("============ BOOKBOT ============")
    print("Analyzing book found at ./books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {count_file_words(get_book_text("./books/frankenstein.txt"))} total words")
    print("--------- Character Count -------")
    for items in character_list:
        if items["char"].isalpha():
            print(f"{items["char"]}: {items["num"]}")
    print("============= END ===============")

main()