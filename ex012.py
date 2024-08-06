import math

x = float(input('Digite o comprimento do cateto oposto: '))
y = float(input('Digite o comprimento do cateto adjacente: '))

h = math.hypot(x, y)

print(f'A hipotenusa é: {h:.2f}')