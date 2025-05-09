#6. Calcular e mostrar a gasto em dinheiro por um fumante. Os dados de entrada são: o
#número de anos que ele fuma, o número de cigarros fumados por dia e o preço de uma
#carteira (uma carteira possui 20 cigarros).

anos_fumado = int(input('Me informe a quantidade de anos que você fuma:\n'))
numb_cigarros_dia = int(input('Me informe o número de cigarros que você fuma no dia:\n'))
preco_carteira = float(input('Me informe o valor pago em uma carteira de cigarro:\n'))

carteira = 20 

cigarros_fumado = (numb_cigarros_dia * 365) * anos_fumado
carteira_compradas = cigarros_fumado // carteira

dinheiro_gasto = preco_carteira * carteira_compradas

print(f'Nesses {anos_fumado} anos fumados, você fumou {cigarros_fumado:.0f} cigarros, comprou {carteira_compradas} carteiras de cigarro e gastou R${dinheiro_gasto:.2f} reais!')
