def Baho_lugar(ismlar):
    talabalar = {}
    for talaba in ismlar:
        baho = input(f'{talaba.title()}ning bahosi: ')
        talabalar[talaba.title()] = int(baho)
    return talabalar

talaba_ismi = ['faxriddin', 'bekzod', 'zuxriddin', 'azimjon', 'shohruh']
print(Baho_lugar(talaba_ismi))
print(talaba_ismi)