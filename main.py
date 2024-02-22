def main():
    book='./books/frankenstein.txt'
    text=get_text(book)
    word_nums=word_count(text)
    letters=letter_count(text)
    letter_report=report(letters)
    print(letter_report)

def report(item:dict):
    for key,val in item.items():
        print(f'The {key} character was found {val} times.')
    return

def letter_count(words:str):
    letters_dict={}
    word_list=words.split()
    for word in word_list:
        for character in word:
            if character.isalpha()==True:
                if letters_dict.get(character.lower())==None:
                    letters_dict[character.lower()]=1
                else:
                    letters_dict[character.lower()]+=1
    
    return letters_dict
    
def word_count(words:str):
    word_list=words.split()
    return len(word_list)

def get_text(file):
        with open(file) as f:
            file_contents=f.read()
        return file_contents

main()

