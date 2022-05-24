import json

with open('evidence.json') as f:
    evid = json.load(f)

a = list(evid)
print('a:',a)
b = list(evid.values())
print('b:',b)
c = []
d = []
for i in b:
    c.append(i[0])
    d.append(i[1])
print('c:',c)
print('d:',d)
i = 0
heading = 'Phone number, Name, Age'
with open('data.csv', 'w') as f:
    f.write(heading +'\n')
    while i!= 5:
        j=[]
        j.append(a[i])
        j.append(c[i])
        j.append(d[i])
        print(j)
        l = ','.join(j)
        f.write(l +'\n')
        i+=1