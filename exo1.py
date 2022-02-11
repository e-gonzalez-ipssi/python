def remove(string):
    if string[len(string)-1] == "!":
        return string[:-1]
    else:
        return string
    
print(remove("string"))
print(remove("string!"))