marks = input("please enter your marks: ")
marks = int(marks)

if marks >= 80 :
    grade = "A+"
elif marks >= 70 :
    grade = 'A'
elif marks >= 60 :
    grade = 'A-'
elif marks >= 50 :
    grade = 'B'
elif marks >= 40 :
    grade = 'D'
else:
    grade = 'F'


print('YOur grade is', grade)