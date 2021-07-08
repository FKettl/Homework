numeromaior = 0
posição = 0
for x in range(100):
    numero = int(input())
    if numero > numeromaior:
        numeromaior = numero
        posição = x + 1 
print(numeromaior)
print(posição)