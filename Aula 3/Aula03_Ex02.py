''' Exerc.02- Aula 03
Elabore um programa que calcule o valor a ser pago por um produto,
considerando seu preço normal e a condição de pagamento.
a. à vista (dinheiro ou cheque) – 10% de desconto
b. 1x no cartão – 5% de desconto
c. 2x cartão – preço normal
d. 3x ou mais no cartão - 20% de juros  '''

preço = float(input('Preço do produto: R$ '))

while True:
    opçao = str(input('Escolha uma opção de pagamento(digite apenas o numero):\n 1. à vista (dinheiro ou cheque) – 10% de desconto\n'
    ' 2. 1x no cartão – 5% de desconto\n 3. 2x cartão – preço normal\n 4. 3x ou mais no cartão - 20% de juros\n Opção: '))
    if opçao == '1':
        print(f'Preço a pagar: R$ {preço*0.9}')
        break 
    elif opçao == '2':
        print(f'Preço a pagar: R$ {preço*0.95}')
        break 
    elif opçao == '3':
        print(f'Preço a pagar: R$ {preço}')
        break 
    elif opçao == '4': 
        print(f'Preço a pagar: R$ {preço*1.2}')
        break 
    else:
        print('Opção inválida, digite novamente: ')
        continue