def count_words(text):
    count = len(text.split())
    print(f"Found {count} total words")
    
def count_characters(text):
    character_counts = {}
    for letter in text:
        if letter.lower() not in character_counts:
            character_counts[letter.lower()] = 1
        else:
            character_counts[letter.lower()] += 1
    return character_counts

def create_counts_list(character_counts):
    counts = []
    for count in character_counts:
        if count.isalpha():
            counts.append({"char": count, "num": character_counts[count]})
    return counts
            
def sort_on(items):
    return items["num"]

def sort_counts_list(text):
    counts = create_counts_list(count_characters(text))
    counts.sort(reverse=True, key=sort_on)
    return counts