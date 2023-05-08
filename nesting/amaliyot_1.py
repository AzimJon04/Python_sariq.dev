adab = {
    'ism': 'alisher',
    'fam': 'navoiy',
    'tyil': '1441-yil',
    'tjoy': 'xirot',
    'umr': '60 yil'
}
adab1 = {
    'ism': 'erkin',
    'fam': 'vohidov',
    'tyil': '1963-yil',
    'tjoy': 'farg\'ona',
    'umr': '80 yil'
}
adab2 = {
    'ism': 'abdulla',
    'fam': 'qoditiy',
    'tyil': '1894-yil',
    'tjoy': 'toshkent',
    'umr': '44 yil'
}
adab3 = {
    'ism': 'abu abdulloh Muhammad',
    'fam': 'ibn ismoil',
    'tyil': '810-yil',
    'tjoy': 'buxoro',
    'umr': '60 yil'
}
shaxslar = [adab, adab1, adab2, adab3]
for shaxs in shaxslar:
    print(f'{shaxs["ism"].title()} {shaxs["fam"].title()} {shaxs["tyil"]}da {shaxs["tjoy"].title()}da tavallud topgan. {shaxs["umr"]} umir ko`rgan.')