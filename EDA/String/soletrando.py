import time
palavra = input("Palavra: ")

print("Soletrando a palavra..: ", end="")

for letra in palavra:
    print(letra.upper(), end="", flush=True)
    time.sleep(1)