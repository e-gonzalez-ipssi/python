def is_reverse_word(string):
    stringInverse = string[::-1]
    if stringInverse == string:
        return True
    else:
        return False

print(is_reverse_word("aza"))
print(is_reverse_word("coloc"))
print(is_reverse_word("madam"))
print(is_reverse_word("kayak"))
print(is_reverse_word("bonjour"))
print(is_reverse_word("python"))
