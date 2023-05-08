def Max_son(a, b, c):
    """uchta son qabul qilib ulardan kattasini qaytaruvchi funksiya"""
    maks = a
    if maks < b:
        maks = b
    if maks < c:
        maks = c
    return maks
    # sonlar = [a, b, c]
    # return max(sonlar)

x, y, c = map(int, input("Uchta son kiriting: ").split())
max_son = Max_son(x, y, c)
print(max_son)