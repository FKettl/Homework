'''Aula 06 - Exerc. 03
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos e qual foi o maior e o menor valor lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
#Felipe Backes Kettl

count = 0
tot = 0

n0 = int(input('Digite um número: '))
maior = n0
menor = n0
tot += n0
count += 1

while True:
    a = input('Deseja digitar outro numero? [Y/N] ').upper().strip()
    if a == 'Y':
        num = int(input('Digite um número: '))
        tot += num 
        count += 1 
        if num > maior:
            maior = num
        elif num < menor:
            menor = num 
        continue
    elif a == 'N':
        print(f'A média é {tot//count} o maior é {maior} e o menor é {menor}')
        break


#dava pra fazer outro loop pra evitar qualquer resposta que n seja Y ou N, porém sem só pra deixar o codigo menor, visto que ele ja atende ao que foi pedido