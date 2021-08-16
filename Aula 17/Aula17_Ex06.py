'''Aula 17 - Exerc.06
URI 2091
'''
#Felipe Backes Kettl

while True:
    guia={}
    n = int(input())
    if n == 0:
        break
    numeros = [int(x) for x in input().split()]
    guia = {}
    for x in numeros:
        if x in guia.keys():
            del guia[x]
        else:
            guia[x] = 1
    for key, value in guia.items():
        if value == 1:
            print(key)
            break   