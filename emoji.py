message = input('>')
words = message.split( ' ' )

emojis = {
     ':)' : "😊",
     ':(' : "😞",
}

a = 0
for word in words:
  if word in emojis.keys():
    words[a] = emojis[word]

  a += 1

print(" ".join(words))