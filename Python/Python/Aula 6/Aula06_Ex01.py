''' Aula06 - Exerc. 01
Escreva um programa que leia o sexo das pessoas, mas somente aceite “M” ou “F”.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
#Felipe Backes Kettl

while True:
    sex = input('Qual o seu sexo? [M/F] ').upper()
    if sex == 'M' or sex == 'F':
        print('fim')
        break
    else: 
        print('Digite novamente ')