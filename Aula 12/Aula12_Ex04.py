'''Escreva um programa que leia uma lista X contendo “N” elementos numéricos e leia
um valor numérico qualquer K. Após a inserção dos dados na lista, determine e
imprima a lista resultante da multiplicação de K pelos elementos de X.'''
#Felipe Backes Kettl

lista = [int(x) for x in input('Digite N valores inteiros: ').split()]
k = int(input('Digite um valor K: '))
listak = []

for x in range(len(lista)):
    listak.append(k*lista[x])
    
print(listak)