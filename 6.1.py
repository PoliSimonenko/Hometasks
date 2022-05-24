s = b'r\xc3\xa9sum\xc3\xa9'
b = s.decode('utf -8')
print(b)
c = b.encode('Latin 1')
print(c)
v = c.decode('Latin 1')
print(v)