x=int(input("Enter the no of candy"))
x<200
if (x%5==2 and x%6==3 and x%7==2):
    print("You win all candy")
else:
    print("Better Luck next time")
m=1
n=1
o=1
for i in range(0,20,1):
    k=(m*i+2)%5==2
    l=(n*i+2)%6==3
    m=(m*i+2)%7==2
    if(k==l==m):
        print(k)
    
    
    







marks=int(input("Enter Marks "))
if marks<25:
    print("F")
if 25<=marks<45:
    print("E")
if 45<=marks<50:
    print("D")
if 50<=marks<60:
    print("C")
if 60<=marks<80:
    print("B")
if marks>80:
    print("A")





year=int(input("Write Year "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("It's Leap Year ")
        else:
            print("Not Leap Year")
    else:
        print("It's Leap Year ")

else:
    print("Not Leap Year ")







q1=int(input("Question 1: 3 x 4 =  "))
if q1==12:
    print("Right!")
else:
    print("Wrong. The answer is 12")
    
q2=int(input("Question 2: 3 x 6 =  "))
if q2==18:
    print("Right!")
else:
    print("Wrong. The answer is 18")
    
q3=int(input("Question 3: 9 x 4 =  "))
if q3==36:
    print("Right!")
else:
    print("Wrong. The answer is 36")
    
q4=int(input("Question 4: 7 x 9 =  "))
if q4==63:
    print("Right!")
else:
    print("Wrong. The answer is 63")
    
q5=int(input("Question 5: 3 x 8 =  "))
if q5==24:
    print("Right!")
else:
    print("Wrong. The answer is 24")
    
q6=int(input("Question 6: 2 x 9 =  "))
if q6==18:
    print("Right!")
else:
    print("Wrong. The answer is 18")
    
q7=int(input("Question 1: 8 x 9 =  "))
if q7==72:
    print("Right!")
else:
    print("Wrong. The answer is 72")
    
q8=int(input("Question 8: 5 x 9 =  "))
if q8==45:
    print("Right!")
else:
    print("Wrong. The answer is 45")
    
q9=int(input("Question 1: 7 x 8 =  "))
if q9==56: 
    print("Right!")
else:
    print("Wrong. The answer is 56")
    
q10=int(input("Question 10: 6 x 9 =  "))
if q10==54:
    print("Right!")
else:
    print("Wrong. The answer is 54")





























