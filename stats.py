def count_words(path_to_file):
    with open(path_to_file) as f:
        list = f.read().split()
        return len(list)

def count_characters(path_to_file):
    with open(path_to_file) as f:
        string = f.read()
        char_counts = {}
        for char in string.lower():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        return char_counts

def dict_to_list_of_dict(dict):
    list = []
    for i in dict:
        dicts = {"char": "", "num": 0}
        dicts["char"] = i
        dicts["num"] += dict[i]
        list.append(dicts)

    def sort_on(dict):
        return dict["num"]
    
    list.sort(reverse=True, key=sort_on)
    return list
