'''Aula 16 - Exerc.01
 1) Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista.
 No final mostre:
 A) quantas pessoas foram cadastradas;
 B) a média de idade do grupo
 C) uma lista com todas as mulheres
 D) uma lista com todas as pessoas com idade acima da média 
 '''
 #Felipe Backes Kettl

dados = {}
conjunto = []
total = 0
while True:
    dados['Nome'] = input('Digite o nome: ').capitalize()
    dados['Idade'] = int(input('Digite a idade: '))
    dados['Sexo'] = input('Digite o sexo: [M/F] ').upper()
    conjunto.append(dados.copy())
    continuar = input('Deseja cadastrar outra pessoa? [S/N]: ' ).upper()
    while continuar not in 'SN':
        continuar = input('Deseja cadastrar outra pessoa? [S/N]: ' ).upper()
    if continuar == 'N':
        break
for x in range(len(conjunto)):
    total += conjunto[x]['Idade'] 

mulheres = [conjunto[x]['Nome'] for x in range(len(conjunto)) if conjunto[x]['Sexo'] == 'F' ]
maisQueMedia = [conjunto[x]['Nome'] for x in range(len(conjunto)) if conjunto[x]['Idade'] > (total/len(conjunto))]

print(f'Foram cadastradas {len(conjunto)} pessoa(s).')
print(f'A média de idade do grupo é {total/len(conjunto):.1f}')
print(f'A(s) mulher(es) do grupo é(são): {mulheres}')
print(f'A(s) pessoa(s) com a idade acima da a média é(são): {maisQueMedia}')
