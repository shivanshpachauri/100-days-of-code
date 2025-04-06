import random
names=["alex","beth","caroline","eleanor","dave","freddie"]
list4={
    student:random.randint(0,100) for student in names
}
print(list4)
passed={
    student:marks for (student,marks) in list4.items() if marks >=60
}
print(passed)