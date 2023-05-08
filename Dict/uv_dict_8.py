davlatlar = {
    "o'zbekiston": 'toshkent',
    "qozog'iston": "olmata",
    "qirg'iziston": "bishkek",
    "rassiya": "maskva",
    "angliya": "london",
    "italiya": "rim",
    "germaniya": "berlin",
    "xitoy": "pekin",
    "yaponiya": "tokiyo",
    "kareya": "seul"
}
poy = input('Davlat nomini kiriting: ')
print(davlatlar.get(poy.lower(), 'Bizda bunday ma\'lumot yo\'q.'))