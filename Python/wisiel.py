word = "rafał"
used_words = []
lista = []


for _ in word:
    lista.append("_")


def find_indexes(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
        return indexes
    
while True:
    letter = input("Podaj litrerę: ")
    used_words.append(letter)
    print(used_words)
    
    print(find_indexes(word, letter))
    print(used_words)