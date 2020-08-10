number = input('Phone Number: ')
digits = {
  
  "1" : "One",
  "2" : "Two",
  "3" : "Three",
  "4" : "Four",
  "5" : "Five",
  "6" : "Six",
  "7" : "Seven",
  "8" : "Eight",
  "9" : "Nine",
}

output = " "
for numbers in number:
  output += " " + digits[numbers]


print(output)