a = input('введите строку')
b = input('введите строку')
d = input('введите строку')
g = input('введите строку')
f = open('1.txt','w')
f.write(a + '\n')
f.write(b+'\n')
f.close()
k = open('1.txt','a')
k.write(d + '\n')
k.write(g)
k.close