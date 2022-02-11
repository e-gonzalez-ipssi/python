def shortcut(text):
  consonne = "bcdfghjklmnpqrstvwxz"
  indexes = [letter for letter in text.lower() if letter in consonne]
  return "".join(indexes)

print(shortcut("Esteban"))
print(shortcut("xylophone"))