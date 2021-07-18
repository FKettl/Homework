'''Aula 08 - Exerc.10
Faça um programa que leia 10 números inteiros do teclado,
seu programa deve ter uma função que verifique e retorne (a cada novo número digitado) se ele é par ou ímpar
A partir desta informação, ao final de sua execução, seu programa deve imprimir o número total de pares e ímpares que foram digitados. 

'''
#Felipe Backes Kettl


def contador(num):
    if num % 2  == 0 and  num != 0:
        return 'par'
    elif num % 2 != 0 :
        return 'impar'


par = 0
impar = 0

for x in range(10):
    n = int(input('Digite um número: '))
    tipo = contador(n)
    if tipo == 'par':
        par +=1
        print('Esse número é par.')
    elif tipo == 'impar':
        impar +=1
        print('Esse número é ímpar.')

print(f'Entre esses números há {par} pares e {impar} ímpares.')


