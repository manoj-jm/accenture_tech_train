# the price of eaach  item is product of each digits in code 

s = input()

o = 1

for i in s:
  if i.isdigit():
    o *= int(i)

print(o)
#problem 2

# the sprice of the product is su o fthe numbers in the code  ( take the consecutive numbwer and add them )
ss = 0
t = 0
for i in s:
  if i.isdigit():
    t= t*10 + int(i)
  else:
      if t>0:
        ss+=t
      t=0

ss+=t
print(ss)

