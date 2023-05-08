def Katta_harf(sozlar):
    """qabul qilingan ro'yhatlarni harbir so'zlarini bosh harflarini katta qilib ro'yhat qaytaradi"""
    katt = []
    for i in sozlar:
        katt.append(i.title())
    return katt

ismlar = ['azimjon', 'farxod', 'farrux', 'ashraf']
Katta_ism = Katta_harf(ismlar)
print(Katta_ism)
print(ismlar)