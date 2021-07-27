'''Aula 12 - Exerc.01
Implemente um sistema que manipule as notas de um aluno.
Restrição: 0 <= Nota <= 10
Ações esperadas:
a) Indicar a média do aluno;
b) Indicar a maior nota;
c) Indicar a menor nota.
d) Retorna a diferença entre a maior e a menor nota.
Considerar que não existem notas iguais.
'''
#Felipe Backes Kettl

n = [int(x) for x in input('Digite as notas do aluno: ').split()]
n.sort()
maior = n[len(n)-1]
menor = n[0]
total = 0
for x in range(len(n)):
    total += n[x]
media = total/len(n)
diferença = maior - menor
print(f'Média do alun: {media} \nMaior nota: {maior} \nMenor nota: {menor} \nA diferença entre a maior e a menor é: {diferença}')    

