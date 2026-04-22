import math

def add(x,y):
    print(f"Sum is {x+y}")
    
def substract(x,y):
    print(f"Substraction is {x-y}")
    
def multiply(x,y):
    print(f"Multiplication is {x*y}")
    
def divide(x,y):
   print(f"Division is {x/y}")
 
def square(x):
    print(f"Square is {x*x}")
     
def cube(x):
    print(f"Cube is {x*x*x}")

x=int(input("How many numbers do you want to enter or type 3 for trignometric functions:"))
if(x==2):
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))

    choice=int(input("Choose\n 1.Addition\n 2.Substraction\n 3.Multiplication\n 4.Division\n"))

    if(choice==1):
        add(num1,num2)
    
    elif(choice==2):
        substract(num1,num2)
    
    elif(choice==3):
        multiply(num1,num2)
    
    elif(choice==4):
        divide(num1,num2)
elif(x==1):
    number=int(input("Enter a Number:"))
    
    choice=int(input("Choose\n 1.Sqaure\n 2.Cube\n"))
    
    if(choice==1):
        square(number)
        
    elif(choice==2):
        cube(number)
elif(x==3):
    degree=int(input("Enter Degrees:"))
    radians=math.radians(degree)
    choice=int(input("Choose\n 1.Sin\n 2.Cos\n 3.Tan\n"))
    
    if(choice==1):
        print(f"Answer is {math.sin(radians)}")
    elif(choice==2):
        print(f"Answer is {math.cos(radians)}")
    else:
        print(f"Answer is {math.tan(radians)}")