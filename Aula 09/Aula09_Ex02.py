'''Aula 09 - Exerc.02
URI 2417
''' 
#Felipe Backes Kettl

cv, ce, cs, fv, fe, fs = [int(x) for x in input('Digite vitórias, empates e saldos de gol (nesse ordem) primeiro do time C depois do time F (ex: VC, EC, SC, VF, EF, SF): ').split()]

while True:
    if (0 <= cv <= 100) and (0 <= ce <= 100) and (0 <= fv <= 100) and (0 <= fe <= 100) and (-1000 <= cs <= 1000) and (-1000 <= fs <= 1000):
        break
    else:
        cv, ce, cs, fv, fe, fs = [int(x) for x in input('Digite vitórias, empates e saldos de gol (nesse ordem) primeiro do time C depois do time F (ex: VC, EC, SC, VF, EF, SF): ').split()]

vencedor = ''
pontosc = cv*3 + ce 
pontosf = fv*3 + fe
if pontosc > pontosf:
    vencedor = 'C'
elif pontosf > pontosc:
    vencedor ='F'
else:
    if cs > fs:
        vencedor = 'C'
    elif fs > cs:
        vencedor = 'F'
    else:
        vencedor = '='

print(vencedor)    
