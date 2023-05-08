Python = {
    "string": 'matin',
    "integer": "butun son",
    "float": "haqiyqiy son",
    "if": "tarmoqlanadigon operator",
    "while": "takrorlanadigon operator",
    "for": "takrorlanadigan operator"
}
soz = input('Kalit so\'z kiriting: ')
if soz in Python:
    print(Python[soz])
else:
    print('Bunday so\'z mavjud emas')