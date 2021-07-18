'''Aula 05 - Ex 01
Leia 5 valores Inteiros.
A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares,
 quantos valores digitados foram positivos e quantos valores digitados foram negativos.
'''
#Felipe Backes Kettl

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

par = 0
impar = 0
positivo = 0
negativo = 0
for x in [a , b ,c ,d ,e]:
    if x % 2 == 0:
        par = par+1
    elif x % 2 !=0:
        impar = impar+1
    if x > 0:
        positivo = positivo+1
    elif x < 0: 
        negativo = negativo+1
        
print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')
