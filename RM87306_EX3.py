print("BEM VINDO AO JOGO")
x= 1
y= 0
a= 0
print("O jogador deverá informar um número aleatório, que vai de 0 à 11.000, caso esse número esteja dentro da sequência de Fibonacci, o jogador vence a partida")
jogo = int(input("Digite um número de 0 à 11.000: "))
for i in range (1,21):
    z = y
    y = x
    x = z + y
    print (x)
    if x == jogo:
        a = 1
if a == 1:
        print("Ação bem sucedida")
else:
        print("A ação falhou...")

