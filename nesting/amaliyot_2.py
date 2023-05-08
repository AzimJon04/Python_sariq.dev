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
adab['asarlar'] = ['Xamsa', 'Lison ut-Tayr', 'Mahbub Al-Qulub', 'Munojar']
adab1['asarlar'] = ['Tong nafasi', 'Qo\'shiqlarim sizga', 'O`zbegim', 'Qiziquvchan matmusa']
adab2['asarlar'] = ['O`tkan kunlar', 'Mehrobdan chayon', 'Obid ketmon']
adab3['asarlar'] = ['Al-jome` as-sahih', 'Al-adab al-mufrat', 'Al-tarix al-kabir', 'Al-tarix as-sag`ir']
shaxslar = [adab, adab1, adab2, adab3]
for shaxs in shaxslar:
    print(f"\n{shaxs['ism'].title()} {shaxs['fam'].title()}ning mashxur asarlari: ")
    for asar in shaxs['asarlar']:
        print(asar)