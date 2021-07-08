'''Aula 07 - Exerc 06
URI 2295 - Frota de Táxi
'''
#Felipe Backes Kettl

while True:
    plal, plga, ral, rga = [float(x) for x in input().split()]
    kmal = ral/plal
    kmga = rga/plga
    if (10.00 >= plga, plal >= 0.01) and (20.00 >= rga ,ral >= 0.01):
        if kmal > kmga:
            print('A')
            break
        else:
            print('G')
            break
    else:
        continue