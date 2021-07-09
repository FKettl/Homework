'''Aula 07 - Exerc.02
Faça um programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
indique, caso os lados formem um triângulo, se o mesmo é equilátero, isósceles ou escaleno.
dicas: três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triangulo Equilátero: três lados iguais;
Triangulo Isósceles: quaisquer dois lados iguais;
Triangulo Escaleno: três lados diferentes;
'''
#Felipe Backes Kettl


while True:
    #cria 3 var com a input de 3 lados.
    triangulo = 0
    tipo = 0
    a, b, c = [int(x) for x in input('Digite três lados (espaço entre eles): ').split()]

    #Define a existência ou não de um triângulo.
    if a+b >= c and b+c >= a and c+a >= b:
        triangulo = True
    else:
        triangulo = False

    #Caso exista triângulo define o tipo dele, caso contrario não.
    if triangulo == True:
        if a == b == c:
            tipo = 'Equilátero'
        elif a == b != c or a == c != b or c == b != a:
            tipo = 'Isósceles'
        elif a != b != c:
            tipo = 'Escaleno'
        print(f'Esses 3 lados formam um triângulo {tipo}.')
    elif triangulo == False:
        print('Esses 3 lados não formam um triângulo.')
    
    #Opção do usuário de continuar com outros 3 valores ou parar.
    continuar = input('Deseja continuar? [S/N] ').upper().strip()
    if continuar == 'S':
        continue
    elif continuar == 'N':
        print('Fim.')
        break
    


