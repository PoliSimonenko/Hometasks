def gh(a):
    """
        ninijdjowjwodjwo
    """
    a = a.lower()
    p = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    g = 0
    for f in p:
            s = a.count(f)
            s = str(s)
            s = len(s)
            s = int(s)
            if s > g:
                g = s
    for f in p:
        if a.count(f) > 0:
            print('| {} | {:<{}} |'.format(f, a.count(f), g))




a = input('Введите строку:')
gh(a)
print(gh.__doc__)