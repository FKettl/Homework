'''Aula 06 - Exerc.04
Implementar um programa que calcula o desconto previdenciário dos funcionários de uma empresa.
O algoritmo deve, dado um salário, retornar o valor do desconto proporcional ao mesmo. 

- O cálculo de desconto segue a seguinte regra: o desconto deve ser de 11% do valor do salário, entretanto, o valor máximo de desconto é R$320,00.
Sendo assim, seu programa deve verificar se calculará sobre 11%  do salário ou utilizará o teto R$320,00. 
No caso, de o desconto aplicado for R$320,00, seu programa deve indicar qual foi o % de desconto aplicado para este funcionário.

- Critério de parada definido pelo usuário (perguntar a cada verificação se deseja continuar)
'''
#Felipe Backes Kettl

salario = float(input('Digite um salário a ser calculado: R$ '))
desconto = salario*0.11
descteto = (320/salario)*100
if desconto > 320:
    print(f'O valor de desconto é 320 reais, que equivalem a {descteto:.2f}% do total')
elif desconto <= 320:
    print(f'O valor de desconto é {desconto} reais')

while True:
    resposta = input('Deseja calcular outro valor? [S/N]').upper().strip()
    if resposta == 'N':
        print('Fim.')       
        break
    if resposta == 'S':
        salario = float(input('Digite um salário a ser calculado: R$ '))
        desconto = salario*0.11
        descteto = (320/salario)*100
        if desconto > 320:
            print(f'O valor de desconto é 320 reais, que equivalem a {descteto:.2f}% do total')
        elif desconto <= 320:
            print(f'O valor de desconto é {desconto} reais')
        