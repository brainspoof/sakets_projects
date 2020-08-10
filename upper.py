ui= input('write a text: ')
saket = ui.lower()

list1 = list(saket)

list2=[]

for letters in list1:
  char = ord(letters) - 32
  achar = chr(char)
  list2.append(achar)
 
a=''

a=a.join(list2)
print(a)

