#1

def reverse(string):
    str = ""
    for i in string:
        str = i + str
    return str
  
string = str(input("Enter any string : "))
  
print ("The original string  is : " ,string) 
print (" The reversed string(using loops) is : " ,reverse(string))


#2
min_ran = int(input("Enter any minimum range : "))
max_ran = int(input("Enter any maximum range : "))
num = int(input("Enter any number: "))
for i in range(min_ran,max_ran):
    z=(i)%num
    if z==0:
        print(i)

#3
import math
a = int(input("Enter any first side : "))
b = int(input("Enter any second side: "))
c = int(input("Enter any third side : "))
if a<(b+c) and b<(c+a) and c<(b+a):
    s=(a+b+c)/2
    area= math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area of given combinations is ", area)
else:
    print("Area is not possible for given combinations ")

    

#4  
d=5
for i in range (0,d+1):
    for j in range(i):    
        print("*",end="")
    print()
     
    
for i in range (d-1,0,-1):
    for j in range(i):    
        print("*",end="")
    print()



#5  

alp=65
n=int(input("number of rows: "))
for i in range(n):   
    for j in range (i+1):
        ans = chr(alp)
        print(ans,end="")
        alp+=1
        if alp>90:
            alp=65
    print()



#6 
m=int(input("Enter the lower range of prime  "))
n=int(input("Enter the upper range of prime  "))
print ("The Prime Numbers in the range ",m,"and",n," are : ")  
for i in range (m,n+1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)
    


#7
for i in range(0,501):
    if (i%11)==0 and (i%7)==0:
        print(i)
        

#8 
lst = []
for i in range(0, 10):
    ele = int(input("Enter the integer value: "))
    lst.append(ele)
print(lst)
pos = []
neg = []
odd = []
even = []
for j in lst:
    if j>0:
        pos.append(j)
    if j<0:
        neg.append(j)
    if(j%2!=0):
        odd.append(j)
    if(j%2==0):
        even.append(j)
print(pos,"are the positive number")
print(neg,"are the negative number")
print(odd,"are the odd number")
print(even,"are the even number")
def count(lst):
    counts = dict()
    for word in lst:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(count(lst))
 
  

 

#9
lst=[]
n=int(input("Enter the no of element in list: "))
for i in range(n):
    ele = str(input("Enter any value: "))  
    lst.append(ele)
def count(lst):
    counts = dict()
    for word in lst:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(count(lst))


