#start
num_stud = int(input('number of students:'))

i = 0
max_grade = 0

while True:
    i +=1
    grade = int(input('Enter a grade: '))
    if grade < 0 or grade > 100:
        print('illegal grade')
    elif grade > max_grade:
        max_grade = grade
        if max_grade == 100:
            break

    if i >= num_stud:
        break
print(max_grade)


#stop
