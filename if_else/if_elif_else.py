#==================================================================#
# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input('Nima ovqat yeysiz?: ')
# if ovqat.lower() in menu:
#     print("Buyurtmangiz qabul qilindi.")
# else:
#     print('Afsuski bizda bunday ovqat yo\'q')
#==================================================================#
# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']
#
# for taom in buyurtmalar:
#     if taom in menu:
#         print(f'Menuda {taom} bor')
#     else:
#         print(f'Menuda {taom} yo\'q')
#=================================================================#
'''Foydalanuvchidan juft son kiritishni so'rang.
Agar foydalanuvchi juft son kiritsa "Rahmat!",
 agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.'''

# j = int(input('Juft son kiriting: '))
# if j%2 == 0:
#     print('Rahmat!')
# else:
#     print('Bu juft son emas.')
#=================================================================#
'''Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm'''

# yosh = int(input("Yoshingiz nechida: "))
# if yosh <= 4 or yosh >=60:
#     print('Muzeyga kirish uchun chipta bepul')
# elif 4 < yosh <= 18:
#     print("Muzeyga kirish uchun chipta 10,000 so'm")
# elif yosh > 18:
#     print('Muzeyga kirish uchun chipta 20,000 so\'m')
#====================================================================#
'''Foydalanuvchidan ikita son kiritishni so'rang,
sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring'''

# a = int(input('Birinchi sonni kiriting: '))
# b = int(input('Ikkinchi sonni kiriting: '))
# if a > b:
#     print(f'{a} > {b}')
# elif a == b:
#     print(f'{a} = {b}')
# else:
#     print(f'{a} < {b}')
#====================================================================#
'''mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.
Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta
mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan
solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda,
"Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring'''

# mahsulotlar = ['anor', 'nok', 'kivi', 'olma', 'jo\'xori', 'limon', 'gril', 'go\'sht', 'guruch', 'piyoz']
# savat = []
# for n in range(1, 6):
#     savat.append(input(f'Savarga {n} - mahsulotni qo\'shing: '))
# for s in savat:
#     if s.lower() in mahsulotlar:
#         print(f'Do\'konimizda {s} bor')
#     else:
#         print(f'Do\'konimizda {s} yo\'q')
#====================================================================#
'''Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang.
Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga,
do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.
Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor"
degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.'''

# mahsulotlar = ['anor', 'nok', 'kivi', 'olma', 'jo\'xori', 'limon', 'gril', 'go\'sht', 'guruch', 'piyoz']
# savat = []
# for n in range(1, 6):
#     savat.append(input(f'Savarga {n} - mahsulotni qo\'shing: '))
# bor_mahsulotlar = []
# yoq_mahsulotlar = []
# for s in savat:
#     if s.lower() in mahsulotlar:
#         bor_mahsulotlar.append(s)
#     else:
#         yoq_mahsulotlar.append(s)
# if yoq_mahsulotlar:
#     print(f'Do\'konimizda quyidagi mahsulotlar yo\'q:')
#     for yoq in yoq_mahsulotlar:
#         print(yoq)
# else:
#     print('Siz so\'ragan barcha mahsulotlar do\'konimizda bor')
#=================================================================#
'''foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing.
Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan
loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring.
Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!"
aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.'''

# foydalanuvchilar = ['admin', 'jek', 'deep', 'kiki', 'lolo']
# yangi_log = input('Yangi login tanlang: ')
# if yangi_log.lower() in foydalanuvchilar:
#     print('Login band, yangi login tanlang!')
# else:
#     print('Xush kelibsiz, foydlanuvchi!')
#=================================================================#
'''Foydalanuvchidan biror butun son kiritishni so'rang.
Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga 
qoldiqsiz bo'linishini konsolga chiqaring. '''

# s = int(input('Istalgan butun son kiriting: '))
# for y in range(2, 11):
#     if not (s%y):
#         print(f'{s} soni {y} soniga qoldiqsiz bo\'linadi')









