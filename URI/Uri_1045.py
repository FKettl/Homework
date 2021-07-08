a, b, c = [float(x) for x in input().split()]
triangulo = True
if a >= b + c or b >= c + a or c >= b + a:
    print('NAO FORMA TRIANGULO')
    triangulo = False
elif a**2 == b**2 + c**2 or b**2 == c**2 + a**2 or c**2 == b**2 + a**2:
    print('TRIANGULO RETANGULO')
elif a**2 > b**2 + c**2 or b**2 > c**2 + a**2 or c**2 > b**2 + a**2:
    print('TRIANGULO OBTUSANGULO')
elif a**2 < b**2 + c**2 or b**2 < c**2 + a**2 or c**2 < b**2 + a**2:
    print('TRIANGULO ACUTANGULO')

if a == b == c:
    print('TRIANGULO EQUILATERO')
elif (a==b!=c or b==c!=a or c==a!=b) and triangulo == True :
    print('TRIANGULO ISOSCELES')