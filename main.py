import sys
from stats import count_words
from stats import count_characters
from stats import dict_to_list_of_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        num_words = count_words(path)
        num_characters = count_characters(path)
        sorted_list_of_dict = dict_to_list_of_dict(num_characters)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for i in sorted_list_of_dict:
            if i["char"].isalpha() == False:
                continue
            else:
                print(f"{i["char"]}: {i["num"]}")
        print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

   

main()