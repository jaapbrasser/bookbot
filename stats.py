def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_character_counts(char_counts):
    # Only include alphabetic characters
    filtered = [
        {"char": char, "num": count}
        for char, count in char_counts.items()
        if char.isalpha()
    ]
    # Sort in-place descending by count
    filtered.sort(key=lambda x: x["num"], reverse=True)
    return filtered