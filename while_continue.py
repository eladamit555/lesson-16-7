#start
num_stud = 0
sum = 0
while True:
    grade = int(input('Enter a grade: '))
    if grade == 999:
         break
    if grade < 0 or grade > 100:
         print('Invalid grade, ignored')
         continue

    sum += grade
    num_stud += 1
print('students:', num_stud)

if num_stud > 0:
      print('average:', sum / num_stud)

#stop