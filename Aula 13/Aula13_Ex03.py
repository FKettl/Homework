'''Aula 13 - Exerc. 03
URI 1547
'''
#Felipe Backes Kettl

 
#n = int(input())

#for x in range(n):


n = int(input())
    
for x in range(n):
    qtdalunos, numero = [int(x) for x in input().split()]
    codigos = [int(x) for x in input().split()]
    proximidade = [abs(numero-codigos[i]) for i in range(qtdalunos)]
    menor = -1
    posiMenor = 0
    for x in proximidade:
        if x == 0:
            print(proximidade.index(x)+1) 
            posiMenor = 0
            break
        if (x < menor) or menor == -1:
            menor = x
            posiMenor = proximidade.index(x)+1
    if posiMenor == 0:
        continue
    for x in proximidade:
        if x == menor:
            print(proximidade.index(x)+1)
            break

        