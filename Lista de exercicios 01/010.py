#10. Calcular a média final dadas as notas de 3 provas e produzir uma saída com a média e a
#situação do aluno de acordo com o seguinte critério:
#a) média >= 7: aprovado;
#b) 5 <= média < 7: recuperação;
#c) média < 5: reprovado.

nota1 = float(input("Digite a primeira nota:  "))
nota2 = float(input("Digite a segunda nota:  "))
nota3 = float(input("Digite a terceira nota:  "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7 and media <= 10:
    print(f"A média final é {media:.2f}. O aluno está aprovado.")

elif media >= 5 and media < 7:
    print(f"A média final é {media:.2f}. O aluno está em recuperação.")

elif media > 0 and media < 5:
    print(f"A média final é {media:.2f}. O aluno está reprovado.")

else:
    print("Nota inválida. As notas devem estar entre 0 e 10.")