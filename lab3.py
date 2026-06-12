
# 1. 
a = 5
print("a")
# Output: a


# 2. 
a = 99.35
print(a)
# Output: 99.35


# 3. 
a = 5
b = 6
print("a+b")
# Output: a+b


# 4. 
a = 5
b = 6
print("a"+b)
# Output: TypeError (cannot concatenate string and integer)


# 5. 
a = 5
b = 6
print(a+b)
# Output: 11


# 6. 
a = 15
b = 6
c = a - b
print(c)
# Output: 9


# 7. 
a = 5
b = 6
c = a + b
print("Sum is : ",c)
# Output: Sum is : 11


# 8. 
a = 5
b = 6
c = a + b
print(c,"is Your Result")
# Output: 11 is Your Result


# 9. 
a = 5
b = 6
c = a + b
print("Sum ",c,"is your Result")
# Output: Sum 11 is your Result


# 10. 
a = 5
b = 6
c = a + b
print(a,"and",b,"sum is",c)
# Output: 5 and 6 sum is 11


# 11. 
cost = 2500
discount = 10
discAmt = (cost /100) * discount
print(discAmt)
# Output: 250.0


# 12. 
a = 10
b = 20
a = a + b
b = a - b
a = a - b
print(a,"\t",b)
# Output: 20    10


# 13. 
a = 20
a = "Naveen"
print(a)
# Output: Naveen


# 14. 
a = 2
b = a
print(b)
# Output: 2


# 15. 
n1 = "Naveen"
n2 = "with Python"
fname = n1+"-"+n2
print(fname)
# Output: Naveen-with Python


# 16. 
a = "7"
b = "9"
c = a + b
print(c)
# Output: 79


# 17. 
a = 7
b = 5
a = a * b
b = a // b
a = a // b
print(a,"\t",b)
# Output: 5    7


# 18. 
a = 7
b = 5
c = a
a = b
b = c
print(a,"\t",b)
# Output: 5    7


# 19. 
n = 12
sum = 0
r = n % 10
n = n // 10
sum = sum + r
r = n % 10
n = n // 10
sum = sum + r
print(n,"\t",sum)
# Output: 0    3


# 20. 
c1 = "Advance"
c2 = " Django"
c3 = " Project"
c4 = c1 + c3 + c2 + c3
print(c4)
# Output: Advance Project Django Project


# 21. 
a = 5
b = 7
a,b = b,a
print(a,"\t",b)
# Output: 7    5


# 22. 
p = 5
q = 3
r = 7
print(p,"\t",q,"\t",r)
# Output: 5    3    7


# 23. 
p = 5
q = 3
r = 7
print(p,q,r)
# Output: 5 3 7


# 24.
p = 5
q = 3
r = 7
print(p,q,r,sep=",")
# Output: 5,3,7


# 25.
p = 5
q = 3
r = 7
print(p,q,r,sep="$")
# Output: 5$3$7


# 26.
p = 5
q = 3
r = 7
print(p,q,r,sep="-->")
# Output: 5-->3-->7


# 27.
p = 5
q = 3
r = 7
print(p,q,r,sep="V")
# Output: 5V3V7


# 28.
p = 5
q = 3
print(p,end="\t")
print(q)
# Output: 5    3


# 29.
p = 5
q = 3
print(p)
print(q)
# Output:
# 5
# 3


# 30.
p = 5
q = 3
print(p,end="-")
print(q)
# Output: 5- 
#3


# 31.
a = 2.523649
print(a)
# Output: 2.523649


# 32.
a = 8
print("%d"%a)
# Output: 8


# 33.
a = 8
b = 4
print("%d%d"%(a,b))
# Output: 84


# 34.
a = 8
b = 4
print("%d\t%d"%(a,b))
# Output: 8    4


# 35.
a = 41.756
print("%f"%a)
# Output: 41.756000


# 36.
a = 41.756
print("%.2f"%a)
# Output: 41.76


# 37.
a = 41.756
print("%.4f"%a)
# Output: 41.7560


# 38.
a = 41.756
print("%d"%a)
# Output: 41


# 39.
a = 6
print("A value is :{0}".format(a))
# Output: A value is :6


# 40.
a = 6
b = 3
print("{0}\t{1}".format(a,b))
# Output: 6    3


# 41.
a = 6
b = 3
print("a={0}\tb={1}".format(b,a))
# Output: a=3    b=6


# 42.
a = 6.43
print("a={0}".format(a))
# Output: a=6.43