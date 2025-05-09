#2. Ler a medida do lado de um quadrado e calcular e mostrar a área e o perímetro

lado_quadrado = int(input('Me informe o lado em metros do quadrado:  '))

area = lado_quadrado ** 2
perimetro = lado_quadrado * 4 

print(f'A area do quadrado é: {area}\nO perimetro é: {perimetro}')