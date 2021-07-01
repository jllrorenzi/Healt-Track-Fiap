print("Vamos Calcular as calorias diárias")
caloria_total_cafe = 0
caloria_total_alm = 0
caloria_total_lan = 0
caloria_total_jant = 0
café= str(input("Desejar incluir as refeições do café da manhã (S/N): "))
if café.upper() != "N" and café.upper() != "S":
    while café.upper()!= "N" and café.upper() != "S":
        print("Ação não identificada. Tente novamente")
        café= str(input("Desejar incluir as refeições do café da manhã (S/N): "))
if café.upper() == "S":
    continuar_cafe = "S"
    while continuar_cafe.upper() != "N":
        alimento = str(input("Digite o alimento ingerido: "))
        caloria_cafe = int(input("Insira o total de calorias do alimento: "))
        caloria_total_cafe= int(caloria_total_cafe) + caloria_cafe
        print(caloria_total_cafe)
        continuar_cafe = str(input("Desejar continuar inserindo alimentos (S/N): "))
        if continuar_cafe.upper() != "S" and continuar_cafe.upper() != "N":
            print("Ação não identificada. Tente novamente")
            continuar_cafe = str(input("Desejar continuar inserindo alimentos (S/N): "))
            while continuar_cafe.upper() != "S" and continuar_cafe.upper() != "N":
                print("Ação não identificada. Tente novamente")
                continuar_cafe = str(input("Desejar continuar inserindo alimentos (S/N): "))
almoço= str(input("Desejar incluir as refeições do almoço (S/N): "))
if almoço.upper() != "N" and almoço.upper() != "S":
    while almoço.upper()!= "N" and almoço.upper() != "S":
        print("Ação não identificada. Tente novamente")
        almoço= str(input("Desejar incluir as refeições do almoço (S/N): "))
if almoço.upper() == "S":
    continuar_alm = "S"
    while continuar_alm.upper() != "N":
        alimento = str(input("Digite o alimento ingerido: "))
        caloria_alm = int(input("Insira o total de calorias do alimento: "))
        caloria_total_alm= int(caloria_total_alm) + caloria_alm
        print(caloria_total_alm)
        continuar_alm = str(input("Desejar continuar inserindo alimentos (S/N): "))
        if continuar_alm.upper() != "S" and continuar_alm.upper() != "N":
            print("Ação não identificada. Tente novamente")
            continuar_alm = str(input("Desejar continuar inserindo alimentos (S/N): "))
            while continuar_alm.upper() != "S" and continuar_alm.upper() != "N":
                print("Ação não identificada. Tente novamente")
                continuar_alm = str(input("Desejar continuar inserindo alimentos (S/N): "))
lanche= str(input("Desejar incluir as refeições dos lanches da manhã/tarde/noite (S/N): "))
if lanche.upper() != "N" and lanche.upper() != "S":
    while lanche.upper()!= "N" and lanche.upper() != "S":
        print("Ação não identificada. Tente novamente")
        lanche= str(input("Desejar incluir as refeições dos lanches da manhã/tarde/noite (S/N): "))
if lanche.upper() == "S":
    continuar_lan = "S"
    while continuar_lan.upper() != "N":
        alimento = str(input("Digite o alimento ingerido: "))
        caloria_lan = int(input("Insira o total de calorias do alimento: "))
        caloria_total_lan= int(caloria_total_lan) + caloria_lan
        print(caloria_total_lan)
        continuar_lan = str(input("Desejar continuar inserindo alimentos (S/N): "))
        if continuar_lan.upper() != "S" and continuar_lan.upper() != "N":
            print("Ação não identificada. Tente novamente")
            continuar_lan = str(input("Desejar continuar inserindo alimentos (S/N): "))
            while continuar_lan.upper() != "S" and continuar_lan.upper() != "N":
                print("Ação não identificada. Tente novamente")
                continuar_lan = str(input("Desejar continuar inserindo alimentos (S/N): "))
jantar= str(input("Desejar incluir as refeições do jantar (S/N): "))
if jantar.upper() != "N" and jantar.upper() != "S":
    while jantar.upper()!= "N" and jantar.upper() != "S":
        print("Ação não identificada. Tente novamente")
        jantar= str(input("Desejar incluir as refeições do jantar (S/N): "))
if jantar.upper() == "S":
    continuar_jant = "S"
    while continuar_jant.upper() != "N":
        alimento = str(input("Digite o alimento ingerido: "))
        caloria_jant = int(input("Insira o total de calorias do alimento: "))
        caloria_total_jant= int(caloria_total_jant) + caloria_jant
        print(caloria_total_jant)
        continuar_jant = str(input("Desejar continuar inserido alimentos (S/N): "))
        if continuar_jant.upper() != "S" and continuar_jant.upper() != "N":
            print("Ação não identificada. Tente novamente")
            continuar_jant = str(input("Desejar continuar inserindo alimentos (S/N): "))
            while continuar_jant.upper() != "S" and continuar_jant.upper() != "N":
                print("Ação não identificada. Tente novamente")
                continuar_jant = str(input("Desejar continuar inserindo alimentos (S/N): "))
caloria_total= int(caloria_total_cafe + caloria_total_alm + caloria_total_lan + caloria_total_jant)
print("O total de calorias ingeridas durante o café da manhã é {} cal" .format(caloria_total_cafe))
print("O total de calorias ingeridas durante o almoço é {} cal" .format(caloria_total_alm))
print("O total de calorias ingeridas durante o lanhe da manhã/tarde/noite é {} cal" .format(caloria_total_lan))
print("O total de calorias ingeridas durante o jantar é {} cal" .format(caloria_total_jant))
print("O total de calorias ingeridas durante o dia é de {} cal" .format(caloria_total))


