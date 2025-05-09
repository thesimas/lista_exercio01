#12. Faça o mesmo exercício acima, só que agora, a velocidade máxima permitida será lida. 

velocidade = int(input("Me informe a velocidade do motorista:  "))
velocidade_maxima = int(input("Me informe a velocidade máxima permitida:  "))

diferenca = velocidade - velocidade_maxima

if diferenca <= 0:
    print("O motorista não foi multado.")

elif diferenca > 0 and diferenca <= 10:
    print("O motorista foi multado em R$50,00.")

elif diferenca > 10 and diferenca <= 30:
    print("O motorista foi multado em R$100,00.")

else:
    print("O motorista foi multado em R$200,00.")