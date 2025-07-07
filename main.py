from stats import count_file_words

def get_book_text(file_path):
    file_content = None
    with open(file_path) as path_content:
        file_content = path_content.read()
    return file_content


def main():
    print(f"{count_file_words(get_book_text("./books/frankenstein.txt"))} words found in the document")


main()