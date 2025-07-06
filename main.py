from stats import *
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    print("Found",word_count(text), "total words")
    dictionary = letter_count(text)
    res = (clean_dict(dictionary))
    for i,j in res.items():
        print(f"{i}: {j}")
main()