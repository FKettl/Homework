'''Exerc.04- Aula 04
 Escreva um programa que, para um determinado valor, informe se este é positivo, negativo ou zero.
 E verifique também se este número é par.
 '''
#Felipe Backes Kettl

valor = int(input('Informe um valor: '))

if valor > 0:
    print(f'O numero {valor} é Positivo.')
elif valor < 0:
    print(f'O numero {valor} é negativo')
else:
    print(f'O valor é zero')
    
if (valor % 2) == 0:
    print('E é par.')
else:
    print('E é ímpar.')