'''Aula 19 - Exerc.01

'''
#Felipe Backes Kettl

from pessoa import Pessoa
from time import sleep
p1 = Pessoa('Felipe', 22)

p1.comer('banana')
sleep(1)
p1.comer('abacaxi')
sleep(1)
p1.parar_comer()
sleep(1)
p1.falar('POO')
sleep(1)
p1.comer('chocolate')
sleep(1)
p1.falar('Xadrez')
sleep(1)
p1.parar_falar()
sleep(3)
p1.imprime_dados()


