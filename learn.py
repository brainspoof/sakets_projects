user_input = input('Text: ')
to_replace = input('''
Would you like to replace any thing
If none than type --//none//--
''')
replace_with = input('with: ')

user_input = user_input.split(" ")
to_replace = to_replace.replace(' ', '')
to_replace = to_replace.split(',')

replace_with = replace_with.replace(' ', '')
replace_with = replace_with.split(',')

if to_replace == '--//none//--':
  exit()

for u in user_input:
    if u in to_replace:
        i = to_replace.index(u)
        index = user_input.index(u)
        user_input[index] = replace_with[i]
print(" ".join(user_input))
