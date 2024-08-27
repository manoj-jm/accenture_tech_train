# a --> f ..... u ---> z and v ---> a


s = input()
nc = ""
for i in s:
  if(ord(i)+5 < 122):
    nc += chr(ord(i)+5)
  else:
    nc+=chr(ord(i)+5-26)



print(nc[::-1])

