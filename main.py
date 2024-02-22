def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    # Word count
    word_count = count_words(text)

    # Character counts
    char_counts = count_characters(text)

    # Generate and print the report
    print_report(book_path, word_count, char_counts)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts

def print_report(book_path, word_count, char_counts):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    sorted_char_counts = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

    for char, count in sorted_char_counts:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

main()
