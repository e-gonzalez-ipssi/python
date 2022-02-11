def smash(list):
    string = ""
    for item in list:
        string = string + item + " "
    return string

print(smash(["je", "suis"]))
print(smash(["tu", "es"]))
print(smash(["il", "est"]))