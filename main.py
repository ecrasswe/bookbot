def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    character_count = get_character_count(book_text)
    sorted_characters = character_sort(character_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} found in the document")
    print()

    for item in sorted_characters:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found '{item['count']}' times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    text_lower_case = text.lower()
    letter_counts = {}
    for letter in text_lower_case:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts

def character_sort(character_dict):
    sorted_list = []
    for ch in character_dict:
        sorted_list.append({"char": ch, "count": character_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
 
def sort_on(dict):
    return dict["count"]

main()