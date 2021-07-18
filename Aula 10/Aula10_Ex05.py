'''Aula 10 - Exerc.05
URI 1094
'''
#Felipe Backes Kettl

testes= int(input())
total = 0
totalC = 0
totalR = 0
totalS = 0

for x in range(testes):
    qtd, tip = input().upper().split()
    qtd = int(qtd)
    total += qtd
    if 'C' in tip:
        totalC +=qtd
    elif 'R' in tip:
        totalR +=qtd
    elif 'S' in tip:
        totalS += qtd

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {totalC}')
print(f'Total de ratos: {totalR}')
print(f'Total de sapos: {totalS}')
print(f'Percentual de coelhos: {(totalC/total) * 100:.2f} %')
print(f'Percentual de ratos: {(totalR/total)*100:.2f} %')
print(f'Percentual de sapos: {(totalS/total)*100:.2f} %')