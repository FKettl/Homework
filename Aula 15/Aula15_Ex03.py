'''Aula 15 - Exerc.03
URI 1796
'''
#Felipe Backes Kettl

 
n = int(input())
pesquisa = [int(x) for x in input().split()]
total = 0

for i in range(n):
    total += pesquisa[i]

if total >= (n/2):
    print('N')
else: 
    print('Y')