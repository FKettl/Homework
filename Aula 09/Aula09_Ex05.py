'''Aula 09 - Exerc.5
URI 2376
'''
#Felipe Backes Kettl
#Acho q talvez com o uso de dicionario desse pra por for dentro de for pra fazer o codigo bem curto, ou com uma lista [abcdefghijklmnop] e ir removendo os itens

v1 = ''
v2 = ''
v3 = ''
v4 = ''
v5 = ''
v6 = ''
v7 = ''
v8 = ''
v9 = ''
v10 = ''
v11 = ''
v12 = ''
v13 = ''
v14 = ''
vencedor = ''
for i in range(15):
    n1, n2 = [int(x) for x in input().split()]
    if i == 0:
        if n1 > n2:
            v1 = 'A'
        else:
            v1 = 'B'
    if i == 1:
        if n1 > n2:
            v2 = 'C'
        else:
            v2 = 'D'
    if i == 2:
        if n1 > n2:
            v3 = 'E'
        else:
            v3 = 'F'
    if i == 3:
        if n1 > n2:
            v4 = 'G'
        else:
            v4 = 'H'
    if i == 4:
        if n1 > n2:
            v5 = 'I'
        else:
            v5 = 'J'
    if i == 5:
        if n1 > n2:
            v6 = 'K'
        else:
            v6 = 'L'
    if i == 6:
        if n1 > n2:
            v7 = 'M'
        else:
            v7 = 'N'
    if i == 7:
        if n1 > n2:
            v8 = 'O'
        else:
            v8 = 'P'
    if i == 8:
        if n1 > n2:
            v9 = v1
        else:
            v9 = v2
    if i == 9:
        if n1 > n2:
            v10 = v3
        else:
            v10 = v4
    if i == 10:
        if n1 > n2:
            v11 = v5
        else:
            v11 = v6
    if i == 11:
        if n1 > n2:
            v12 = v7
        else:
            v12 = v8
    if i == 12:
        if n1> n2:
            v13 = v9
        else:
            v13 = v10
    if i == 13:
        if n1 > n2:
            v14 = v11
        else:
            v14 = v12
    if i == 14:
        if n1 > n2:
            vencedor = v13
        else:
            vencedor = v14
    
print(vencedor)