#7. Calcular qual será o preço de um carro ao consumidor, o valor para imposto e o valor do
#lucro para o distribuidor. Para isso, deverá ser lido qual é o custo de fábrica do carro. O
#imposto é 45% sobre o custo do carro e o lucro para o distribuidor é 12% sobre o custo do carro.

custo_fabricar_carro = float(input('Qaunto custa para fábricar um carro?\n'))

imposto = (custo_fabricar_carro * 45) / 100
lucro_distribuidor = (custo_fabricar_carro * 12) / 100

valor_final_cliente = custo_fabricar_carro + imposto + lucro_distribuidor

print(f'O preço de um carro para o consumidor final é de: R$ {valor_final_cliente:.2f} reias!')
print(f'O valor do imposto sobre o custo de fabricar um carro é de: R$ {imposto:.2f} reias!')
print(f'O lucro do distribuidor sobre um carro fabricado é de: R$ {lucro_distribuidor:.2f} reias!')

