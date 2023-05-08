# dars-8 Ro'yxatlar bilan ishlash
# 31/01/2023


############################ .sort() ro'yxatni alfavit bo'yicha saralab beradi 
# cars = ['bmw', 'toyota', 'gm', 'chevrolet', 'ford', 'hyundai', 'audi']
# cars.sort()                            ### asl ro'yxatni o'zgartiradi (cars)
############################ .sort(reverse=True) ro'yxatni alfavitka teskari saralab beradi 
# cars.sort(reverse=True)                ### asl ro'yxat o'zgaradi (cars)
# print(cars)

########################### sorted() asl ro'yxatni o'zgartirmagan holda chiqariladi
# print(sorted(cars))
# print(sorted(cars, reverse=True))

########################## .reverse() ro'yxatni teskari qilib tuzib beradi (6, 4, 3, 2) >>> (2, 3, 4, 6)
# print(cars)
# cars.reverse()
# print(cars)

######################### len() ro'yxatning uzunligini, nechtaligini chiqarib beradai
# number = [5, 2, 25, 65, -5, 32, 14]
# print(len(number))
# print(len(cars))

######################## range() belgilangan qiymatdan belgilangan qiymatgacha bo'lgan sonlarni shakilantirib beradi
# range(0,10)
# number = list(range(0,10))  ### 0 dan 10 gacha sonlarni ro'yxatini tuzadi
# print(number)

# toq_sonsal = list(range(1,10,2))  ### 1 dan 10 gacha bo'lgan sonlarni har 2 chisini ro'yxatini tuzadi (toq sonlarni)
# print(toq_sonsal)
# juft_sonlar = list(range(0,10,2))  ### 0 dan 10 gacha bo'lgan sonlarni har 2 chisini ro'yxatini tuzadi (juft sonlarni)
# print(juft_sonlar)

# max_qiymat = max(juft_sonlar)
# print(max_qiymat)

# ######################## max(), min() va sum()
# narxlar = [22000, 55000, 12000, 500, 6000, 89000, 25000]
# max_narx = max(narxlar)
# min_narx = min(narxlar)
# jami = sum(narxlar)
# print(f'Eng qimmat narx {max_narx}, eng arzon narx {min_narx}, umumiy qiymati {jami}')

########################## 
# cars = ['bmw', 'toyota', 'gm', 'chevrolet', 'ford', 'hyundai', 'audi']
# print(cars)
# print(cars[0:4])
# print(cars[:3])
# print(cars[2:])

######################### Ro'yxatdan nusxa olish usuli. Agar nusxa olinmasa olingan ro'yxatga o'zgartirish kiritilsa asl nusxa ham o'zgaradi ###
# cars = ['bmw', 'toyota', 'gm', 'chevrolet', 'ford', 'hyundai', 'audi']
# print(cars)
# ######## my_cars = cars XXXX ##########
# my_cars = cars[:]
# my_cars.remove('gm')
# my_cars.insert(1, "tesla")
# print(my_cars)
# print(cars)

######################## TUPLE - o'zgarmas ro'yxat

# toys = ("ayiqcha", 'qo\'g\'irchoq', 'mashina', 'robot', 'kopto\'k')  ### bu o'zgarmas ro'yxat
# toys = list(toys)                                                    #### o'zgarmas ro'yxatni o'zgaruvchanga o'tkazildi
# print(type(toys))
# print(toys)

# toys.append('lego')
# del toys[1]
# toys.insert(0, 'phon')
# print(toys)
# toys = tuple(toys)
# print(toys)

##########################################################   AMALIYOT   #############################################################

################################################################################ 1-O'zingizga ma'lum davlatlarning ro'yxatini tuzing 
# davlatlar = ['germaniya', 'italiya', 'angliya', 'xitoy','amerika', 'rassiya']

###################### 2 - ro'yxatni konsolga chiqaring
# print(davlatlar)       

###################### 3 - Ro'yxatning uzunligini konsolga chiqaring
# print(len(davlatlar))

###################### 4 - sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
# print(sorted(davlatlar))

###################### 5 - sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
# print(sorted(davlatlar, reverse=True))

###################### 6 - Asl ro'yxatni qaytadan konsolga chiqaring
# print(davlatlar)

###################### 7 - reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# davlatlar.reverse()
# print(davlatlar)

###################### 6 - sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)

###################### 7 - 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# sonlar = list(range(120, 1200, 2))
# print(sonlar)

###################### 8 - Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# sum = sonlar
# print(sum(sonlar))

###################### 9 - Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# print(max(sonlar)-min(sonlar))

###################### 10 - Ro'yxatdagi elementlar sonini hisoblang
# print(len(sonlar))

###################### 11 - Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
# print(sonlar[:20])
# print(sonlar[260:280])
# print(sonlar[520:540])

###################### 12 - taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = []
taomlar.append('Osh')
taomlar.append('Norin')
taomlar.append('Xasib')
taomlar.append('Halim')
taomlar.append('Sho\'rva')
print(taomlar)

###################### 13 - nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = []
nonushta = taomlar[:]

###################### 14 - Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove('Halim')
del nonushta[3]
nonushta.insert(0, 'Non')
nonushta.insert(0, 'Issiq choy')

###################### 15 - Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(taomlar)
print(nonushta)

###################### 16 - Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
print(nonushta)
nonushta = list(nonushta)
nonushta[0] = "Qaymoq va non"
nonushta = tuple(nonushta)
print(nonushta)