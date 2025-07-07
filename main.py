import sys
from stats import count_characters, sort_character_counts

def get_book_text(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def count_words(text):
    words = text.split()
    return len(words)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text(book_path)
    if text.startswith("Error"):
        print(text)
        return

    word_count = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    char_counts = count_characters(text)
    sorted_char_data = sort_character_counts(char_counts)

    print("--------- Character Count -------")
    for entry in sorted_char_data:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
