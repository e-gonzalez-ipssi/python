result = []
for item1 in [1, 2, 3]:
    for item2 in [1, 2, 3]:
        if item1 > 2 and item2 < 3:
            result.append(item2)
print(result)

list = [j for i in [1, 2, 3] for j in [1, 2, 3] if i > 2 and j < 3]
print(list)


result = []
for item1 in [x for x in range(10)]:
    for item2 in [j for j in range(5)]:
        if item2 > 3:
            result.append((item1, item2))
print(result)

list = [(i,j) for i in range(10) for j in range(5) if  j > 3]
print(list)