from string import ascii_lowercase

with open("books/Frankenstein.txt") as f:
    text = f.read()

def get_word_count(text):
    "Return the number of words in a file."
    return len(text.split())

def get_letter_count(text):
    letters = {}
    
    for i in ascii_lowercase:
        letters[f'{i}']=0
    
    text.lower()
    list_text = list(text)

    for k in list_text:
        if k in letters:
            letters[f"{k}"] += 1
        #letters.update({k:})
    return letters

def full_report(text):
    print(f"{get_word_count(text)} words found in the document")
    for i in get_letter_count(text):
        print(f"The '{i}' character was found {get_letter_count(text)[i]} times")
    print(" --- end report --- ")

full_report(text)

