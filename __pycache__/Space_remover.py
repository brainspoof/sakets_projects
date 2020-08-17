# way 1

b = ''
user = 'Hi Hello How     are you                       '
user = list(user)

if user[-1] == ' ':
    b = True

else:
    b = False

while b == True:
    if user[-1] == " ":
        user.pop(-1)
    elif user[-1] != " ":
        break

user = ''.join(user)
user = user.replace(' ', '-')

print(user)

# way 2

i = '               Hi Hello How     are you                       '
output = i.strip()
print(output)