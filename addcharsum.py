# a = 0 , b = 1 c = a+b , d = b+c

s = input().lower()

sum1 = 0
def fib(n):
  if n==0 or n==1:
    return n
  else:
    return fib(n-1)+fib(n-2)
  
for i in s:
  val = fib(ord(i)-97)
  sum1+=val
print(sum1)