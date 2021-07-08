'''Aula 05 - Ex03
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.
'''
#Felipe Backes Kettl

numeromaior = 0
posição = 0

for x in range(100):
    numero = int(input())
    if numero > numeromaior:
        numeromaior = numero
        posição = x + 1 
        
print(numeromaior)
print(posição)