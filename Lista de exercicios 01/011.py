#11. Ler a velocidade com que o motorista está dirigindo e calcular a multa que será emitida,
#caso haja a multa. Sabe-se que a velocidade permitida é de 80 km/h e que o custo da multa é de:
#a) R$50, se a velocidade ultrapassar em até 10 km/h a velocidade permitida;
#b) R$100, se a velocidade estiver acima de 10 até 30 km/h da velocidade permitida.
#c) R$200, se estiver acima de 30 km/h da velocidade permitida.

velocidade = int(input("Me informe a velocidade do motorista:  "))

if velocidade <= 80:
    print("O motorista não foi multado.")

elif velocidade > 80 and velocidade <= 90:
    print("O motorista foi multado em R$50,00.")

elif velocidade > 90 and velocidade <= 110:
    print("O motorista foi multado em R$100,00.")

else:
    print("O motorista foi multado em R$200,00.")