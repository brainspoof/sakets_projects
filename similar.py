list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 8, 8, 9, 10, 11, 21]
list3 = []


for l in list2:
  for li in list1:
    if l == li:
      list3.append(l)
      
print(list3)


# list 2 ka pehela element lo
# agar wo element list 1 me bhi hai to use list 3 me dal do 
# warna kuch bhi mat karo 
# repeate steps 1-3 till the time you have gone through all the elements
#print(list 3)