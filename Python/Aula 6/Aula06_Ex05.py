'''Aula 06 - Exerc.05
Florianópolis é uma cidade que possui diversas praias.
De forma a melhor orientar os turistas a Secretaria Municipal de Turismo mediu a distância de cada praia a partir do centro da cidade.
Seu programa deve solicitar que o usuário indique o número de praias que deseja cadastrar.
E para cada praia, indique o nome (string) e a distância do centro da cidade (int).
A partir destas informações, seu programa deve obter os seguintes dados:
•   qual a praia mais distante do centro da cidade;
•   quantas praias estão entre 15 e 20 km do centro;
•  qual a distância média das praias (arredondado na primeira casa decimal);
 '''

n = int(input('Indique o número de praias que deseja cadastrar: '))
count = 0
maisdistante = 0
nomemaisdistante = 0
countdistancia = 0
distanciatotal = 0
while count < n:
    nome = input('Qual o nome da praia? ')
    distancia = float(input('Qual sua distancia do centro da cidade? [Em KM, apenas numeros] '))
    if distancia > maisdistante:
        maisdistante = distancia
        nomemaisdistante = nome
    if distancia >= 15 and distancia <= 20:
        countdistancia += 1
    distanciatotal += distancia
    count += 1
print(f'A praia mais distante é {nomemaisdistante}.\nHá {countdistancia} praias entre 15 a 20 km do centro. \nA distânia média das praias até o centro é {distanciatotal/n:.1f}')
