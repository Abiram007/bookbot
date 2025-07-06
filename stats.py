def get_book_text(path):
    with open(path) as f:
        content = f.read()

    return content

def word_count(sentence):
    return len(sentence.split())

def letter_count(sentence):
    res = {}
    for char in sentence:
        if char != ' ':  # Skip spaces
            char_lower = char.lower()
            if char_lower not in res:
                res[char_lower] = 1
            else:
                res[char_lower] += 1
    return res

def sort_key(items):
    return items[1]

def clean_dict(dicto):
    res = dict(sorted(dicto.items(), key = sort_key, reverse = True))
    return res