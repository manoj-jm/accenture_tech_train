# arr = [3,2,11,7,93,92,2,4,8,1]
# narr = []
# for i in range(len(arr)):
#   f=0
#   for j in range(i,len(arr)):
#     if arr[j]<arr[i]:
#       narr.append(arr[j])
#       f=1
#       break
#   if f!=1:
#     narr.append(-1)

# print(*narr)


# 2nd 

# find the total number of superior elements present(on the righthand side)  in the arrya

a =  [8,10,6,2,9,7,5]
c=1
# go from last to first
s = a[-1]
i = len(a)-2
while i>=0:
  if a[i]>s:
    c+=1
    s= a[i]
  i-=1


print(c)
  
  