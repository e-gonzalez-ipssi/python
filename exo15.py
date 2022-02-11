def list_sum(list):
    result = 0
    for item in list:
        result = result + item
    return result

def parts_sums(list):
    result = []
    while list != []:
        result.append(list_sum(list))
        list.pop(0)
    result.append(0)
    return result

print(parts_sums([0, 1, 3, 6, 10]))