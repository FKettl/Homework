'''Aula 17 - Exerc.05
URI 1430
'''
#Felipe Backes Kettl

guia = {'W': 1, 'H': 1/2, 'Q': 1/4, 'E': 1/8, 'S': 1/16, 'T': 1/32, 'X': 1/64}

while True:
    notas = [] 
    composiçao = input().split('/')
    acertos = 0
    if '*' in composiçao:
        break
    for x in composiçao:
        notas.append(list(x))
    for x in notas:
        count = 0
        for y in x:
            count += guia[y]
        if count == 1:
            acertos +=1
    print(acertos)