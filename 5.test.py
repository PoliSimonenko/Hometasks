price={
    'f1': {'size': 23, 'cost': 15},
    'f2': {'size': 39, 'cost': 1},
    'f3': {'size': 31, 'cost': 164},
    'f4': {'size': 46, 'cost': 28}

}

print(sorted(price, key = lambda n: price[n]['size']))

characters = {
    'fred': {'xp': 52, 'loot': 9000 },
    'jack': {'xp': 26, 'loot': 4500},
    'lida': {'xp': 94, 'loot': 800},
    'karen': {'xp': 140, 'loot': 7800},
    'molly': {'xp': 68, 'loot': 700}
}

print(sorted(characters, key = lambda s: characters[s]['xp']))
