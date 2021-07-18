''' Exerc.03- Aula 03 
Desenvolva um algoritmo que leia o peso e altura de uma pessoa, calcule seu IMC
e mostre seu status de acordo com:
Abaixo de 18,5 – abaixo do peso
Entre 18.5 e 25 – peso ideal
Entre 25 e 30 - sobrepeso
Entre 30 e 40 - obesidade
Acima de 40 - obesidade mórbida
Para o cálculo do IMC, considere: IMC = peso / (altura x altura) '''
#Felipe Backes Kettl
peso = float(input('Digite seu peso(em kg e apenas numeros): '))
altura = float(input('Digite sua altura(em metros e apenas numeros: '))
imc = peso / (altura**2)

if imc < 18.5:
    print('Status: abaixo do peso.')
elif imc < 25:
    print('Status: peso ideal.')
elif imc < 40:
    print('Status: obesidade')
else:
    print('Status: obesidade mórbida')