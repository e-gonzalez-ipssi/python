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
print(parts_sums([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]))
print(parts_sums([170110, 139570, 171544, 71770, 167818, 133006, 33628, 81872, 3143, 136857, 70720, 122107, 91191, 80135]))
print(parts_sums([14231, 137542, 173347, 19792, 63830, 87040, 15621, 56268, 65441, 193264, 153828, 97321, 179116, 182144]))