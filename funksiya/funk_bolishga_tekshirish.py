def Bolishga_tek(n):
    """olingan parametr bo'yicha 10 gacha bo'lgan sonlarni qoldiqsiz bolinadigonlarini tekshutuvchi funksiya"""
    for i in range(2,11):
        if n%i == 0:
            print(f"{n} {i} ga qoldiqsiz bo'linadi.")
        else:
            pass

a = int(input('Son kiriting: '))
Bolishga_tek(a)