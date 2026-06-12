
#1. Consider a is 5 and b is 3, store a in b print a and b.

a=5
b=3
b=a
print(a,b)
#o/p: 5 5

#2. Consider a is 3 b is 2.5 print a and b.

a = 3
b = 2.5
print(a,b)
#o/p: 3 2.5

#3. Consider a is 2.3, b is 5 store sum of a, b in c print c.

a = 2.3
b = 5
c = a+b
print(c)
#o/p: 7.3

#4. Consider a is "sathya" b is "tech" store fullname in c print c.

a = "sathya"
b = "tech"
c = a+b
print(c)
#o/p: sathyatech

#5. Consider a is 2, b is 5 store a and b in c then print c.

a = 2
b = 5
c = (a,b)
print(c)
#o/p: (2, 5)

#6. Consider a is 2.3 b is 9 store a in b print b.

a = 2.3
b = 9
b = a
print(b)
#o/p: 2.3


#7. Consider a is 5 b is 3 store sum of a, b in c, display output.

a = 5
b = 3
c = a + b
print(c)
#o/p: 8

#8. Consider x is 'a' y is 5 store x in y print x, y.

x = 'a'
y = 5
y = x
print(x,y)
#o/p: a a

#9. Consider x is 2.3 y is 3 store sum of x, y in z print z.

x = 2.3
y = 3
z = x + y
print(z)
#o/p: 5.3

#10. Consider a is 'x' b is 'y' store a and b in c print c.

a = 'x'
b = 'y'
c = a + b
print(c)
#o/p: xy

#11. Consider x is 5 y is 2 x divide by y store in z print z.

x = 5
y = 2
z = x / y
print(z)
#o/p: 2.5

#12. Consider x is 5 product of x and x store in y print y.

x = 5
y = x * x
print (y)
#o/p: 25

#13. Consider x is 3 cube of x store in y print x, y.

x = 3
y = x ** 3
print(x, y)
#o/p: 3 27

#14. Consider x is 3 square of x store in s, cube of x store in c print s, c.

x = 3
s = x ** 2
c = x ** 3
print(s,c)
#o/p: 9 27

#15. Consider x is 2, square of x store in s, cube of x store in c. Sum of s and c store in sum print sum.

x = 2
s = x ** 2
c = x ** 3
sum = s + c
print(sum)
#o/p: 12

#16. Consider x is 5, y is 3. Store product of x and y in z and sum of x, y, z in p print p.

x = 5
y = 3
z = x * y
p = x + y + z
print(p)
#o/p: 23

#17. Principal = 1000, Rate = 15%, Time = 5 years. Display total amount based on Simple Interest.

p = 1000
r = 15
t = 5
si = (p * t * r) / 100
amount = p + si

print("Simple Interest =", si)
print("Total Amount =", amount)

#o/p: Simple Interest = 750.0, Total Amount = 1750.0


#18. Program to calculate total salary of employee.

basic = 10000

hra = basic * 30 / 100
da = basic * 10 / 100

salary = basic + hra + da

print("Total Salary =", salary)

#o/p : Total Salary = 14000.0

#19. Consider 3 subject marks as 60, 70, 80. Display total marks and percentage.

m1 = 60
m2 = 70
m3 = 80

total = m1 + m2 + m3
percentage = total / 3

print("Total Marks =", total)
print("Percentage =", percentage)
#o/p: Percentage = 70.0
# Total Marks = 210

#20. Product cost is 1000 Rs. GST is 10% of product cost. Calculate net price.

cost = 1000

gst = cost * 10 / 100
net_price = cost + gst

print("GST =", gst)
print("Net Price =", net_price)

#o/p: GST = 100.0
# Net Price = 1100.0
