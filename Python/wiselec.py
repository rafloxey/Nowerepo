import sys
no_off_tries = 5
word = 'kamil'
used_letters = []
user_word = []

def find_indexes(word, letter):
    indexes = []
    
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
            
   
    
    return indexes


################################


for _ in word:
    user_word.append('_')


while True:
    letter = input('Podaj literę: ')
    used_letters.append(letter)
    found_indexes = find_indexes(word, letter)
    
    if len(found_indexes) == 0:
        print('Nie znaleziono tej litery.')
        no_off_tries -= 1
        
        if no_off_tries == 0:
            print('Przegrales! Poprawne slowo to:', word)
            sys.exit(0)
        else:
            for index in found_indexes:
                user_word[index] = letter
            print(user_word)
            print("".join(user_word))
    
    print('Uzyte litery:', used_letters)