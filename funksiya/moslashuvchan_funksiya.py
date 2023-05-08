def Kopaytrma(*sonlar):
    """Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya"""
    kopaytr = 1
    for son in sonlar:
        kopaytr *= son
    return kopaytr


print(Kopaytrma(5, 6, 8, 6, 7, 2, 6, 3, 6, 4))
