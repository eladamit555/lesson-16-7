#start
max_number = int(input('Enter a number:'))
i = 1
while i <= max_number:
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
            print('fizz')
    elif i % 5 == 0:
            print('buzz')
    else:
        print(i)
    i += 1

#stop