'''Aula 05 - ex 05
Leia um valor inteiro N. 
Este valor será a quantidade de valores que serão lidos em seguida. 
Para cada valor lido, mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN), ímpar (ODD), positivo (POSITIVE) ou negativo (NEGATIVE).
No caso do valor ser igual a zero (0), embora a descrição correta seja (EVEN NULL), pois por definição zero é par, seu programa deverá imprimir apenas NULL.
'''
#Felipe Backes Kettl

n = int(input())
parimpar = 0
negaposi = 0
for x in range(n):
    valor = int(input())
    if valor % 2 == 0 and valor != 0:
        parimpar = 'EVEN'
    elif valor % 2 != 0:
        parimpar = 'ODD'
    if valor > 0:
        negaposi = 'POSITIVE'
    elif valor < 0:
        negaposi = 'NEGATIVE'
    if valor == 0:
        print('NULL')
    if valor != 0:
        print(f'{parimpar} {negaposi}')
