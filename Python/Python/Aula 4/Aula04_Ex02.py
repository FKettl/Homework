'''Exerc.02- Aula 04
Triplo do maior:
 Escreva um algoritmo que declare duas variáveis de nomes: valor1 e valor2;
- leia estes valores do teclado (valores inteiros);
- escreva uma linha na saída, contendo um inteiro, o triplo do maior dos dois valores lidos da entrada. 
Restrições: 
A entrada obedece às seguintes restrições: 
0 ≤ A ≤ 1000 
0 ≤ B ≤ 1000 
A ≠ B
Exemplo de saída esperada:
Valor 1: 10;
Valor 2: 11;
Saída : 33  
'''
#Felipe Backes Kettl

print('Escreva dois valores maiores ou iguais a 0 e menores ou iguais a 1000 sendo eles diferentes entre si.')
valor1 = int(input('Escreva um valor: '))
valor2 = int(input('Escreva outro valor: '))
if 0 <= valor1 <= 1000 and 0 <= valor2 <= 1000 and valor1 != valor2:
    if valor1 > valor2:
        print(f'Triplo do valor 1: {valor1*3}')
    else:
        print(f'Triplo do valor 2: {valor2*3}')
else:
    print('Uma das restrições não foi cumprida.')
