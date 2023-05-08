def Lugat_tuz(ism, familiya, tugil_yil, tugil_joy, email = '', tel_raqam = '', hozir_yil = 2023):
    """ma'lum bir ma'lumotlarni to'plab lug'at qaytaruvchi funksiya"""
    mijoz = {
        'ism': ism.title(),
        'familiya': familiya.title(),
        'tugilgan yil': tugil_yil,
        'tugilgan joy': tugil_joy.capitalize(),
        'email': email,
        'telefon raqam': tel_raqam,
        'yosh': hozir_yil - tugil_yil
    }
    return mijoz

print("Mijozlar ro'yhatini shakillantiramiz.")
mijozlar = []
while True:
    print("Mijoz haqida ma'lumotlar.",end="\n")
    ism = input("Mijoz ismi: ")
    familiya = input("Mijoz familiyasi: ")
    tugil_yil = int(input("Mijoz tug'ilgan yil: "))
    tugil_joy = input("Mijoz tug'ilgan joy: ")
    email = input("Mijoz emaili (shart emas): ")
    tel_raqam = input("Mijoz telefon raqami (shart emas): ")
    mijozlar.append(Lugat_tuz(ism, familiya, tugil_yil, tugil_joy, email, tel_raqam))
    javob = input("Yana maijoz kiritasizmi(ha/yo'q): ")
    if javob == 'yo\'q':
        break

print(mijozlar)