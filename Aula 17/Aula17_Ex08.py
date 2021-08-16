'''Aula 17 - Exerc.08
URI 1261
'''
#Felipe Backes Kettl

palavras, encontrar = [int(x) for x in input().split()]
dicio = {}
for x in range(palavras):
    cargo, valor = input().split()
    dicio[cargo] = int(valor)
count = 0
total = 0
while count != encontrar:
    frase = list(input().split())
    if '.' in frase:
        print(total)
        count += 1
        total = 0
        continue 
    for palavra in frase:
        if palavra in dicio.keys():
            total += dicio[palavra]

