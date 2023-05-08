def Lugat_tuz(ism, familiya, tugil_yil, tugil_joy, email = '', tel_raqam = '', hozir_yol = 2023):
    """ma'lum bir ma'lumotlarni to'plab lug'at qaytaruvchi funksiya"""
    inson = {
        'ism': ism.title(),
        'familiya': familiya.title(),
        'tugilgan yil': tugil_yil,
        'tugilgan joy': tugil_joy.capitalize(),
        'email': email,
        'telefon raqam': tel_raqam,
        'yosh': hozir_yol - tugil_yil
    }
    return inson

inson = Lugat_tuz("azimjon", "abdikarimov", 1996, "toshkent vilayati", "anvarovich.96@mail.ru")
print(inson)