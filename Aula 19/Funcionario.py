class funcionario:

    _bancodedados = {}    

    def __init__(self, nome, salarioatual, reajuste='Não Recebeu'):
        self.nome = nome
        self.salarioatual = float(salarioatual)
        self.reajuste = reajuste
        self.salarioreajustado = 0
        self._bancodedados[nome] = [float(salarioatual), self.salarioreajustado]

    def checar_funcionarios(self):
        for nome, salario in self._bancodedados.items():
            print(f'Nome: {nome}, Salário sem reajuste: {salario[0]:.2f}', end = '') 
            if salario[1] != 0:
                print (f', com reajuste: {salario[1]:.2f}')
            else:
                print()
        print()



    def reajustar_salario(self):
        if self.reajuste == 'Não Recebeu':
            self.reajuste = 'Recebeu'
            if 1500.00 <= self.salarioatual < 1750.00:
                self.salarioreajustado = self.salarioatual * 1.12
            elif 1750.00 <= self.salarioatual < 2000.00:
                self.salarioreajustado = self.salarioatual * 1.10
            elif 2000.00 <= self.salarioatual < 3000.00:
                self.salarioreajustado = self.salarioatual * 1.07
            elif 3000.00 <= self.salarioatual:
                self.salarioreajustado = self.salarioatual * 1.05
            self._bancodedados[self.nome][1] = self.salarioreajustado
            print(f'O {self.nome} recebe {self.salarioatual}, portanto o sálario reajustado é {self.salarioreajustado:.2f}')
        else:
            print('Esse funcionario já recebeu reajuste')
    
    