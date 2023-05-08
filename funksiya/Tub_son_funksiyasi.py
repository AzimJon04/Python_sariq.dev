def Tub_qaytaruvchi(n):
    """tub sonlarni chiqaruvchi funksiya"""
    tub = []
    for i in range(2, n+1):
        rec = 0
        for c in range(1, i+1):
            if i%c == 0:
                rec += 1
        if rec == 2:
            tub.append(i)
    return tub
n = int(input("Son kiriting: "))
print(Tub_qaytaruvchi(n))


# for i in range(2, 50):
#     rec = 0
#     for n in range(1, i+1):
#         if i%n == 0:
#             rec += 1
#     if rec == 2:
#         print(i)