from stats import count_words, count_characters, sort_counts_list
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    
def create_output(filepath):
    book_text = get_book_text(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    count_words(book_text)
    print("--------- Character Count -------")
    for letter in sort_counts_list(book_text):
        print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")
    
def main():
    if len(sys.argv) == 2:
        create_output(sys.argv[1])
    else:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
if __name__ == "__main__":
    main()
