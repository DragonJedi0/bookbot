from stats import *
from sys import *

def get_book_text(filepath):
    return filepath.read()

def main():
    try:
        pwd = "/home/sybarra/bootdev/bookbot"
        path = argv[1]
        full_path = f"{pwd}/{path}"
        try:
            with open(full_path, "r") as book_path:
                bookText = get_book_text(book_path)
            num_words = get_number_of_words(bookText)
            num_chars = get_number_of_characters(bookText)

            char_list=get_report(num_chars)
            char_list.sort(key=sort_on, reverse=True)
            
            # Print Report
            print("============ BOOKBOT ============")
            print(f"Analyzing book found at {path}...")
            print("----------- Word Count ----------")
            print(f"Found {num_words} total words")
            print("--------- Character Count -------")
            for i in range(0, len(char_list)):
                if char_list[i]["char"].isalpha():
                    print(char_list[i]["char"] + ":", char_list[i]["num"])
            print("============= END ===============")

        except FileNotFoundError:
            print(f"Error: the file {path} was not found.")
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        return exit(1)

main()