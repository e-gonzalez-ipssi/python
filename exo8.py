def multiply(list):
    result = 1
    for item in list:
        result = result * item
    return result

print(multiply((8, 2, 3, -1, 7)))
print(multiply((16, 12, 5, 2, -7)))
print(multiply((100, 12, 5, -2, -2)))