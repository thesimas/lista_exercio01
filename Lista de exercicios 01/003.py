#3. Ler o raio de uma circunferência e calcule e apresente sua a área e perímetro.

raio = float(input("Me informe o raio de um circunferência em centímetros?\n"))

area = 3.14159 * raio **2 
perimetro = ((2 * 3.14159) * raio) #"3.14159" é o valor de Pi

print(f'A área da circunferência é de: {area:.2f}cm²\nO perímetro da circunferência é de: {perimetro:.2f}cm')

