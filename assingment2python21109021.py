#1.a
string="Python is a case sensitive language"  #given input string
length=len(string)
print(length)   #print length

#1.b
#reverse the string
revese=string[length::-1]
print(revese)

#1.c
#print specific part of string
y=string.index('a')
an=slice(y,length-9)
print(string[an])


#1.d
#replace substring
z=string.replace("a case sensitive", "object oriented")
print(z)

#1.e
#index of substring
ind=string.index('a')
print(ind)

#1.f
#remove white space
delete=string.replace(" ","")
print(delete)



#2
name="Shashwat Rai"
sid="21109021"
department="Production"
cgpa=9.9
f1="Hey,{} Here!"
f2="My SID is {}"
f3="I am from {} department and my CGPA is {}"
c1=f1.format(name)
c2=f2.format(sid)
c3=f3.format(department,cgpa)
print(c1)
print(c2)
print(c3)



#3
a=56
b=10
#a
print
(a&b)
#b
print(a|b)
#c
print(a^b)
#d
print(a<<2,b<<2)
#e
print(a>>2,b>>4)



#4
string = input("Enter a String ; ")
if "name" in string:
    print("yes")
else:
    print("No")



#5
a = int(input("Enter side a of triangle :"))
b = int(input("Enter side b of triangle : "))
c = int(input("Enter side c of triangle : "))
while  (a<=b+c and (b<=a+c) and c<=b+a):
    print('yes')
    break
else:
    print('no')

#6
#Count number of bits to be flipped to convert A into B
# Function that count set bits
a = int(input("Enter first number "))
b = int(input("Enter second number "))
def countSetBits(n):
    count=0
    while n:
        count+=1
        n&=(n-1)
    return count
#Function that return count of flipped number
def FlippedCount(a,b):
    # Return count of set bits in a XOR b
    return countSetBits(a^b)
print(FlippedCount(a,b))











