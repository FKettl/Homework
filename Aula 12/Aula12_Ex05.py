'''Aula 12 - Exerc.05
Faça um programa que leia uma lista X[0..19] e, após sua criação, troque a posição do
1º elemento pela posição do 20º elemento, o 2º com o 19º e assim por diante.'''
#Felipe Backes Kettl

lista = [int(x) for x in input('Digite 20 números inteiros: ').split()]
a = 0
for x in range(10):
    a = lista[x]
    lista[x] = lista[-x-1]
    lista[-x-1] = a
print(lista)

