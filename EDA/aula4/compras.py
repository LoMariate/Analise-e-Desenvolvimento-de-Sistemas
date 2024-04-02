compras = []
precos = []

def titulo(texto, sublinhado="="):
    print(texto)
    print(sublinhado*40)

def incluir():
    titulo("Inclusão de compar", "-")
    compra = input("Descrição da Compra: ")
    preco = float(input("Valor previsto R$..: "))
    
    compras.append(compra)
    precos.append(preco)
    print("Ok. Compra Cadastrada com Sucesso!")


def listar():
    titulo("Listar Cadastradas", "-")
    
    total = sum(precos)
    print("Descriçao da compra..........: R$ Previsto: ")
    print("--------------------------------------------")
    
    
    for compra, preco in zip(compras, precos):
        print(f"{compra:30s} R$ {preco:12.2f}")
    print(f"Total de Compras: R$ {total:12.2f}")
    print("--------------------------------------------")


def listar_ordem():
    titulo("Listar Cadastradas em Ordem", "-")
    total = sum(precos)

    print("Descriçao da compra..........: R$ Previsto: ")
    print("--------------------------------------------")
    
    
    for compra, preco in sorted(zip(compras, precos)):
        print(f"{compra:30s} R$ {preco:12.2f}")
    print(f"Total de Compras: R$ {total:12.2f}")
    print("--------------------------------------------")

def excluir():
    titulo("Exclusão de Compra", "-")
    listar()
    pos = int(input("Informe o número da compra a ser excluída: "))
    
    if pos >= 0 and pos < len(compras):
        compras.pop(pos)
        precos.pop(pos)
        print("Compra excluída com sucesso!")
    else:
        print("Posição Inválida. Tente Novamente!")

    input("Pressione ENTER para continuar...")

def grava_compras():
    with open("compras.txt", "w") as arq:
        for compra, preco in zip(compras, precos):
            arq.write(f"{compra};{preco}\n")

def carrega_compras():
    try:
        with open("compras.txt") as arq:
            for linha in arq:
                compra, preco = linha.strip().split(";")
                compras.append(compra)
                precos.append(float(preco))
    except FileNotFoundError:
        pass

carrega_compras()

while True:
    titulo("Lista de Compras da Semana")
    print("1. Iniciar Compra")
    print("2. Listar Compras")
    print("3. Listar Compras em Ordem")
    print("4. Excluir Compra")
    print("5. Finalizar")
    
    opcao = int(input("Opção: "))

    if opcao == 1:
        incluir()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        listar_ordem()
    elif opcao == 4:
        excluir()
    elif opcao == 5:
        grava_compras()
        break
    else:
        print("Opção Inválida. Tente Novamente!")
        input("Pressione ENTER para continuar...")


