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

should_stop=False
while(should_stop!=True):
    try:
        n1=float(input("Enter first number=\n"))
        n2=float(input("Enter second number=\n"))
        print("Enter operation to perform \n +\n -\n/\n*")
        operation=input()
    
        if operation=="+":
            print("added value=",add(n1,n2))
            user_input=input("\n enter y if you want to continue n for no\n").lower()
            if user_input=='n':
                should_stop=True
        elif operation=="*":
            print("multiplied value",multiply(n1,n2))
            user_input=input("\n enter y if you want to continue n for no\n").lower()
            if user_input=='n':
                should_stop=True
        elif operation=="-":
            print("subtracted",subtract(n1,n2))
            user_input=input("\n enter y if you want to continue n for no\n").lower()
            if user_input=='n':
                should_stop=True
        elif operation=="/":
            print("divided value",divide(n1,n2))
            user_input=input("\n enter y if you want to continue n for no\n").lower()
            if user_input=='n':
                should_stop=True
        else:
            print("enter a valid value")
    except ZeroDivisionError as ze:
        print("enter a valid value",ze)
    except ValueError as ve:
        print("enter a valid value without string or special character",ve)

