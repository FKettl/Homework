'''Aula 08 - Exerc.09
Considerar uma turma da Disciplina de Cálculo I, com 5 alunos, fazer um programa que tenha uma função que calcule a média das notas da turma
e verifique o aluno com a melhor nota. Esta função deve retornar a média da turma e a nota do aluno com a média mais alta.
No programa principal após conhecer o média mais alta, informe seu status (aprovado, reprovado ou em recuperação).
Para definir o status assuma a seguinte premissa: Considerando que essas regras funcionam da mesma forma que funcionam na UFSC:

se a média for 5.75 ou maior, o aluno está aprovado,
se o aluno não estiver aprovado mas a nota for maior ou igual a 2.75, ele tem o direito de fazer a prova de recuperação
se a média for menor que 2.75 ele está reprovado.

'''
#Felipe Backes Kettl


def calcmedia():
    total = 0
    melhoraluno = 0
    maiornota = 0 
    for x in range(1, 6):
        nota = float(input(f'Digite a nota do aluno {x}: '))
        total += nota
        if nota > maiornota:
            melhoraluno = x
            maiornota = nota

    media = total/5
    return media, maiornota, melhoraluno

iniciar = input('Deseja calcular a média da turma? [S/N] ').upper().strip()
situação = ''
if iniciar == 'S':
    media, maiornota, melhoraluno = calcmedia()
    if maiornota >= 5.75:
        situação = 'aprovado'
    elif 2.75 <= maiornota < 5.75:
        situação = 'em recuperação' 
    else:
        situação = 'reprovado'
    print(f'A média da turma é {media:.2f} \nA maior média é {maiornota:.2f} e pertencente ao aluno {melhoraluno}, que está {situação}.')
else:
    print('Fim.')