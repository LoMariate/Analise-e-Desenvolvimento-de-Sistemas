palavra = input("Informe a palavra: ")

inicial = palavra[0]

verificado = " "

for letra in palavra:
    if letra == inicial:
        verificado += letra + " "
    else:
        verificado += "_" + " "

print(verificado)