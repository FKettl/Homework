'''Aula 17 - Exerc.03
1911
'''
#Felipe Backes Kettl


while True: 
    qtdalunos = int(input())
    if qtdalunos == 0:
        break
        
    verdadeira = {}
    duvidosa = {}
    count = 0
    
    for x in range(qtdalunos):
        nome, assinatura = [x for x in input().split()]
        verdadeira[nome] = assinatura
        
    qtdpresentes = int(input())
    for x in range(qtdpresentes):
        nome, assinatura = [x for x in input().split()]
        duvidosa[nome] = assinatura
            
    for x in duvidosa:
        comparar = list(duvidosa[x])
        comparar2 = list(verdadeira[x])
        diferenças = 0
        for x in range(len(x)):
            if comparar[x] != comparar2[x]:
                diferenças += 1
        if diferenças > 1:
            count += 1

    print(count)