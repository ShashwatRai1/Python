#Q1
A=int(input("Enter the first number:"))
B=int(input("Enter the second number:"))
C=int(input("Enter the third number:"))
a=(A+B+C)/3
print("The average of three numbers is:", a)


#Q2
A=int(input("Enter the gross income:"))
B=int(input("Enter the number of dependents:"))
tax_rate=0.20
std_detn=10000
dpdt_detn=3000
taxable_income=A-std_detn-dpdt_detn*B
tax=taxable_income*tax_rate
print("The tax is:", tax)



#Q3    
s=int(input("Enter the no. of seconds = "))
m=s/60
m=int(m)
r=s%60
print("minutes = ",m)
print("seconds =",r)




#Q4

X=25
Y='25'
Z=25.0
Y2=int(Y)
Z3=int(Z)
final=X+Y2+Z3
new_value=str(final)
print(new_value)


 

#Q5
from math import pi,sin,cos
deg=0
y=0
z=0
for deg in range(0,346,15):
    rad= deg*(pi/180)
    y=round(sin(rad),4)
    z=round(cos(rad),4)
    print(deg,"---",y," ",z)


 
