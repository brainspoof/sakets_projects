string = input("> ")

chars = list(string)

reversed_chars = []

for char in chars:
  reversed_chars.insert(0, char)

reversed_string = ''.join(reversed_chars)
print(reversed_string)