# try:
#     mobile = int(input('Enter Your mobile number: '))
#     print(f'Your Mobile number is {mobile}')

# except ValueError:
#     print('Enter a valid mobile number ')


# mobile = '12--123'
# mobile = list(mobile)
# alpha = []
# number = []

# for m in mobile:
#     if m.isalpha():
#         alpha.append(m)

#     elif m.isnumeric():
#         number.append(m)

# if len(alpha)>=1:
#     print('Invalid number')

# else:
#     print(''.join(mobile))


number = '123401239asd'

print(number) if number.isnumeric() else print("Invalid Number")


