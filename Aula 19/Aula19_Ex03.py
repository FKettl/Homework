'''Aula 19 - Exerc.03
Sistema veterinario
'''

class caes:

    _bixos = {}

    def __init__(self, raça, cor, peso, idade, nome, dono):
        self.raça = raça
        self.cor = cor
        self.peso = peso
        self.idade = idade
        self.nome = nome
        self.dono = dono  
        self._bixos[nome] = int(idade)
    

    def mais_velho():
        maisvelho = 0
        nomemaisvelho = ''
        for key, item in caes._bixos.items():
            if item > maisvelho:
                maisvelho = item
                nomemaisvelho = key
        return maisvelho, nomemaisvelho

class vip(caes):
        def __init__(self, raça, cor, peso, idade, nome, dono, periododebanho, restrição_alimentar=False):
            super().__init__(raça, cor, peso, idade, nome, dono)
            self.restrição_alimentar = restrição_alimentar
            self.banho = int(periododebanho)
            self.desconto = True




dog1 = vip('vira lata', 'preto', 40, 8, 'auau', 'Felipe', 3)
dog2 = caes('pincher', 'branco', 10, 2, 'mala', 'Bruna')
dog3 = caes('Pastor alemão', 'Amarelo e preto', 30, 40, 'Alpha', 'Rodrigo')
dog4 = vip('Poodle', 'branco', 8, 7, 'fifi', 'Laura', 4)
idade, nome = caes.mais_velho()
print(f'O mais velho é o {nome} com {idade} anos')
print(caes._bixos)
