def Talaba(ism, familiya, **malumotlat):
    """Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya"""
    malumotlat['Ismi'] = ism.title()
    malumotlat["Familiyasi"] = familiya.title()
    return malumotlat

talaba1 = Talaba('alisher', 'nematulayev', Tugilgan_yili = 1995, Yashash_joyi = 'Pskent', Bahosi = '5')
print(talaba1)
