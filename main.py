from stats import count_words, count_characters, sort_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path_to_file = sys.argv[1]

def main():
    #path_to_file = 
    text = get_book_text(path_to_file)
    num_words = count_words(text)
    chats_dict = count_characters(text)
    sorted = sort_list(chats_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzin book fount at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in sorted:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["count"]}")
    print("============= END ===============")

    #print(f"{num_words} words found in the document")
    #print((chats_dict)) 
    #print(sorted)



def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()
