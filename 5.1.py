a = int(input('Введите число:'))
s = lambda a: 'нечётное' if a % 2 != 0 else( 'ноль' if a == 0 else 'чётное' )
print(s(a))