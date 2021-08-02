'''Aula 15 - Exerc.01
URI 1181
'''
#Felipe Backes Kettl

linha = int(input())
metodo = input()

soma = 0
matriz = []
for linhas in range(12):
    linhas = []
    for coluna in range(12):
        linhas.append(float(input()))
    matriz.append(linhas)

for x in range(12):
    soma += matriz[linha][x]
if metodo == 'S':
    print(f'{soma:.1f}')
elif metodo =='M':
    print(f'{soma/12:.1f}')