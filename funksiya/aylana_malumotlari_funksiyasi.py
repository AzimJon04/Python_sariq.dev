def Aylana_paramet(radius):
    """aylana radiusini qabul qilib uning boshqa parametrlarini qaytaruvchi funksiya"""
    ay_parametr = {
        'Aylana radiusi (m)': radius,
        "Aylana diametri (m)": radius*2,
        "Aylana uzunligi (m)": 2*3.14*radius,
        "Aylana yuzasi (m2)": 3.14*(radius**2)
    }
    return ay_parametr

radius = float(input("Aylana radiusini kiriting (m): "))
print(Aylana_paramet(radius))