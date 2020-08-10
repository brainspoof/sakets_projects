numbers = [10, 20, 30, 40, 50, 50, 40, 30, 20, 10]

different = []
for number in numbers:
  if number not in different:
    different.append(number)
    print(different)

