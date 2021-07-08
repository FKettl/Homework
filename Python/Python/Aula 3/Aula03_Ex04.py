''' Exerc.04- Aula 03
Faça um programa que leia 3 notas de um aluno, calcule sua média e mostre seu
conceito final conforme a indicação abaixo:
Abaixo de 5 – Reprovado
Entre 5 e menor que 7 – Em recuperação
Igual ou maior que 7 – Aprovado '''

a = float(input('Digite sua nota 1: ')) 
b = float(input('Digite sua nota 2: ')) 
c = float(input('Digite sua nota 3: ')) 
media = (a + b + c) / 3

if media < 5:
    print('Situação: Reprovado')
elif media < 7:
    print('Situação: Em recuperação')
else:
    print('Situação: Aprovado')