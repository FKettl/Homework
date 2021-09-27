#Felipe Kettl e Samantha Costa
class clientes():
    listaclientes = []

    def __init__(self, nome): # cadastra o cliente
        self.nome = nome
        self.listaclientes.append(nome)
    
    def removerCliente(self):
        nome = self.nome
        self.listaclientes.remove(nome)
        print('Cliente removido.')
        
    def checarClientes():
        print('-'*14, 'Clientes', '-'*14)
        for x in clientes.listaclientes:
            print(x)
        print('-'*16, 'Vips', '-'*16)
        for x in vip.listaclientes:
            print(x)
    
    @classmethod
    def checarTipo(cls):
        return cls

class vip(clientes):
    listaclientes = []
    
    def __init__(self, nome):
        super().__init__(nome)



