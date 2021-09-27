from Carrinho import *
#Felipe Kettl e Samantha Costa
class produto():
    _estoque = {}
    
    def __init__(self, nome: str, preço: float, qtd: int):
        self.nome = nome
        self.qtd = qtd
        self.preço = preço
        self.adicionarAoEstoque(nome, preço, qtd)
        
    @classmethod
    def adicionarAoEstoque(cls, nome, preço, qtd):
        #if type(self).__name__ == produto: #se está em produto, adiciona ao estoque.
            cls._estoque[nome] = [preço, qtd]
        #else:
         #   premium.adicionarAoEstoque(self, nome, preço, qtd)

    def produzir(self, nome, qtd):
        if nome in produto._estoque:
            self.qtd += qtd
            produto._estoque[nome][1] += qtd
            print(f'{qtd} {nome} (s) produzidos.')
        else:
            print('Ainda não produzimos esse produto.')
    
    def vender(self, qtd): 
        if self.qtd < qtd:
            print('Não há estoque o suficiente.')
        else:
            carrinho(self.nome, qtd, self.preço)
            print(f'{self.nome} ({qtd}) adicionado no carrinho.')  
                 
    @classmethod
    def removerDoEstoque(cls): #método que remove do estoque os itens comprados
        for x in range(len(carrinho.lista)):
            nome = carrinho.lista[x][0]
            if nome in cls._estoque:
                cls._estoque[nome][1] -= carrinho.lista[x][1]

    def checarEstoque(): #mostra tanto o estoque normal quanto o premium.
        print('-'*14, 'Produtos', '-'*14)
        for key, value in produto._estoque.items():
            print(f'{key}: R$ {value[0]:.2f}, {value[1]} em estoque')
        print()
        print('-'*9, 'Produtos Premium:', '-'*10)
        for key, value in premium._estoque.items():
            print(f'{key}: R$ {value[0]:.2f}, {value[1]} em estoque')
        
    @classmethod
    def removerProduto(cls, nome):
        del cls._estoque[nome]
        print('Produto removido.')
    
    @classmethod
    def alerta(cls):
        for k, v in cls._estoque.items(): #para cada lista no estoque
           if v[1] == 0: #se a quantidade está em 0
               print(f'Alerta: Estoque do produto "{k}" está vazio. ')

    @classmethod
    def checarTipo(cls):
        return cls

class premium(produto):
    _estoque = {}

    def __init__(self, nome, preço, qtd):
        super().__init__(nome, preço, qtd)
        
    def produzir(self, nome, qtd):
        if self.nome in premium._estoque:
            self.qtd += qtd
            premium._estoque[nome][1] += qtd
            print(f'{qtd} {nome} produzidos.')
        else:
            print('Ainda não produzimos esse produto.')

    def vender(self, qtd): 
        if qtd <= 5:
            super().vender(qtd)
        else:
            print('Máximo de 5 produtos premium por cliente.')
