'''Aula 13 - Exerc. 04
URI 1961
'''
#Felipe Backes Kettl
 
pulo, qtd = [int(x) for x in input().split()]
canos = [int(x) for x in input().split()]
resultado = 'YOU WIN'
for x in range(1, qtd):
    if abs((canos[x] - canos[x-1])) > pulo:
        resultado = 'GAME OVER'
        break
print(resultado)