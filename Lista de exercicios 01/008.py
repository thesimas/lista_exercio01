#8. Ler 3 números e verificar se o primeiro é maior que a soma dos outros dois. Apresentar a
#mensagem “O primeiro número é maior que a soma dos outros dois” ou “O primeiro número
#NÃO é maior que a soma dos outros dois”.

num1 = int(input('Me informe o primeiro número:  '))
num2 = int(input('Me informe o segundo número:  '))
num3 = int(input('Me informe o terceiro número:  '))

soma_ultimos_num = num2 + num3

if soma_ultimos_num < num1:
    print(f'O primeiro número ({num1}) é maior que a soma dos dois ultimos números informados! ({soma_ultimos_num})')

elif soma_ultimos_num > num1: 
    print(f'O primeiro número ({num1}) NÃO é maior que a soma dos dois ultimos números informados! ({soma_ultimos_num})')

else:
    print(f'O primeiro número ({num1}) é igual a soma dos ultimos números informados! ({soma_ultimos_num})')
