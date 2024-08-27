s1 = input()
s2 = input()
i=0
j=0
f=1
ns = ''
while i!=len(s1) and j!=len(s2):
  if f==1:
    ns+=s1[i]
    i+=1
    f=0
  else:
    ns+=s2[j]
    j+=1
    f=1


ns += s1[i:]
ns +=s2[j:]

print(ns.upper())