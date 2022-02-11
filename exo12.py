def merge_string(word1, word2, letter):
    return word1.split(letter)[0] + letter + word2.split(letter)[1]

print(merge_string("Hello", "World", "l"))
print(merge_string("Esteban", "James", "a"))