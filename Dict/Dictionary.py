talaba_0 = {
    'ism': 'alijon',
    'familiya': 'shamshiyev',
    'yosh': 22,
    'kurs': 4
}
print(talaba_0['ism'].title())
print(talaba_0.items())
#=========================================== .items()
# for kalit, qiymat in talaba_0.items():
#     print(f'kalit: {kalit}')
#     print(f'qiymat: {qiymat} \n')

# telefonlar = {
#     'ali': 'iphone x',
#     'vali': 'galaxy s9',
#     'olim': 'mi 10 pro',
#     'orif': 'nokia 3310'
# }
# for k, q in telefonlar.items():
#     print(f'{k.title()}ning telefoni {q}')

# mahsulotlar = {
#     'olma': 10000,
#     'anor': 20000,
#     'uzum': 40000,
#     'anjir': 25000,
#     'shaftoli': 30000
# }
#======================================= .keys()
# print('Do\'kondagi mahsulotlar')
# for k in mahsulotlar.keys():
#     print(k.title())

# bozorlik = ['anor', 'uzum', 'non', 'baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f'{mahsulot.title()} {mahsulotlar[mahsulot]} sum')
# for tovar in bozorlik:
#     if tovar not in mahsulotlar:
#         print(f'Iltimos do\'koningizga {tovar} ham olib keling')

# print("Do'kondagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

#======================================= .values()
# telefonlar = {
#     'ali': 'iphone x',
#     'vali': 'galaxy s9',
#     'olim': 'mi 10 pro',
#     'orif': 'nokia 3310',
#     'nodir': 'galaxy s9',
#     'kamol': 'nokia 3310',
#     'said': 'iphone 12',
#     'shox': 'poco 12 pro'
# }
# print(telefonlar.values())
# print('Foydalanuvchilar quydagi telefonlardan foydalanishadi: ')
# for telefon in telefonlar.values():
#     print(telefon)

# print('Foydalanuvchilar quydagi telefonlardan foydalanishadi: ')
# for telefon in set(telefonlar.values()):
#     print(telefon)
#
# toys = {'boll', 'car', 'lamp', 'bear', 'car', 'boll'}
# print(toys)

