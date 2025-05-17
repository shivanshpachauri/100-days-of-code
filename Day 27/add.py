def add(*args):
    try:
        sum=0
        li=args
        for i in li:
            sum=sum+i
        return sum
    except TypeError as te:
        print("incompatible data type error ",te)
print(add(1,2,3,4,5,6,None))