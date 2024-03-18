num = int(input("Nº de chinchilas: "))
anos = int(input("Nº Anos da Criação: "))

total = num

if num < 2:
    print("Deve inicar com, no mínimo, 2 chinchilas")
else:
    for i in range(1, anos+1):
        print(f"{i}º ano: {total}")
        total = total * 3