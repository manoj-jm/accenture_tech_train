# find the count of magical number from 1 to nonlocal
n = int(input())
count =0 
for i in range(1,n+1):
  k=str(bin(i))[2:]
  l=list(k)
  for i in range(len(l)):
    if l[i]=='0':
      l[i]='1'
    elif l[i]=='1':
      l[i]='2'
  sum =0
  for i in 1:
    sum+=int(i)
  if sum%2==1:
    count+=1
print(count)

# problem
