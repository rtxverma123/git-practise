lst = [1,2,3,4,5,6,7]
def mul(n):
   n = n**2
   return n

x = map(mul,lst)
print(list(x))
