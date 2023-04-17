zurnalas = []

atlyginimas = float(input("Įvesti šio men. atlyginimą: "))
atlyginimo_mokestis_proc = float(input("Įvesti mokeščio procentų dydį: "))

balansas = atlyginimas * (1 - atlyginimo_mokestis_proc / 100)
zurnalas.append(balansas)


while True:

    print('Porgramų pasirinkimas: Kuras(1), Blanasas(2), Buto nuoma(3), Dienos išlaidos(4), Pramogos(5), Iseiti(6)')
    pasirinkimas = int(input("Įveskite pageidautina programą: "))

    if pasirinkimas == 1:
        kuras = int(input("Įveskite suma kuria išleidžiate kurui: "))
        zurnalas.append(-kuras)
        print(f"Jūsų kuro išlaidos: {kuras}")

    elif pasirinkimas == 2:
        print(f'Jūsu dabartinis balansas: {balansas}')

    elif pasirinkimas == 3:
        butas = int(input('Įveskite buto nuomos išlaidas: '))
        zurnalas.append(-butas)
        print(butas)
    elif pasirinkimas == 4:
        pass
    elif pasirinkimas == 5:
        pass
    elif pasirinkimas == 6:
        print('Geros dienos')
        break