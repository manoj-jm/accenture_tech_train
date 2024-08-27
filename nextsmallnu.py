arr = [3,2,11,7,93,92,2,4,8,1]
narr = []
for i in range(len(arr)):
  f=0
  for j in range(i,len(arr)):
    if arr[j]<arr[i]:
      narr.append(arr[j])
      f=1
      break
  if f!=1:
    narr.append(-1)

print(narr)