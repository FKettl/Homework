class Pessoa:

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    
    def comer(self, alimento):
        if self.falando:
            print(f'{self.nome} está ocupado falando.')
            return
        if self.comendo:
            print(f'{self.nome} já está comendo!')
            return
        
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True
    
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        
        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} está de boca cheia.')
            return
        if self.falando:
            print(f'{self.nome} ja está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    
    def imprime_dados(self):
        print(f'{self.nome} tem {self.idade} anos. \n{self.nome} está comendo? {self.comendo} \n{self.nome} está falando? {self.falando}')
