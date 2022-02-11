def validate_word(string):
    already_use = {}
    for char in string:
        if char.lower() in already_use:
            already_use[char.lower()] += 1
        else:
            already_use[char.lower()] = 1
    
    nums = []
    for key in already_use:
        nums.append(already_use[key])

    for i in range(len(nums)):
        if nums[i] != nums[0]:
            return False
    return True

print(validate_word("abcabc"))
print(validate_word("Abcabc"))
print(validate_word("AbcabcC"))
print(validate_word("AbcCBa"))
print(validate_word("pzppz"))
print(validate_word("?!?!?!"))
print(validate_word("abc123"))
print(validate_word("abcabcd"))
print(validate_word("abc!abc!"))
print(validate_word("abc:abc"))
