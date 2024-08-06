qd = int(input('Quantos dias o carro foi alugado: '))
km = float(input('Quantos Km o carro rodou: '))

d = qd * 60
kmt = km * 0.15
t = d + kmt

print(f'As diárias foram de {qd} dias e o valor foi de {d}')
print(f'Os km rodados foram de {km} Km e o valor total foi de R$ {kmt}')
print(f'O total é R$ {t:.2f}');