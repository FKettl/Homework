'''Aula 15 - Exerc.04
URI 1514
'''
#Felipe Backes Kettl

while True:
    participantes, questoes = [int(x) for x in input().split()]
    torneio = []
    cond1 = 1
    cond2 = 1
    cond3 = 1
    cond4 = 1
    
    if (participantes == 0) and (questoes == 0):
        break

    for x in range(participantes):
        resolvidos = []
        count = 0
        resolvidos =[int(x) for x in input().split()]
        torneio.append(resolvidos)    
        for i in range(questoes):
            count += resolvidos[i]
        if count == questoes:
            cond1 = 0
        if count == 0:
            cond4 = 0
            
    for x in range(questoes):
        count = 0
        for j in range(participantes):
            count += torneio[j][x]
        if count == 0:
            cond2 = 0
        if count == participantes:
            cond3 = 0
            
    print(cond1+cond2+cond3+cond4)