def sort_on(dict): #specifies how @func .sort() is to search through the dictionary of characters.
    return dict['num']

def get_word_count(book_text): # accepts a string and returns the total number of words
    num_words = len(book_text.split())
    return num_words

def get_char_count(book_text):
    book_text = book_text.lower() # convert to lower case to avoid dups
    char_dict = { }
    for i in range(len(book_text)):
        c = book_text[i]
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict.update({c : 1})
    return char_dict

def get_sorted_list(char_dict): # takes dict of total chars and their counts and returns a sorted list of dictionaries
    results = [ ]
    for key in char_dict:
        if key.isalpha():
            list_entry = {"char": key, "num": char_dict[key]}
            results.append(list_entry)
    results.sort(reverse=True, key=sort_on)
    return results
    