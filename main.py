import random

numbers = [random.randint(0, 100) for a in range(50)]
print(numbers)
# maximum = 0

# for number in numbers:
#   if number > maximum:
#     maximum = number

# print(maximum)

print(max(numbers))