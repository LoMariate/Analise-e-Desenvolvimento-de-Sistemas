palavra = input("Palavra: ")

reverso = palavra[::-1]

if palavra == reverso:
    print(f"{palavra} é palíndrome")
else:
    print(f"{palavra} não é um palíndrome")