zurnalas = []

atlyginimas = float(input("Įvesti šio men. atlyginimą: "))
atlyginimo_mokestis_proc = int(input("Įvesti mokeščio procentų dydį"))

balansas = atlyginimas * (1 - atlyginimo_mokestis_proc / 100)
zurnalas.append(balansas)


while True:

    print('Porgramų pasirinkimas: Kuras(1), Blanasas(2), Buto nuoma(3), Dienos išlaidos(4), Pramogos(5)')
    pasirinkimas = int(input("Įveskite pageidautina programą: "))

    if pasirinkimas == 1:
        kuras = int(input("Jūsų mašinos sunaudotas kuras litrais per mėnesį: "))
        zurnalas.append(kuras)
        print(f"Jūsų kuro išlaidos: {kuras}")

    elif pasirinkimas == 2:
        pass
    elif pasirinkimas == 3:
        pass
    elif pasirinkimas == 4:
        pass
    elif pasirinkimas == 5:
        pass

    break 