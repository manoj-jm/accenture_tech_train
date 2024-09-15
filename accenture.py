# def differenceof(n,m):
#   sumnum=0
#   notsnum=0
#   for i in range(1,m+1):
#     if i%n==0:
#       sumnum+=i
#     else:
#       notsnum+=i

#   print(sumnum,"-",notsnum,"=",abs(notsnum-sumnum))

# differenceof(4,20)

# arr = [1,8,0,2,3,5,6]
# evenpositionarr = [arr[i] for i in range(len(arr)) if i%2==0]
# oddpositionarr = [arr[i] for i in range(len(arr)) if i%2!=0]
# evenpositionarr.sort()
# oddpositionarr.sort()
# print(evenpositionarr,oddpositionarr)
# print(evenpositionarr[-2]+oddpositionarr[-2])

# def productsmallestpair(s,arr):
#   if len(arr)==0:
#     return 0
#   #least two elements
#   for i in range(len(arr)-1):
#     if arr[i]+arr[i+1]<s:
#       print(arr[i]*arr[i+1])
#       break
#   else:
#     print('0')


# arr = [5,2,4,3,9,7,1]
# productsmallestpair(9,arr)


#question 8
# di = {}
# j=65
# for i in range(0,36):
#   di[i]=i
#   if i>=10:
#     key = chr(j)
#     di[i]=key
#     j+=1

# # print(di)
# def dectoNbase(n,num,di):
#   li = []
#   while num!=0:
#     rem = num%n
#     li.append(di[int(rem)])
#     num= num//n
#     print(num)
#   li.reverse()
#   res = ''
#   for i in li:
#     res +=str(i)
#   print(res)

# dectoNbase(21,5678,di)

#question 9

# s = input()
# c=''
# ns =''
# for i in s:
#   if i=='-':
#     c+=i
#   else:
#     ns += i
    
# print(c+ns)

    