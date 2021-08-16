'''Aula 17 - Exerc.07
URI 1953
'''
#Felipe Backes Kettl

while True:
    try:
        turma = {'EPR': 0, 'EHD':0, 'INTRUSOS':0}
        qtsalunos = int(input())
        
        for x in range(qtsalunos):
            numero, curso = input().split()
            if (curso == 'EPR') or (curso == 'EHD'):
                turma[curso] += 1
            else:
                turma['INTRUSOS'] += 1
        
        print(f"EPR: {turma['EPR']}")
        print(f"EHD: {turma['EHD']}")
        print(f"INTRUSOS: {turma['INTRUSOS']}")
    except EOFError:
        break
    