while True:

    nome = input("Nome completo: ")

    partes = nome.split()

    print("-"*30)

    if len(partes) >= 2:
        print(f"Nome completo: {nome}")
        print(f"Nome no cracha: {partes[0].upper()}")
        break
    else:
        print(f"Nome completo: {nome}")
        print("Ops... Por favor, informe o nome completo")

    print("-"*30)
    