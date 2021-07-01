print("VAMOS CONTROLAR OS NOSSOS GASTOS?")
diario=int(input("Quantos gastos foram realizados durante o dia? "))
gast_total = 0
for x in range(diario):
    gast_1= float(input("Inserir o valor do gasto R$: "))
    gast_total = gast_total + gast_1
print("O valor total gasto durante o dia é de R$ {0:.2f}" .format(gast_total))
media=gast_total / diario
print("A média de gastos é de R$ {0:.2f}" .format(media))