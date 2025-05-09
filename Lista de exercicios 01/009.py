#9. Ler 2 números (A e B), verificar e imprimir qual deles é o maior ou a mensagem “A=B” (A e B são iguais).

num1 = int(input("Digite o primeiro número:  "))
num2 = int(input("Digite o segundo número:  "))

if num1 > num2:
    print(f"O maior número é: {num1}")

elif num2 > num1:
    print(f"O maior número é: {num2}")

else:
    print("Os dois números informados são iguais.")
