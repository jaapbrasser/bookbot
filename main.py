def get_book_text(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def main():
    book_path = "books/frankenstein.txt"  # adjust path if it's in a subfolder
    text = get_book_text(book_path)
    print(text)

if __name__ == "__main__":
    main()
