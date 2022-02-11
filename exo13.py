def even_last(list):
    if not list:
        return 0
    result = 0
    for i in range(len(list)):
        if i % 2 == 0:
            result = result + list[i]
    result = result * list[len(list)-1]
    return result

print(even_last([]))
print(even_last([2, 3, 4, 5]))