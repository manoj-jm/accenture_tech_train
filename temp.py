T=[73,74,75,71,69,72,76,73]
res=[0 for x in range(len(T))]
for i in range(len(T)):
  for j in range(i+1,len(T)):
    if T[j]>T[i]:
       res[i]=j-i
       break
print(res)