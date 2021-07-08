'''Aula 05 - Ex 04
Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N, se for o caso.
'''
#Felipe Backes Kettl

 
n = int(input())

for x in range(2, n+2, 2):
    a = x**2
    print (f'{x}^2 = {a}')
 
   