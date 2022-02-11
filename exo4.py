def smash(list):
    string = ""
    for item in list:
        string = string + item + " "
    return string

print(smash(["hello", "world"]))
