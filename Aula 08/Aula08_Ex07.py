'''Aula 08 - Exerc.07
função do URI 2378 sem o uso do return
'''
#Felipe Backes Kettl



def excedencia(n, c):
    total = 0
    excedeu = False
    
    for i in range(1, n+1):
        s, e = [int(x) for x in input(f'Digite quantas pessoas sairam e quantas entraram na {i}ª parada: ').split()]
        total -= s
        total += e
        if total > c:
            excedeu = True
        
    if excedeu == True:
        print('S')
    else:
        print('N')

n, c = [int(x) for x in input('Digite o total de paradas do elevador e sua capacidade total: ').split()]
excedencia(n , c)