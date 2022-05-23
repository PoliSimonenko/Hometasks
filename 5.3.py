a = ['шалаш', 'молоко','заказ','дверь']
print(list(filter(lambda i:i if i[::-1] == i[::1] else None,a)))
