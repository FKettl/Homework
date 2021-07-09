'''Aula 08 - Exerc.02 
fazer função pro URI 2057 sem o uso do return
'''
#Felipe Backes Kettl

def calcchegada(s, t ,f):
    chegada = s+t+f
    if chegada >= 24:
        chegada -= 24
    elif chegada < 0:
        chegada += 24
    print(chegada)

s, t, f = [int(x) for x in input().split()]
calcchegada(s, t, f)