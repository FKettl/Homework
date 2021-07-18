'''Aula 10 - Exerc.04
URI 1168
'''
#Felipe Backes Kettl

n = int(input())
for x in range(n):
    total = 0
    numero = input()
    doisleds = numero.count('1')
    tresleds = numero.count('7')
    quatroleds = numero.count('4')
    cincoleds = numero.count('3') + numero.count('2') + numero.count('5')
    seisleds = numero.count('6') + numero.count('9') + numero.count('0')
    seteleds = numero.count('8')
    total = doisleds*2 + tresleds*3 + quatroleds*4 + cincoleds*5 + seisleds*6 + seteleds*7
    print(f'{total} leds')

    