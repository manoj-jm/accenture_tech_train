s1 = input()
s2 = input()
i=0
ns = ''
while i<len(s1) or i<len(s2):
  if i<len(s1):
    ns+=s1[i]
  if i<len(s2):
    ns+=s2[i]
  i+=1

ns +=s1[i:]
ns +=s2[i:]

print(ns.upper())