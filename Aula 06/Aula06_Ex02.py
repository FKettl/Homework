'''Aula 06 - Exerc.02
Implemente um jogo onde o usuário deve adivinhar o número escolhido pelo computador (entre 0 e 10).
O Usuário irá digitando valores até descobrir este valor.
 Quando o usuário “acertar”, uma mensagem avisa o final do jogo (que o número correto foi digitado) e o número de tentativas.
'''
#Felipe Backes Kettl

from random import randint

tentativas = 1
n = randint(0 ,10)

while True:
    r = int(input('Adivinhe um número de 0 a 10: '))
    if r == n:
        print(f'Fim de jogo, você acertou o número {n} depois de {tentativas} tentativa(s)')
        break
    tentativas += 1