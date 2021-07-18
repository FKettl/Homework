'''Aula 09 - Exerc.06
URI 2434
'''
#Felipe Backes Kettl


n, movido = [int(x) for x in input().split()]
while True:
    if (1 <= n <= 30) and (-10**3 <= movido <= 10**3):
        break
    n, movido = [int(x) for x in input().split()]   

total = movido
menor = total
for j in range(n):
    movido = int(input())
    total += movido
    if total < menor:
        menor = total

print(menor)