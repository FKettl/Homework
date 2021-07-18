'''Aula 10 - Exerc.06
No mundo da matemática, para sabermos se um grande número é divisível por outro existe uma regra, chamada de regra de divisibilidade.
Um número natural é divisível por 3 quando a soma de todos os seus algarismos forma um número divisível por 3, ou seja, um múltiplo de 3.
Ex1: 1.104 é divisível por 3?
Resposta: SIM. É divisível por 3, pois seus algarismos quando somados: 1 + 1 + 0 + 4 = 6, que é um número divisível por 3 (porque 6 ÷ 3 = 2,
que é um número natural).
Ex2: 2.791.035 é divisível por 3?
Resposta: SIM. 2.791.035 é constituído de algarismos que somados: 2 + 7 + 9 + 1 + 0 + 3 + 5 = 27,
gera um número divisível por 3 (pois 27 ÷ 3 = 9, número natural).
Faça um programa que dado um número, ele verifique se este número é divisível por 3.

Entrada
O arquivo de entrada conterá dois números, n (1< n <10) indicando o número de algarismos de m, (1< m < 1000000000). Sendo m e n números inteiros.
Utilizar o laço while para controlar a entrada de dados (perguntar se o usuário deseja continuar verificando).

Saída
Seu programa deve fornecer o número da soma dos algarismos de m e logo depois apresentar “sim” caso o número seja divisível por 3 ou “não” caso não seja. 
Exemplo:
Entrada 
3 111
1 1
2 24

Saída
3 sim
1 nao
6 sim

'''
#Felipe Backes Kettl

while True:
    total = 0
    n, m = input().split()
    n = int(n)
    for j in range(n):
        num = int(m[j])
        total += num
    if total% 3 == 0:
        print(f'{total} sim')
    else:
        print(f'{total} nao')
    continuar = input('Deseja continuar? [S/N] ').upper()
    if continuar == 'N':
        print('Fim.')
        break
