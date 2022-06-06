from math import*


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

b = input('Введите простое выражение, содержащие максимум 2 значения, через пробел(Чтобы закончить напишите stop):')

while b != 'stop':
    b = b.split()

    if b[1] == '!':
        b.append('0')

    if b[0] == 'res':
        b[0] = res
    if b[2] == 'res':
        b[2] = res

    if b[0] == 'pi':
        b[0] = pi
    if b[2] == 'pi':
        b[2] = pi

    if b[0] == 'e':
        b[0] = e
    if b[2] == 'e':
        b[2] = e

    if is_number(b[0]) is False or is_number(b[2]) is False:
        print('Пожалуйста, введите цифры и символы операции.')
    else:
        if b[1] == '-':
            c = float(b[0]) - float(b[2])
            print('Ответ:', int(c))
        elif b[1] == '+':
            c = float(b[0]) + float(b[2])
            print('Ответ:', int(c))
        elif b[1] == '/':
            c = float(b[0]) / float(b[2])
            print('Ответ:', c)
        elif b[1] == '*':
            c = float(b[0]) * float(b[2])
            print('Ответ:', c)
        elif b[1] == '^':
            c = float(b[0]) ** float(b[2])
            print('Ответ:', int(c))
        elif b[1] == '-/':
            c = float(b[0]) ** (1./float(b[2]))
            print('Ответ:', c)
        elif b[1] == '!':
            x = 0
            c = 1
            while x != (int(b[0]) - 1):
                v = (int(b[0]) - x)
                x += 1
                c *= v
            print('Ответ:', c)
        res = str(c)
    b = input('Введите простое выражение, содержащие максимум 2 значения, через пробел:')
