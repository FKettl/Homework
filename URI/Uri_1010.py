codigo1, numero1, valor1 = input().split()
codigo2, numero2, valor2 = input().split()
codigo1 = int(codigo1)
codigo2 = int(codigo2)
numero1 = int(numero1)
numero2 = int(numero2)
valor1 = float(valor1)
valor2 = float(valor2)
valorpag1 = numero1 * valor1
valorpag2 = numero2 * valor2
valortot = valorpag1 + valorpag2
print(f"VALOR A PAGAR: R$ {valortot:.2f}")