def pow(num: (int, float), k: (int, float)) -> float:
    """
    Возведение в степень
    Возвращает число

    :param num Основание (Принимает только число)
    :param k Степень
    """
    return float(num ** k)


dict1 = {
    "key1": {'name': 'кросы', 'cost': 16},
    "key2": {'name': 'кросы', 'cost': 1},
    "key3": {'name': 'кросы', 'cost': 345},
    "key4": {'name': 'кросы', 'cost': 3},
    "key5": {'name': 'кросы', 'cost': 124}
}


def sorted_dict(x):
    return dict1[x]['cost']


sorted_key = sorted(dict1, key=lambda x: dict1[x]['cost'])
print(sorted_key)
for k in sorted_key:
    print(k, dict1[k]['cost'])