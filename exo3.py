def shortcut(text):
	result = []
	voyelles = ["a", "e", "i", "o", "u", "y"]
	for char in text:
		if char.lower() not in voyelles:
			result.append(char)
	result = "".join(result)
	return result


print(shortcut("hello"))
print(shortcut("wars"))
print(shortcut("goodbye"))
print(shortcut("HELLO"))
