'''Aula 07 - Exerc.04
Coloque em ordem crescente três números inteiros, lidos do teclado.
'''
#Felipe Backes Kettl


a, b, c = input('digite três numeros: ').split()
a = int(a)
b = int(b)
c = int(c)


maior = a
meio = a
menor = a

for x in (a, b, c):
    if x > maior:
        maior = x
    elif x < menor:
        menor = x
    
if a > b:
    if a < c:
        meio = a 
    elif b > c:
        meio = b
    else:
        meio = c

elif a < b:
    if a > c:
        meio = a
    elif c > b:
        meio = b
    else:
        meio = c

print(f'A ordem dos numeros é {menor} {meio} {maior}.')



'''Esse código é de um colega, eu gostei muito dele e quero assimilar a lógica por tras pra em futuros codigos conseguir chegar em algo assim por conta
só deixei aqui pra caso eu volte a ler

for x in (a, b, c):
    if x > maior:
        meio = maior
        maior = x
    elif x < menor:
        meio = menor
        menor = x
    else:
        meio = x
'''
