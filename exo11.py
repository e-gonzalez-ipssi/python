def validate_word(string):
    already_use = []
    for char in string:
        if char in already_use:
            return False
        else:
            already_use.append(char)
    return True

print(validate_word("test"))
print(validate_word("Esteban"))