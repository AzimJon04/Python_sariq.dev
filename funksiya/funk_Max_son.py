def Max_son(a, b):
    """funksiya ikkta parametr oladi va ularnni katta - kichligini aniqlaydi"""
    if a > b:
        print(f'{a} katta')
    elif a < b:
        print(f'{b} katta')
    else:
        print(f'{a} va {b} birbiriga teng')

a, b = map(int, input().split())
Max_son(a, b)
