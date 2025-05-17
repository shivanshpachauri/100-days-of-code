# file not found error

# try:
#     with open("file.txt") as file:
#         file.read()
    
# except FileNotFoundError as fe:
#     with open("file.txt",mode="w") as file:
#         file.write("shivansh pachauri")
# with open("shivansh_pachauri.txt") as file:
#     file.read()
        
# key error
# try:
#     dict2={
#         "a":1,
#         "b":2
#     }
#     dict2["shivansh"]
# except KeyError:
#     dict2["shivansh"]='shivansh'
#     print(dict2)

# index error

# a=[1,2,3,4]
# print(a[4])
# try:
#     a=[1,2,3,4]
#     print(a[4])
# except IndexError:
#     a.append(4)
#     print(a[4])

# type - error
# try:
#     a="shivansh"
#     a=a+2
# except TypeError:
#     a=f"{a}2"
#     print(a)

try:
    # typerror
    a="shivansh"
    a=a+2
    # indexerror
    a=[1,2,3,4]
    print(a[4])
    # keyerror
    dict2={
        "a":1,
        "b":2
    }
    dict2["shivansh"]
    # filenotfound
    with open("file2.txt") as file:
        file.read()
except FileNotFoundError as fe:
    print("file not found error",fe)
except KeyError as ke:
    print("key error",ke)
except IndexError as ie:
    print("index error",ie)
except TypeError as te:
    print("typerror ",te)
else:
    print("error occured")