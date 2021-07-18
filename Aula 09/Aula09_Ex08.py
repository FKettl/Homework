'''Aula 09 - Exerc 08
URI 2297
'''
#Felipe Backes Kettl

count = 1

while True:
    totala = 0
    totalb = 0
    n = int(input())
    if n == 0:
        break
    for x in range(n):
        a, b = [int(x) for x in input().split()]
        while True: #Verificação de valores
            if (0 <= a <= 100) and (0 <= b <= 100):
                break
            a, b = [int(x) for x in input().split()]
        totala += a
        totalb += b
    if totala > totalb:
        vencedor = 'Aldo'
    else:
        vencedor = 'Beto'
    print(f'Teste {count}')
    print(vencedor)
    print('')
    count += 1