'''
input ; abcd
ouput: zyxw'''

# we use the ascii value to solve this 
# 2 methods : ord() and chr()
# a-z = 97 --- 122

s = input()
d = {}
s.lower()
out =""
for i in s:
  out = out+chr(ord('z')-ord(i)+ord('a'))# 122 - 97 +97 ( for letter 'a' )
print(out)