#start
max_number = int(input('enter number: '))
i = 1
while i <= max_number:
    if i % 3 != 0 and i % 5 != 0 :
        print(i, end = "")
    else:
        if i % 3 == 0:
            print('fizz', end = "")
        if i % 5 == 0:
            print('buzz', end = "")
    i = i + 1
    print(' ', end = "")

#stop