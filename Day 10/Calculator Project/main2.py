import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

def subtract(n1,n2):
    return n1-n2
dict={}
should_stop=False
while(should_stop!=True):
    
    try:
        n1=float(input("Enter first number=\n"))
        n2=float(input("Enter second number=\n"))
        
        dict={"+":add(n1,n2),"-":subtract(n1,n2),"/":divide(n1,n2),"*":multiply(n1,n2)}
        # yes_no={"y",}
        print("Enter operation to perform \n +\n -\n/\n*")
        operation=input()
        for i in dict:
            if operation==i:
                print("output\n",dict[i])
                user_input=input("enter y for yes n for no\n").lower()
                if user_input=='n':
                    should_stop=True
    except ZeroDivisionError as ze:
        print("value undefined not division by zero",ze)
    except ValueError as ve:
        print("enter a valid value without string or special character",ve)

