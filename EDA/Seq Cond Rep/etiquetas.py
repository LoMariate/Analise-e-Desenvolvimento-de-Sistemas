produto = input("Produto: ")
num = int(input("Nº de Etiquetas: "))

for i in range(1, num+1):
    if i % 2 == 1:
        print(f"{produto:30s}", end="")
    else:
        print(produto)