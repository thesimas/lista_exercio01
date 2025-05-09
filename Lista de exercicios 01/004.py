#4. Calcular e mostrar a área da base e o volume de um cilindro dados o Raio e a Altura.

raio = int(input("Me informe o raio de um cilindro:\n"))

altura = int(input('Me informe a a altura do cilindro:\n'))

area_base = 3.14 * raio ** 2

volume = area_base *altura

print(f'A area do cilindro é de: {area_base:.2f}\nO volume deste cilindro é de: {volume:.2f}')
