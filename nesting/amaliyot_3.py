kinolar = {}
for odam in range(4):
    ism = input('Salom, ismingizni yozing: '.title())
    print(f"{ism} yoqtirgan 3 ta kino nomini kiriting:")
    toplam = []
    for kino in range(3):
        toplam.append(input(f"{kino+1} - kino nomi: ".title()))
    kinolar[ism] = toplam
print(kinolar)
for shaxs in kinolar.keys():
    print(f'{shaxs}ning sevimli kinolari:')
    for kinom in kinolar[shaxs]:
        print(kinom)