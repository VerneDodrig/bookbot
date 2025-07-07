from stats import count_file_words, count_file_characters, dict_to_list
import sys

def get_book_text(file_path):
    file_content = None
    with open(file_path) as path:
        file_content = path.read()
    return file_content


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    character_list = dict_to_list(count_file_characters(get_book_text(path_to_book)))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    print("----------- Word Count ----------")
    print(f"Found {count_file_words(get_book_text(path_to_book))} total words")
    print("--------- Character Count -------")
    for items in character_list:
        if items["char"].isalpha():
            print(f"{items["char"]}: {items["num"]}")
    print("============= END ===============")

main()