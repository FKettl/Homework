#Felipe Kettl e Samantha Costa
class carrinho():
    lista = [] # lista de produtos no carrinho e sua quantidade
    listasonome = []
    total = 0

    def __init__(self, nome, qtd, preço):
        existe = False
        indice = 0
        for x in carrinho.lista: # checa cada lista nos carrinhos
            if x[0] == nome: #x[0] é nome do produto no carrinho
                existe = True
                indice = carrinho.lista.index(x)
        if existe == False:
            self.lista.append([nome, qtd]) # quantidade = quantidade a ser comprada
            self.somar(qtd, preço)
            self.listasonome.append(nome)
        else: # existe o item já no carrinho, só aumentar qtd
            carrinho.lista[indice][1] += qtd
        
    def somar(self, qtd, preço):
        carrinho.total += qtd*preço

    def exibirCaixa():
        for x in carrinho.lista:
            print(f'{x[0]}: {x[1]} unidades')
        print(f'Total a pagar no momento: R${carrinho.total:.2f}')
        if carrinho.lista == []:
            print('Carrinho vazio.')

    def fecharCompra(desconto = False):
        print('Finalizando compra')
        if desconto == False:
            print(f'O total a pagar é: R$ {carrinho.total:.2f}')  #retorna o valor final, soma de dos preços*qtd desejada em float
        else:
            total = carrinho.total * 0.9
            print('Clientes cadastrados recebem 10% de desconto.')
            print(f'Portanto, o total a pagar é: R$ {total:.2f}')
        carrinho.lista.clear()
        carrinho.listasonome.clear()
        carrinho.total = 0
    
    def cancelarCompra():
        carrinho.lista.clear()
        carrinho.listasonome.clear()
        carrinho.total = 0
        print('Compra cancelada com sucesso.')
    
    def removerItem(nome, qtd, preço):
        for x in carrinho.lista: # para cada lista dentro do carrinho
            if x[0] == nome: #x[0] é nome do produto no carrinho
                if x[1] > qtd:
                    x[1] -= qtd
                    carrinho.total -= qtd*preço
                    print('Item removido com sucesso.')
                elif x[1] == qtd: #removendo toda quantiidade do item no carrinho
                    carrinho.total -= qtd*preço
                    carrinho.lista.remove(x)
                    print('Item removido com sucesso.')
                    for x in carrinho.listasonome:
                        if x == nome:
                            carrinho.listasonome.remove(x)
                else:
                    print('Quantidade inválida.')