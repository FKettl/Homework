'''Aula 05 - Ex 07
Richard Phillips Feynman era um físico americano muito famoso e ganhador do Prêmio Nobel de Física. 
Ele trabalhava em física teórica e também foi pioneiro no campo da computação quântica. 
Ele visitou a América do Sul por dez meses, dando palestras e aproveitando a vida nos trópicos.
Ele também é conhecido pelos livros "Surely You’re Joking, Mr. Feynman!" e "What Do You Care What Other People Think?",
 que inclui algumas de suas aventuras abaixo do equador.
Sua paixão da vida inteira era resolver e criar quebra-cabeças, trancas e códigos. 
Recentemente, um fazendeiro idoso da América do Sul, que hospedou o jovem físico em 1949, achou alguns papéis e notas que acredita-se terem pertencido a Feynman. 
Entre anotações sobre mesóns e eletromagnetismo, havia um guardanapo onde ele escreveu um simples desafio:
 "quantos quadrados diferentes existem em um quadriculado de N x N quadrados?".
No mesmo guardanapo havia um desenho, que está reproduzido abaixo, mostrando que para N = 2, a resposta é 5.
'''
#Felipe Backes Kettl


quadrados = 0

for x in range(1, 10000000000):   
   n = int(input())
   if n == 0:
       break
   for i in range(n, 0, -1):
       quadrados += i**2
   print(f'{quadrados}')
   quadrados = 0
    
#profe a range ta em 10000000000 pq eu fiz o codigo pra ser aceito no uri, e la ele espero q usemos o while, visto que não sabemos o numero de testes
#então pra enganar o site eu fiz a range um numero muito alto pra passar o numero de testes kkkkkk