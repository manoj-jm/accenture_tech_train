#9-1001 # last bit is 1 ( odd)
#10-1010 # last bit is 0(even)

n = int(input())
if (n&1):
  print("odd number")
else:
  print("even number")


# bit manipulation
# toggle the Kith bit number 
'''
9 --> 1001
toggle with 2nd bits
1001 --> 1011

'''

k = int(input("enter the k : "))
res = n*(1<<(k-1))
print(res)