n = int(input())
parimpar = 0
negaposi = 0
for x in range(n):
    valor = int(input())
    if valor % 2 == 0 and valor != 0:
        parimpar = 'EVEN'
    elif valor % 2 != 0:
        parimpar = 'ODD'
    if valor > 0:
        negaposi = 'POSITIVE'
    elif valor < 0:
        negaposi = 'NEGATIVE'
    if valor == 0:
        print('NULL')
    if valor != 0:
        print(f'{parimpar} {negaposi}')