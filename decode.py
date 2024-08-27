n = input()
s = str(n)
l = s.split('0')
os = ''
for i in l:
  os += chr(len(i)+64) 
print(os)

# for i in l:
#   res ==chr(i.count('1')+64)
