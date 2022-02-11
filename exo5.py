def pillars(num, length, width):
    if num <= 1:
        return 0
    else:
        return (num-1) * (length * 100) + (num-2) * (width)

print(pillars(1, 10, 10))
print(pillars(2, 20, 25))
print(pillars(11, 15, 30))