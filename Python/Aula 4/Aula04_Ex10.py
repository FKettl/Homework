'''Exerc.10 - Aula 04
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:
se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A**2 = B**2 + C**2, apresente a mensagem: TRIANGULO RETANGULO
se A**2 > B**2 + C**2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A**2 < B**2 + C**2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
'''
#Felipe Backes Kettl
  
a, b, c = [float(x) for x in input().split()]
triangulo = True
if a >= b + c or b >= c + a or c >= b + a:
    print('NAO FORMA TRIANGULO')
    triangulo = False
elif a**2 == b**2 + c**2 or b**2 == c**2 + a**2 or c**2 == b**2 + a**2:
    print('TRIANGULO RETANGULO')
elif a**2 > b**2 + c**2 or b**2 > c**2 + a**2 or c**2 > b**2 + a**2:
    print('TRIANGULO OBTUSANGULO')
elif a**2 < b**2 + c**2 or b**2 < c**2 + a**2 or c**2 < b**2 + a**2:
    print('TRIANGULO ACUTANGULO')

if a == b == c:
    print('TRIANGULO EQUILATERO')
elif (a==b!=c or b==c!=a or c==a!=b) and triangulo == True :
    print('TRIANGULO ISOSCELES')

#sem poder usar o comando .sort() fica bem mais complexo visto que o valor maior poder ser qualquer um 
#tive que usar triangulo == true como condição pro isosceles, se não ele printava não triangulo e isosceles pra alguns valores como 5 5 12
#o triangulo = true no começo é porque se ele fosse qualquer coisa fora ''não forma triangulo'' ficaria com a variavel triangulo sem definição e daria erro.