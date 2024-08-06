import math

a = float(input('Digite o ângulo: '))

an = math.radians(a)

s = math.sin(an)
c = math.cos(an)
t = math.tan(an)


print(f'O seno de {a} é {s:.2f} o cosseno é {c:.2f} e a tangente é {t:.2f}')