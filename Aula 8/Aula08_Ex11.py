'''Aula 08 - Exerc.11
Encontrar números primos é uma tarefa difícil.
Faça um programa que defina uma função que retorne a quantidade de números primos existentes no intervalo digitado 
(intervalo fechado, ou seja, considerando os números digitados).
'''
#Felipe Backes Kettl


def isprimo(numero):
    count = 0
    for j in range(1, numero+1):
        if numero % j == 0 :
            count +=1
    if count == 2:
        return True
    else:
        return False

def qtdprimo(min, max):
    count = 0
    for x in range (min, max+1):
        primo = isprimo(x)
        if primo == True:
            count += 1
    return count

x, y = [int(x) for x in input('Digite um intervalo fechado (dois números): ').split()]
z = 0
#Para intervalos decrescente fiz um inversos de valor x e y só pra n precisar repetir toda a estrutura do for na função
if x > y:
    z = x
    x = y
    y = z

numprimos = qtdprimo(x, y)

print(f'Há {numprimos} números primos entre o intervalo {x} e {y}')

