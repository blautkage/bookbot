import sys
from stats import get_num_words, character_count, report_sort

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def main():
    if (len(sys.argv)) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
    word_count = get_num_words(text)
    print(f"Found {word_count} total words")
    char_counts = character_count(text)
    sorted_chars = report_sort(char_counts)
    for item in sorted_chars:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha(): print(f"{ch}: {num}") 

if __name__ == "__main__":
    main()