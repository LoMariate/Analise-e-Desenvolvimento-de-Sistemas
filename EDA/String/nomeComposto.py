nome = input("Nome completo: ")

partes = nome.split()
tam = len(partes)

if tam < 1:
    print("Nome incompleto")
else:
    print(f"Nome completo: {nome}")
    print(f"Nome no cracha: {partes[0].upper}")
    