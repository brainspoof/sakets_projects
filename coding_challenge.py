a=0
sake = input('Word: ')
integer = []
string = []
lenght = len(sake)-1



while a<= lenght:
  number = sake[a]
  true = number.isnumeric()
  stri = number.isalpha()
  if stri == True:
    string.append(sake[a])
  if true == True:
    integer.append(sake[a])
 
  a+=1


print('\nYou have total ' + str(len(integer)) + ' ' + 'numbers' )
print('You have total ' + str(len(string)) + ' ' + 'alphabet' )
















#step 1 :: agar input mai se koi bhi character int ho to hi print karnba

#varna bye print karna









