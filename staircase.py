

n =int(input())
# c= 0
# i=0
# while n>0:
#   nn= 1<<n.bit_length()-1
#   c+=1
#   n-=nn
# print(c)

# 2nd method
k = str(bin(n))
print(k.count('1'))
  