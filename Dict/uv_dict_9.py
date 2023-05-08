menu = {
    'osh': 30000,
    'somsa': 8000,
    'lag\'mon': 28000,
    'chuchvara': 25000,
    'norin': 25000,
    'hasib': 26000,
    "halim": 32000,
    'manti': 6000,
    'shashlik': 12000,
    'kabob': 30000
}
print('3 ta ta\'om buyurtma bering!')
taom = []
for ovqat in range(3):
    taom.append(input(f'{ovqat+1} - ta\'om: '))
for narx in taom:
    sum = menu.get(narx.lower())
    if sum == None:
        print(f"Kechirasiz, bizda {narx} yo\'q")
    else:
        print(f"{narx} - {sum}")
