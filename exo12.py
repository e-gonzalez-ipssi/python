def merge_string(word1, word2, letter):
    return word1.split(letter)[0] + letter + word2.lstrip(word2.split(letter)[0]+letter)

print(merge_string("Hello", "World", "l"))
print(merge_string("coding", "anywhere", "n"))
print(merge_string("jason", "samson", "s"))
print(merge_string("wonderful", "people", "e"))