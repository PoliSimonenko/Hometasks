a = input('Введите число:')
while True:
    for d in a:
        if d == '.' or d == ',':
            a = a.replace(d,'')
    a = list(a)
    if a[0] == '-':
        del a[0]
        a = ''.join(a)
        if a.isdigit() == True:
                print('Отрицательное')
        else:
            print('Должно быть число!')
    else:
        a = ''.join(a)
        if a.isdigit():
            if a == '0':
                print('Ноль')
            else:
                print('Положительное')
        else:
            print('Должно быть число!')
    a = input('Введите число:')
