# def Darajasi(x, y):
#     """funksiya x vay parametrlarni olib x ni y darajasini hisoblab beradi"""
#     print(f'{x} ning {y} darajasi - {x**y} ga teng')
#
# a, b = map(int, input().split())
# Darajasi(a, b)

def Darajasi(x, y = 2):
    """funksiya x vay parametrlarni olib x ni y darajasini hisoblab beradi"""
    print(f'{x} ning {y} darajasi - {x**y} ga teng')

a = int(input())
Darajasi(a)