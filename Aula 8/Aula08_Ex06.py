'''Aula 08 - Exerc.06
função URI 1115 sem o uso do return
'''
#Felipe Backes Kettl

def quadrante():
    while True: 
        x, y = [int(x) for x in input().split()]
        if  x == 0 or y == 0:
            break
        if x > 0 and y > 0:
            quadrante = 'primeiro'
        elif x < 0 and y > 0:
            quadrante = 'segundo'
        elif x < 0 and y < 0:
            quadrante = 'terceiro'
        elif x > 0 and y < 0:
            quadrante = 'quarto'
        print(quadrante)

quadrante()