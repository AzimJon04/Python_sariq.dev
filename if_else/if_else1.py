# yangi_cars = ['tayota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in yangi_cars:
#     if car == "gm":
#         print(car.upper())
#     else:
#         print(car.title())
#======================================================================#
# yangi_cars = ['tayota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in yangi_cars:
#     if car != "gm":
#         print(car.title())
#     else:
#         print(car.upper())
#=====================================================================#
# login = input('Loginingizni kiriting: ')
# if login.lower() == 'admin':
#     print('Xush kelibsiz, Admin. Foydalanuvchilar ro\'yxatini ko\'rasizmi')
# else:
#     print(f'Xush kelibsiz, {login.title()}!')
#=====================================================================#
# a, b = map(int, input('Ikkta son kiriting: ').split())
# if a == b:
#     print('Sonlar teng')
# print(f'{a} {b} dan katta') if a > b else print(f'{a} dan {b} katta')
#=====================================================================#
# i = int(input('Istalgan son kiriting: '))
# if i < 0:
#     print('Manfiy son')
# else:
#     print('Musbat son')
#=====================================================================#
i = int(input('Istalgan son kiriting: '))
if i > 0:
    print(int(i**(1/2)))
else:
    print('Musbar son kiriting')