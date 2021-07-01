print("Vamos calcular o seu IMC?")
print("obs: ao inserir os dados solicitados, favor utilizar ponto ao invés de vírgula")
nome=input("Digite seu nome: ")
peso = input("Digite o seu peso em quilos): ")
peso = float(peso)
altura = input("Digite sua altura em metros): ")
altura = float(altura)
imc = (peso / (altura * altura))
print("Seu IMC é: {0:.2f}"  .format(imc))
if imc < 16.00:
    print("Baixo peso Grau III")
elif imc < 16.99:
    print("Baixo peso Grau II")
elif imc < 18.49:
    print("Baixo peso Grau I")
elif imc < 24.99:
    print("Peso ideal")
elif imc < 29.99:
    print("Sobrepeso")
elif imc < 34.99:
    print("Obesidade Grau I")
elif imc < 39.99:
    print("Obesidade Grau II")
elif imc > 40:
    print("Obesidade Grau III")
