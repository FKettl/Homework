'''Aula 07 - Exerc.03
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

Média de aproveitamento | Conceito:
 Entre 9.0 e 10.0       | A
 Entre 7.5 e 9.0        | B
 Entre 6.0 e 7.5        | C
 Entre 4.0 e 6.0        | D
 Entre 4.0 e zero       | E

 o algoritmo deve mostrar na tela as notas, a média, o conceito correspondente 
 e a mensagem ''APROVADO'' se o conceito for A, B ou C ou ''REPROVADO'' se o conceito for D ou E.
'''
#Felipe Backes Kettl

while True:
    #Recebe dois valores que equivales a duas notas, respectivamente, var x e y.
    x, y = [float(i) for i in input('Insira as duas notas (Com um espaço entra elas): ').split()]
    media = (x+y)/2
    conceito = 0
    situacao = 0

    #Define o conceito do aluno com base na média das notas.
    if media <= 10.0 and media >= 9.0:
        conceito = 'A'
    elif media < 9.0 and media >= 7.5:
        conceito = 'B'
    elif media < 7.5 and media >= 6.0:
        conceito = 'C'
    elif media < 6.0 and media >= 4.0:
        conceito = 'D'
    elif media < 4.0: 
        conceito = 'E'
    
    #Define a situação do aluno com base no conceito dele.
    if conceito == 'A' or conceito == 'B' or conceito == 'C':
        situacao = 'APROVADO'
    elif conceito == 'D' or conceito == 'E':
        situacao = 'REPROVADO'
    print(f'As notas são {x} e {y} sendo a média {media}, portanto o aluno foi: {situacao}.')

    #Opção para o usuário verificar outro aluno ou parar o programa.
    continuar = input('Deseja verificar outro aluno? [S/N] ').upper().strip()
    if continuar == 'N':
        print('Fim.')
        break
    elif continuar == 'S':
        continue


