#start
while True:
    a = float(input('a'))
    b = float(input('b'))
    c = float(input('c'))

    if a <= 0 or b <= 0 or c <= 0:
        break
    if a + b <= c or a + c <= b or b + c <= a:
        break
    print('sum of sides', a + b + c)
    print('next triangle')

print('bye bye')
#stop
