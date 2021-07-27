'''Elabore um programa que contenha uma tupla contendo 10 números inteiros. Mostre
as posições em que o maior e o menor elemento ocupam na tupla.'''
#Felipe Backes Kettl


lista = [int(x) for x in input('Digite 10 números inteiros: ').split()]
tupla = tuple(lista)

maior = tupla[0]
menor = tupla[0]
indexmaior = 0
indexmenor = 0

for x in range(len(tupla)):
    if tupla[x] > maior:
        maior = tupla[x]
        indexmaior = x
    if tupla[x] < menor:
        menor = tupla[x]
        indexmenor = x

print(f'A o maior numero está na posição {indexmaior} e o menor na posição {indexmenor}.')