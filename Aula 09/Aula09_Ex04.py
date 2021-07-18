'''Aula 09 - Exerc.04
URI 2927
'''
#Felipe Backes Kettl

a, c, x, y = [int(x) for x in input().split()]

while True:
    if (0 < c <= 1000) and (a <= c) and (a <= 1000) and (x <= c) and (x <= 100) and (y <= c) and (y <= 1000):
        break
    else:
        a, c, x, y = [int(x) for x in input().split()]

compdispo = c - x - y - 1
if a > compdispo:
    if x > (y/2):
        print('Caio, a culpa eh sua!')
    else:
        print('Igor bolado!')
else:
    print('Igor feliz!')
