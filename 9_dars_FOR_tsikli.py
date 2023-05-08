5# 9 - dars FOR tsikli bilan tanishamiz
# 06/02/2023
''' for BILAN TANISHAMIZ
 Dasturlash davomida kodimizning biror qismini bir necha marta takrorlash talab etilishi mumkin. Misol uchun, 
 ro'yxat ichidagi har bir elementni alohida qatordan konsolga chiqarish, yoki bo'lmasa har bir elementni kvdartaga oshirish va hokazo. 
 Mana shunday vaziyatlarda bizga for operatori yordam beradi. Dasturlashda bu tsikl (loop) deb ataladi. 
 Keling quyidagi misolni ko'ramiz. Bizda mehmonlar ro'yxati bor, biz har bir mehmonning ismini yangi qatordan chiqarmoqchimiz. Buning uchun quyidagi kodni yozamiz:
'''
##################################################################### For
# mehmonlar = ['Vali', 'Bobur', 'Farrux', 'Ali', 'Rustam', 'Jasur']
# for mehmon in mehmonlar:
# 	# print('Salom', mehmon)
# 	print(f'Hurmatli, {mehmon} sizni 11-fevral kuni nahorga oshga taklif qilamiz')
# 	print('Hurmat bilan O\'lmasovlar oilasi')

#####################################################################
# sonlar = list(range(1, 20, 2))
# for son in sonlar:
# 	print(f'{son} ning kvadrati {son**2} ga teng')

#####################################################################
# sonlar = list(range(0,20,2))
# sonlar_kvadrati = []
# for son in sonlar:
# 	sonlar_kvadrati.append(son**2)

# print(sonlar)
# print(sonlar_kvadrati)

#####################################################################
# dostlar = []
# for n in range(5):
# 	dostlar.append(input(f'{n+1}-dostingizni kiriting: '))
# print(dostlar)

##################################################################### AMALIYOT ##############################################################################

################################################## 1
# ismlar = ['Zik', "Martin", 'Vin', 'Jek', 'Frad']
# for talaba in ismlar:
# 	print(f'Hurmatli {talaba} o\'qish 1-sentyabrda boshlanadi')

# ################################################## 2
# print(f'Kod {len(ismlar)} marta takrorlandi')

# ################################################## 3
# sonlar = list(range(11, 100, 2))
# for son in sonlar:
# 	print(son**3)

################################################## 4
# kinolar = []
# for n in range(5):
# 	kinolar.append(input(f'{n+1}-Eng sevimli kinoingizni kiriting: '))
# print(kinolar)

################################################## 5

n_odamlar = int(input('Nechta odam bilan suxbatlashdingiz: '))
ismlar = []
for n in range(n_odamlar):
    ismlar.append(input(f'{n+1}-odamning ismini kiriting: '))
print(ismlar)