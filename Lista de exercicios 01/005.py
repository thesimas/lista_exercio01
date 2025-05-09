#5. Ler dois valores numéricos e na sequência calcular e mostrar:
#a) A soma destes valores
#b) O produto deles
#c) O quociente entre eles.

num1 = int(input('Me informe o primeiro número:  '))
num2 = int(input('Me informe o segundo número:  '))


if num2 == 0:
    print(f'{num1} / {num2}; Não é possivel gerar o resultado do quociente.')
    soma = num1 + num2
    produto = num1 * num2 
    print(f"A soma dos dois números informados é: {soma}")
    print(f"O produto dos dois números informados é: {produto}")

else: 
    soma = num1 + num2
    produto = num1 * num2 
    quociente = num1 * num2
    print(f"A soma dos dois números informados é: {soma}")
    print(f"O produto dos dois números informados é: {produto}")
    print(f"O quociente dos dois números informados é: {quociente:.1f}")
