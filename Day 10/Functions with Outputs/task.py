def format_name(f_name,l_name):
    f_name=f_name.title()
    l_name=l_name.title()
    return f_name+" "+l_name
fname=input("Enter your first name = \n")
lname=input("enter your second name = \n")


print(format_name(fname,lname))