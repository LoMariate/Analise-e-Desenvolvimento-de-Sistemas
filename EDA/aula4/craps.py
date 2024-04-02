import random

while True:
    opcao = input("Deseja jogar Craps? (s/n) ")
    if opcao.lower() == "n":
        break
    elif opcao.lower() != "s":
        print("Opção Inválida. Tente Novamente!")
        continue
    
    nome = input("Informe seu nome: ")
    aposta = float(input("Informe o valor da aposta: "))
        
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    somadados = dado1 + dado2

    print(f"Dado 1: {dado1}")
    print(f"Dado 2: {dado2}")
    print(f"Soma: {somadados}")

    if somadados in (7, 11):
        print("Você ganhou!")
    elif somadados in (2, 3, 12):
        print("Você perdeu!")
    else:
        print("Jogue novamente...")
        novo = 0
        while novo != somadados and novo != 7:
            novo = random.randint(1, 6) + random.randint(1, 6)
            print(f"Novo: {novo}")
            
        if novo == somadados:
            print("Você ganhou!")
        else:
            print("Você perdeu!")
    #

