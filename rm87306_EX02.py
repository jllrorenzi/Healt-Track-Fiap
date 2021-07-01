print("Valor a ser cobrado pelo serviços prestados")
print("Planos:")
print("1- Basic")
print("2- Silver")
print("3- Gold")
print("4- Platinum")
plano= int(input("Digite o seu plano (utilizar um dos números acima): "))
faturamento=float(input("Digite o valor do seu faturamento R$: "))
if plano == 1:
    bonus1= (faturamento * 30) / 100
    print("O bonus a ser pago é de R$ {0:.2f}" .format(bonus1))
elif plano == 2:
        bonus2 = (faturamento * 20) / 100
        print("O bonus a ser pago é de R$ {0:.2f}".format(bonus2))
elif plano == 3:
        bonus3 = (faturamento * 10) / 100
        print("O bonus a ser pago é de R$ {0:.2f}".format(bonus3))
elif plano == 4:
        bonus4 = (faturamento * 5) / 100
        print("O bonus a ser pago é de R$ {0:.2f}".format(bonus4))
elif plano!= 1 or 2 or 3 or 4:
    print("Plano não encontrado!!!")

