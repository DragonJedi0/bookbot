def get_number_of_words(book_path):
    words = book_path.split()
    counter = 0
    for word in words:
        counter += 1

    return counter

def get_number_of_characters(booktext):
    characters={}
    for char in booktext:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    
    return characters

def get_report(num_chars):
    unsorted_list = []
    empty_dict = {}
    for chars in num_chars:
        empty_dict["char"] = chars
        empty_dict["num"] = num_chars[chars]
        unsorted_list.append(empty_dict)
        empty_dict = {}

    return unsorted_list

def sort_on(dict):
    return dict["num"]