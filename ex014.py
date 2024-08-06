import random

n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluno: '))

lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
escolhidos = random.sample(lista, k=len(lista))

print(f'O aluno escolhido foi {escolhido}')
print(f'A ordem nova é {escolhidos}')