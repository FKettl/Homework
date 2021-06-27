'''Exerc.06- Aula 04
Este algoritmo deve receber dois valores, o primeiro valor indica o preço de um determinado produto e o segundo valor indica o valor pago.
 A partir destas informações, seu algoritmo deve calcular o troco (se houver) ou solicitar quantia faltante para finalizar o pagamento.
'''
#Felipe Backes Kettl

valorproduto = float(input('Preço do produto: R$ '))
valorpago = float(input('Valor pago: R$ '))

if (valorproduto - valorpago) > 0:
    print(f'Falta pagar: R$ {valorproduto - valorpago:.2f}')
elif (valorproduto - valorpago) < 0:
    print(f'O seu troco é: R$ {valorpago - valorproduto:.2f}')
else:
    print('Agradeçemos por nos escolher, tenha um bom dia!')