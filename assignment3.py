#1

n=int(input("Enter a Number to convert into Binary : "))
b=bin(n)
print(b)


#2
a=int(input("Enter First number : "))
b=int(input("Enter Second number: "))
print("Enter the mathematical expression from +,-,*,/")
c=input("Enter expression: ")
if(c=='+'):
    print(a+b)
elif(c=='-'):
    print(a-b)
elif(c=='*'):
    print(a*b)
elif(c=='/'):
    print(a/b)
else:
    print("Invalid expression enter the expression again")


#3

import math
#a
x=(3+4)*(5)
print(x)

#b
n=int(input("Type a Number "))
y =(n*(n-1))/2
print(y)

#c
r=int(input("Radius "))
z=math.pi
m=4*z*r**2
print(m)

#d
r=int(input("Give a Value "))
a=int(input("Enter First Angle in Degree "))
b=int(input("Enter Second Angle in Degree "))
c=(a*z)/180
d=(b*z)/180
cos=math.cos(c)
sin=math.sin(d)
k=(r*cos**2)+(r*sin**2)
f=math.sqrt(k)
print("ANSWER ",f)

#e
Y1=int(input("Enter First number in numerator "))
Y2=int(input("Enter Second number in numerator "))
X1=int(input("Enter First number in denominator "))
X2=int(input("Enter Second number in denominator "))
z=(Y2-Y1)/(X2-X1)
print(z)




#4
#a
for i in range(5):
    print(i)
#b
for j in range(3,10):
    print(j)
#c
for m in range(4,13,3):
    print(m)
#d
for n in range(15,5,-2):
    print(n)
#e
for s in range(5,3,):
    print(s)


#5

h=int(input("No. of Hydrogen Atoms :"))
c=int(input("No. of Carbon Atoms :"))
o=int(input("No. of Oxygen Atoms :"))
molewgt=(h*1.00794)+(c*12.0107)+(o*15.9994)
print("Molecular Weight of Carbohydrate ",molewgt)
