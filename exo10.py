def inver(string):
    result = string.split("-",len(string))
    result.reverse()
    return "-".join(result)

print(inver('green-red-black-white'))