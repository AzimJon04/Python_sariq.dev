# 29/01/2023
# 6-dars List (Ro'yxatlar)

mevalar = ['olma', 'anjir', 'shaftoli', 'o\'rik']  ### mevalar ro'yxati (matin)
narxlar = [12000, 18000, 10900, 22000]	 ### narxlar ro'yxati (sonlar)
sonlar = ["bir", "ikki", 3, 4, 5]  	### sonlar va matn aralash
ismlar = [] 	#### bo'sh ro'yxat

# print(mevalar)
# print(narxlar)
# print(mevalar[1].title())
# print(mevalar[0].upper())
# print(narxlar[2])

# mevalar[2] = 'uzum'
# print(mevalar)
# narxlar[3] = 50000
# print(narxlar)
# print (narxlar[1] + narxlar[2])
# print(mevalar[-1])

#####################################   Elemantlarni qo'shish usullari   #######################################################

############## .append() metodi ro'yxatga element qo'shishning onson usuli, u elemantni ro'yxatning oxiriga qo'shadi
# mevalar = ['olma', 'anjir', 'shaftoli', 'o\'rik']  ### mevalar ro'yxati (matin)
# mevalar.append('ananas')
# print(mevalar)

############## .insert() Ro'yxatning istalgan joyiga yangi element qo'shish uchun foydalaniladi
# narxlar = [12000, 18000, 10900, 22000]	 ### narxlar ro'yxati (sonlar)
# narxlar.insert(2, 23000)
# print(narxlar)

############## DEL - Ro'yxatdan biror elementni INDEKSI orqali olib tashlash uchun ishlatiladi
# mevalar = ['olma', 'anjir', 'shaftoli', 'o\'rik']  ### mevalar ro'yxati (matin)
# print(mevalar)
# del mevalar[1]
# print(mevalar)

############## .remove() - ro'yxatdan biror elementni qiymati orqali olib tashlash
# mevalar = ['olma', 'anjir', 'shaftoli', 'o\'rik']  ### mevalar ro'yxati (matin)
# print(mevalar)
# mevalar.remove('olma')
# print(mevalar)

############# .pop() - ro'yxatdan bibor elementni sugurib olish
# bozorlik = ['yog\'', 'guruch', 'gosht', 'piyoz']
# mahsulot = bozorlik.pop(2)
# print(mahsulot)
# print(bozorlik)

################################################################### AMALIYOT ###############################################################################

############################################### 1
# ismlar = ["Bekzod", "Asror", "Aziz"]
# print(f'{ismlar[0]} bugun choyxona bormi?')
# print(f'{ismlar[1]} bugun choyxona borakan smendamasmisan?')
# print(f'{ismlar[2]} bugun choyxona borakan nechilada o\'tasan?')

############################################### 2
# sonlar = [6, 85, 50.6, -20]
# misol = sonlar[0] + sonlar[3]
# print(misol)
# misol1 = sonlar[1] - sonlar[2]
# print(misol1)

############################################### 3
t_shaxslar = ["Beruniy", "Xorazmiy", "Farg'oniy"]
z_shaxslar = ["Ilon Mask", "Bill Gates"]

# print(t_shaxslar)
# print(z_shaxslar)
# print(f'Men iloji bo\'lganda tarixiy shaxslardan {t_shaxslar.pop(0)} bilan va hozirgi zamonamizning mashhur shaxslaridan {z_shaxslar.pop(0)} bilan suxbatlashgan bo\'lardim')
# print(t_shaxslar)
# print(z_shaxslar)

############################################### 4
# friends = []
# friends.append('Bekzod')
# friends.append('Zuxriddin')
# friends.append('Faxriddin')
# friends.append('Azimjon')
# print(friends) 

# friends.remove("Azimjon")
# friends.remove("Faxriddin")
# print(friends)

# friends.insert(0, "Diyor")
# friends.insert(8, 'Shox')
# print(friends)

############################################## 5
# friends = []
# friends.append('Bekzod')
# friends.append('Zuxriddin')
# friends.append('Faxriddin')
# friends.append('Azimjon')
# print(friends)

# mehmonlar = []
# friends.pop(0)
# friends.pop(0)
# mehmonlar.append(friends[0])
# mehmonlar.append(friends[1])
# # mehmonlar = friends
# print(mehmonlar)
