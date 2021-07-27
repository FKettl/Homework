'''Aula 12 - Exerc.02
Faça um programa que leia uma série de números inteiros e os armazene em uma lista.
Em seguida, o programa deve determinar se nessa série de valores aparece algum valor
repetido.
Mostrar mensagem dizendo se existe ou não um número repetido!
'''
#Felipe Backes Kettl

n = [int(x) for x in input('Digite varios números inteiros: ').split()]
n.sort()
repetido = False
for x in range(len(n)):
    if n[x] == n[x-1]:
        repetido = True

if repetido == True:
    print('Há números repetidos.')
else:
    print('Não há numeros repetidos.')