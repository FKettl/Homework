'''Aula 05 - Ex 06
Leia um valor inteiro X (1 <= X <= 1000).
Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.
'''
#Felipe Backes Kettl

x = int(input())

for i in range(1, x+1, 2):
    print (i)
