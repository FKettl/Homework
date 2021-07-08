'''Aula 07 - Exerc.01
Faça o implementação do jogo pedra-papel-tesoura.
O jogo deve imprimir vitória, empate ou derrota conforme a opção que os jogadores escolherem. 
Obs.: pedra ganha de tesoura, que ganha de papel, que ganha de pedra. 
Perguntar ao usuário se ele deseja continuar jogando.
'''
#Felipe Backes Kettl

from random import choice

while True:
    #Pega a input do usuario e decide uma randomica pro computador.
    usuario = input('Escolha pedra, papel ou tesoura: ').upper().strip()
    jogo = choice(['Pedra', 'Papel', 'Tesoura'])

    #Decide o resultado do jogo com base nas var acima.
    if (usuario == 'PEDRA' and jogo == 'Pedra') or (usuario == 'PAPEL' and jogo == 'Papel') or (usuario == 'TESOURA' and jogo == 'Tesoura'):
        print('Empate.')
    elif (usuario == 'PEDRA' and jogo == 'Papel') or (usuario == 'PAPEL' and jogo == 'Tesoura') or (usuario == 'TESOURA' and jogo == 'Pedra'):
        print('Você perdeu.')
    elif (usuario == 'PEDRA' and jogo =='Tesoura') or (usuario == 'PAPEL' and jogo == 'Pedra') or (usuario == 'TESOURA' and jogo == 'Papel'):
        print('Você ganhou')
    
    #Deixa o usuário escolher se quer continuar ou terminar.
    continuar = input('Deseja jogar novamente? [S/N] ').upper().strip()
    if continuar == 'S':
        continue
    elif continuar == 'N':
        print('Fim.')
        break
