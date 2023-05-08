# STRING (matn) —Pythondagi eng mashxur ma'lumot turlaridan biri.

# ism = "Azimjon"

# Shahar = 'Pskent'
# Viloyat = 'Toshkent'
# matn = "Men yangi 📱 oldim"
# smayl = "😎"
# print(matn)

######################## 	String ustida amallar

# ism = "Azimjon"
# print("Mening ismim" + ism)

# ism = "Azimjon"
# familiya = "Abdikarimov"
# print(ism + familiya)
# print(ism +' '+ familiya)

# ism = "Azimjon"
# familiya = "Abdikarimov"
# ism_sharif = f"{ism} {familiya}"    ########### f'' - ikki va undan ko'p matin ko'rinishidagi O'ZGARUVCHILARNI birlashtirish uchun qo'llaniladi
# print(ism_sharif)

########################### Maxsus belgilar

# print("Bayraming bilan megajin")   
# print("Bayraming bilan \tmegajin") ########## \t - so'zning oldiga bo'shliq qo'shib beradi
# print("Bayraming bilan \nmegajin")   ######## \n - so'ni yangi qatorga tushirib beradi
# print("Bayraming \nbilan \tmegajin")

############################### String metodlari

# Ovqat = "Halim"
# Meva = "apelsin"
# Ovqat_meva = f'{Meva} {Ovqat}'
# print(Ovqat_meva.upper())   ####### upper() - matinnig hamma so'zlarini birinchi harfini katta qilib chiqaradi

# Ovqat = "Halim"
# Meva = "apelsin"
# Ovqat_meva = f'{Meva} {Ovqat}'
# print(Ovqat_meva.lower())    ####### lower() - matinnig hamma harflari va so'zlarini kichkina qilib chiqaradi

# Ovqat = "Halim"
# Meva = "apelsin"
# Ovqat_meva = f'{Meva} {Ovqat}'
# print(Ovqat_meva.title())    ####### title() - matinnig har bir so'zining birinchi harfini katta qilib chiqaradi

# Ovqat = "Halim"
# Meva = "apelsin"
# Ovqat_meva = f'{Meva} {Ovqat}'
# print(Ovqat_meva.capitalize())  ############ capitalize() - matinnig faqatgina birinchi so'zining birinchi harfini katta qilib chiqaradi

# print("Ovqat_meva".upper()) 

# meva = "     Apelsin     "
# print(f'Men {meva.lstrip()} mevasini yaxshi ko\'raman')   ############ lstrip() - matinning chap tomonidagi bo'shliqni olib tashlaydi
# print(f'Men {meva.rstrip()} mevasini yaxshi ko\'raman')   ############ rstrip() - matinning o'ng tomonidagi bo'shliqni olib tashlaydi
# print(f'Men {meva.strip()} mevasini yaxshi ko\'raman') 	############ strip()  - matinning ikkala tomonidagi bo'shliqlarni olib tashlaydi

############# INPUT - Foydalanuvchi bilan muloqot

# ism = input("Ismingiz nima?\t")
# print("Assalomu aleykum",ism)


###############     Amaliyot      ############

#1
kocha = 'Bog\'bon'
mahalla = 'Sog\'bon'
tuman = "Bodomzor"
viloyat = "Samarqand"

# #2
# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

#3
# kocha = input("Ko'changizni kiriting: ")
# mahalla = input("Mahallangizni kiriting: ")
# tuman = input("Tumaningizni kiriting: ")
# viloyat = input("Viloyatingizni kiriting: ")
# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")
# print(f"{kocha} ko'chasi,\n{mahalla} mahallasi,\n{tuman} tumani,\n{viloyat} viloyati")

manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())





















