s = input()
d = {}
for i in s:
  if i in d:
    d[i]+=1
  else:
    d[i]=1

# print(d)
for k,v in d.items():
  print(k,":",v)


print("2nd approach")
#2nd 
for i in s:
    d[i]=s.count(i)

for k,v in d.items():
  print(k,":",v)