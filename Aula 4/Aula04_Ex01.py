'''Exerc.04- Aula 03
Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
Se ele ainda vai se alistar ao serviço militar;
Se está no momento de se alistar;
Se passou do tempo do alistamento.
Seu programa deve também mostrar o tempo que falta ou o que passou do prazo. 
As datas devem ser lidas do teclado (por enquanto não utilizar a função Date) 
'''
#Felipe Backes Kettl

ano = int(input('Você nasceu no ano: '))
idade = 2021 - ano
if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o seu alistamento.')
elif idade == 18:
    print('Você deve se alistar esse ano. Boa sorte, guerreiro!!!')
elif idade > 18: 
    print(f'O seu alistamento está {idade - 18} anos atrasado.')

