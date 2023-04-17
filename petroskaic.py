atlyginimas = 1600

print("Jusu atlyginimas: " + str(atlyginimas))

perdiena = float(input("Kiek išleidžiate per dieną: "))


dienos = 0

while atlyginimas > 0:
    atlyginimas = atlyginimas - perdiena
    dienos = dienos + 1

    
print("Reikės", dienos, "kad išleistumėte visą atlyginimą" )
