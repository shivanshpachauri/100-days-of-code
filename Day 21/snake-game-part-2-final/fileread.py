# file=open("data.txt")
# contents=file.read()
# print(contents)
with open ("data.txt",mode="a") as file:
    # contents=file.read()
    file.write("0 1 3")
    # print(contents)
    file.close()