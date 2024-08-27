# the price of eaach  item is product of each digits in code 

s = input()

o = 1

for i in s:
  if i.isdigit():
    o *= int(i)

print(o)
