def count_words(text):
    count = len(text.split())
    return count


def count_characters(text):
    characters = {}
    for char in text:
        lower = char.lower()
        if lower in characters:
            characters[lower] += 1
        else:
            characters[lower] = 1
    return characters

def sort_list(characters):
    char_list = []
    for char, count in characters.items():
        char_list.append({"char": char, "count": count})
    
    def sort_on(dict):
        return dict["count"]        
    char_list.sort(reverse=True, key=sort_on)
    return char_list