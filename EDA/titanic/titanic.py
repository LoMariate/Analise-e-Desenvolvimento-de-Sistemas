import csv
import os
titanic_data = []

os.system("cls")
with open("./EDA/titanic/train.csv", mode="r") as arq:
    dados_csv = csv.DictReader(arq)
    for linha in dados_csv:
        titanic_data.append(linha)

def titulo(texto):
    print("-" * 50)
    print(texto)
    print("-" * 50)

def dados_sexo():
    os.system("cls")
    titulo("1 - Dados por sexo")
    
    masc = 0
    fem = 0
    
    for pessoa in titanic_data:
        if pessoa["Sex"] == "male":
            masc += 1
        else:
            fem += 1
    
    masc_sobre = len([pessoa for pessoa in titanic_data
                     if pessoa["Sex"] == "male" and pessoa["Survived"] == "1"])
    
    masc_mortos = len([pessoa for pessoa in titanic_data
                     if pessoa["Sex"] == "male" and pessoa["Survived"] == "0"])
    Fem_sobre = len([pessoa for pessoa in titanic_data
                     if pessoa["Sex"] == "female" and pessoa["Survived"] == "1"])
    Fem_mortos = len([pessoa for pessoa in titanic_data
                     if pessoa["Sex"] == "female" and pessoa["Survived"] == "0"])
    
    print(f"Total de passageiros: {len(titanic_data)}")
    print(f"Total de homens: {masc}")
    print(f"Total de homens sobreviventes: {masc_sobre}")
    print(f"Total de homens mortos: {masc_mortos}")
    print(f"Total de mulheres: {fem}")
    print(f"Total de mulheres sobreviventes: {Fem_sobre}")
    print(f"Total de mulheres mortas: {Fem_mortos}")
    
    
    
def top_10_idosos():
    os.system("cls")
    titulo("2 - Top 10 mais idosos")
    
    titanic_data.sort(key=lambda x: float(x["Age"]) if x["Age"] != "" else 0, reverse=True)
    
    for i in range(10):
        print(f"{i+1} - {titanic_data[i]['Name']} - {titanic_data[i]['Age']} anos")
        
def idade_media():
    os.system("cls")
    titulo("3 - Idade média (por sexo)")


    masc_idades = ([pessoa["Age"] for pessoa in titanic_data
                    if pessoa["Sex"] == "male" and pessoa["Age"] != ""])
    fem_idades = ([pessoa["Age"] for pessoa in titanic_data
                   if pessoa["Sex"] == "female" and pessoa["Age"] != ""])
    
    masc_media = sum([float(idade) for idade in masc_idades]) / len(masc_idades)
    fem_media = sum([float(idade) for idade in fem_idades]) / len(fem_idades)
    
    print(f"Idade média dos homens: {masc_media:.2f}")
    print(f"Idade média das mulheres: {fem_media:.2f}")
    
def total_arrecadado():
    os.system("cls")
    titulo("4 - Total Arrecadado")
    
    total = sum([float(pessoa["Fare"]) for pessoa in titanic_data])
    
    print(f"Total arrecadado: ${total:.2f}")
    
def dados_por_classe():
    os.system("cls")
    titulo("5 - Dados por classe")
    
    classe1 = len([pessoa for pessoa in titanic_data if pessoa["Pclass"] == "1"])
    classe2 = len([pessoa for pessoa in titanic_data if pessoa["Pclass"] == "2"])
    classe3 = len([pessoa for pessoa in titanic_data if pessoa["Pclass"] == "3"])
    
    print(f"Total de passageiros na 1ª classe: {classe1}")
    print(f"Total de passageiros na 2ª classe: {classe2}")
    print(f"Total de passageiros na 3ª classe: {classe3}")
                   


while True:
    titulo("Análise de Dados do Titanic")
    print("1 - Dados por sexo")
    print("2 - Top 10 mais idosos")
    print("3 - Idade média (por sexo)")
    print("4 - Total Arrecadado")
    print("5 - Dados por classe")
    print("6 - Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        dados_sexo()
    elif opcao == "2":
        top_10_idosos()
    elif opcao == "3":
        idade_media()
    elif opcao == "4":
        total_arrecadado()
    elif opcao == "5":
        dados_por_classe()
    elif opcao == "6":
        break
        