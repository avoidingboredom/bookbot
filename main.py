# imports 
import sys
from stats import get_word_count
from stats import get_char_count
from stats import get_sorted_list

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def print_results(word_count, character_list, file_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for index in character_list:
        print(f"{index['char']}: {index['num']}")
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path_book = sys.argv[1]

    book_text = get_book_text(file_path_book)
    # print(book_contents)
    word_count = get_word_count(book_text)
    char_count_dict = get_char_count(book_text)
    sorted_char_list = get_sorted_list(char_count_dict)
    print_results(word_count, sorted_char_list, file_path_book)

main()