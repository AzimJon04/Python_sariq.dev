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
print("Dunyo davlatlari:")
for k in sorted(davlatlar.keys()):
    print(k.upper())
print("Dunyo davlatlarining poytaxtlari:")
for q in sorted(davlatlar.values()):
    print(q.title())