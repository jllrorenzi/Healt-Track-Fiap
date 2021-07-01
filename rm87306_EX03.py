print("Votação para escolha do dia de realização das lives")
nome=input("Digite o seu nome: ")
dia=str(input("Digite o dia desejado (inserir apenas as três primeiras letras do dia. Ex. QUI =Quinta-feira): "))
if dia.upper() == "SEG":
    print("Um voto para Segunda-Feira")
    print("{} votou na Segunda-Feira" .format(nome))
elif dia.upper() == "TER":
    print("Um voto para Terça-Feira")
    print("{} votou na Terça-Feira" .format(nome))
elif dia.upper() == "QUA":
    print("Um voto para Quarta-Feira")
    print("{} votou na Quarta-Feira" .format(nome))
elif dia.upper() == "QUI":
    print("Um voto para Quinta-Feira")
    print("{} votou na Quint-Feira".format(nome))
elif dia.upper() == "SEX":
    print("Um voto para Sexta-Feira")
    print("{} votou na Sexta-Feira" .format(nome))
elif dia.upper() != "SEG" or "TER" or "QUA" or "QUI" or"SEX":
    print("Seu voto não pôde ser computado")
    print("{} deverá se atentar ao dia escolhido. Vote novamente" .format(nome))