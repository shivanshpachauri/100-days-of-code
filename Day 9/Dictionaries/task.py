# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}
student_scores = {
    'Harry': 88,
    'Ron': 78,
    "shivansh":71,
    'Hermione': 91,
    'Draco': 75,
    'Neville': 60
}
student_grades ={}
for key in student_scores:
    if(student_scores[key]>=91):
        student_grades[key]="Outstanding"
    elif(student_scores[key]>=81):
        student_grades[key]="Exceeds Expectations"
    elif(student_scores[key]>=71):
        student_grades[key]="Acceptable"
    else:
        student_grades[key]='Fail'
    # print(key)
# student_grades ={}
print(student_grades)
# student_grades =