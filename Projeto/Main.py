from Clientes import *
from Produto import *
from Carrinho import *
from time import sleep
#Felipe Kettl e Samantha Costa
# produtos pré-definidos - def __init__(self, nome: str, preço: float, qtd: int):
p1 = produto('Pão', 1.00, 20 )
p2 = premium('Bolo Red Velvet', 47.00, 8) 
p3 = produto('Salgado', 4.00, 20) # salgados no geral :)
p4 = produto('Brigadeiro', 2.00, 30)
p5 = premium('Pizza', 15.00, 8)
p6 = produto('Refrigerante (Lata)', 2.50, 40) 
produtosTotais = {p1.nome:p1, p2.nome:p2 , p3.nome:p3, p4.nome: p4, p5.nome: p5, p6.nome: p6}

# clientes pré-definidos
cliente1 = clientes('Samantha')
cliente2 = vip('Luciana')
cliente3 = clientes('Felipe Kettl')
listaDeCliente = {'Samantha': cliente1, 'Luciana': cliente2, 'Felipe Kettl': cliente3} 


while True:
    sleep(0.5)
    produto.alerta()
    premium.alerta()
    print()
    print('-'*14, 'PADARIA', '-'*14) 
    print('[ 1 ] - Adicionar produto ao carrinho') #OK
    print('[ 2 ] - Carrinho') #OK
    print('[ 3 ] - Produzir') #OK
    print('[ 4 ] - Checar estoque') #OK
    print('[ 5 ] - Cadastrar cliente') #OK
    print('[ 6 ] - Remover cliente') #OK
    print('[ 7 ] - Checar clientes') #OK
    print('[ 8 ] - Novo produto') #OK 
    print('[ 9 ] - Remover produto') #OK
    print('[ 0 ] - Sair do programa') #OK
    print('-'*37)
    option = input('Digite a opção: ')
    print('-'*37)
    print()
    
    
    if option.isnumeric() == True:
        option = int(option)
        
        if option == 0: # Sair do programa
            break

        # nas restrições de cliente e vip:
        # vip: pode comprar todos, produtos premium é max 5
        # cliente normal: produtos normais, desconto neles
        # não-cadastrado: produtos normais sem desconto

        elif option == 1: # Adicionar produto ao carrinho   OK
            nomeclientecomprando = input('Digite o nome do cliente: ').title().strip()
            if nomeclientecomprando in listaDeCliente:
                objetocliente = listaDeCliente[nomeclientecomprando]
                desconto = True
            else:
                print('Não está na lista de clientes cadastrados.')
                objetocliente = '0'
                desconto = False
            while True: #Falta por restrição de vip e normal
                nome = input('Qual produto? (Digite 0 para voltar) ').title().strip()
                if nome == '0':
                    print('Voltando...')
                    break
                elif nome in produtosTotais:
                    objetoproduto = produtosTotais[nome]
                    if objetoproduto.checarTipo() == premium: 
                        if objetocliente == '0':
                            print('Apenas clientes vips podem comprar produtos premium.')
                        elif objetocliente.checarTipo() == vip:
                            qtd = input('Quantas unidades? (Digite 0 para voltar): ')
                            if (qtd.isnumeric() == True) and (qtd != '0') : #checa se a qtd é número
                                qtd = int(qtd)
                                objetoproduto.vender(qtd)
                                
                            elif qtd == '0':
                                print('Voltando...') 
                                break
                            else:
                                print('Entrada inválida.')
                        else:
                            print('Apenas clientes vips podem comprar produtos premium.')
                    else: # não é produto premium
                        qtd = input('Quantas unidades? (Digite 0 para voltar): ')
                        if (qtd.isnumeric() == True) and (qtd != '0') : #checa se a qtd é número
                            qtd = int(qtd)
                            objetoproduto.vender(qtd)
                            
                        elif qtd == '0':
                            print('Voltando...') 
                            break
                        else:
                            print('Entrada inválida.')

                else:
                    print('Não existe esse item em estoque.')
              
        elif option == 2: # Carrinho OK
            while True:
                sleep(0.5)
                print()
                print('-'*37)
                print('[ 0 ] - Voltar')
                print('[ 1 ] - Checar carrinho')
                print('[ 2 ] - Remover item do carrinho')
                print('[ 3 ] - Cancelar carrinho')
                print('[ 4 ] - Finalizar compra')
                print('-'*37)
                option2 = input('Digite a opção: ')
                print('-'*37)
                if option2.isnumeric() == True:
                    option2 = int(option2)
                    
                    if option2 == 0:
                        print('Voltando...')
                        break
                        
                    elif option2 == 1: # Checar carrinho
                        carrinho.exibirCaixa()
                        input('\nDigite algo para retornar ao menu do carrinho: ')
                    
                    elif option2 == 2: # Remover item do carrinho
                        itemremover = input('Remover qual item? (Digite 0 para voltar) ').title().strip()
                        if itemremover == '0':
                            print('Voltando...')
                        else:   
                            if itemremover in carrinho.listasonome:
                                itemremoverqtd = int(input('Remover quantas unidades? (Digite 0 para voltar) '))
                                if itemremover == 0:
                                    print('Voltando...') 
                                else:
                                    carrinho.removerItem(itemremover, itemremoverqtd, produtosTotais[itemremover].preço)
                            else:
                                print('Não há esse item no carrinho.')
                    
                    elif option2 == 3: # Cancelar carrinho
                        carrinho.cancelarCompra()
                        print('Compra cancelada.')
                        break
                        
                    elif option2 == 4: # Finalizar compra
                        for x in range(len(carrinho.lista)):
                            nome = carrinho.lista[x][0]
                            objeto = produtosTotais[nome]
                            objeto.qtd -= carrinho.lista[x][1]
                        produto.removerDoEstoque()
                        premium.removerDoEstoque()                        
                        carrinho.fecharCompra(desconto)
                        print('Produtos removidos do estoque.')
                        break
                    else: 
                        print('Entrada inválida.')
                else:
                    print('Entrada inválida.')
        
        elif option == 3: # Produzir OK
            while True:
                produzirin = input('O que produzir (digite 0 para voltar): ').title().strip()
                if produzirin == '0':
                    print('Voltando...')
                    break
                else:
                    qtd = input('Quantas unidades? (digite 0 para voltar): ').strip()
                    if (qtd.isnumeric() == True) and (qtd != '0'):
                        produzirin = produzirin.title()
                        if produzirin in produtosTotais:
                            tipo = type(produtosTotais[produzirin])
                            qtd = int(qtd)
                            tipo.produzir(produtosTotais[produzirin], produzirin, qtd)
                        else:
                            print('Produto inválido')
                    elif qtd == '0':
                        print('Voltando...')
                        break
                    else:
                        print('Entrada inválida.')  
                
        elif option == 4: # Checar estoque #OK
            produto.checarEstoque()
            input('\nDigite algo para retornar ao menu principal: ')
           
        
        elif option == 5: # Cadastrar cliente #OK
            while True:
                print('[ 1 ] - Cadastrar Cliente Normal: ')
                print('[ 2 ] - Cadastrar Cliente Vip: ')
                print('[ 3 ] - Voltar')
                option3 = input('Digite a opção: ')
                if option3.isnumeric() == True:
                    option3 = int(option3)
                    if option3 == 1:
                        nomecliente = input('Digite o nome do cliente (0 para voltar): ').title().strip()
                        if nomecliente == '0':
                            print('Voltando...')
                        else:  
                            listaDeCliente[nomecliente] = clientes(nomecliente)
                            print('Cadastro concluido')
                    elif option3 == 2:
                        nomecliente = input('Digite o nome do cliente Vip (0 para voltar): ').title().strip()
                        listaDeCliente[nomecliente] = vip(nomecliente)
                        print('Cadastro concluido')
                    elif option3 == 3:
                        print('Voltando...')
                        break
                    else: 
                        print('Entrada inválida.')
                else:
                    print('Entrada inválida.')

        elif option == 6: # remover cliente #OK
            nomeclienteremover = input('Digite o nome do cliente que quer remover (Digite 0 para voltar): ').title().strip()
            if nomeclienteremover in listaDeCliente:
                clientes.removerCliente(listaDeCliente[nomeclienteremover])
                del listaDeCliente[nomeclienteremover]
            elif nomeclienteremover == '0':
                print('Voltando...')
            else:
                print('Entrada inválida.')
            
        elif option == 7: #OK
            clientes.checarClientes()
            input('\nDigite algo para retornar ao menu principal. ')

        elif option == 8: # novo produto #OK
            nomenovoproduto = input('Digite o nome do novo produto (Digite 0 para cancelar): ').title().strip()
            if nomenovoproduto == '0':
                print('Voltando...')
            else:
                preçonovoproduto, qtdnovoproduto, épremium = input('Digite o preço, o estoque inicial e se ele é premium ou normal [P/N] (Digite 0 0 0 para voltar): ').split()
                if (preçonovoproduto == '0') and (qtdnovoproduto == '0'):
                    print('Voltando...')
                else:
                    épremium = épremium.upper()
                    nomenovoproduto = nomenovoproduto.title()
                    preçonovoproduto, qtdnovoproduto = float(preçonovoproduto), int(qtdnovoproduto)
                    if épremium == 'P':
                        produtosTotais[nomenovoproduto] = premium(nomenovoproduto, preçonovoproduto, qtdnovoproduto)
                        print('Novo produto premium adicionado com sucesso. ')
                    elif épremium == 'N':
                        produtosTotais[nomenovoproduto] = produto(nomenovoproduto, preçonovoproduto, qtdnovoproduto)
                        print('Novo produto adicionado com sucesso. ')
                    else:
                        print('Por favor tente novamente e digite N ou P para o tipo de produto.')
        
        
        elif option == 9: # remover produto #OK
            nomeremoverproduto = input('Digite o nome do produto que deseja remover.').title().strip()
            if nomeremoverproduto in produto._estoque:
                produto.removerProduto(nomeremoverproduto)
            elif nomeremoverproduto in premium._estoque:
                premium.removerProduto(nomeremoverproduto) 
            else:
                print('Não existe esse produto em nossa padaria. ')
                
        else: #termina verificação de option aqui
            print('Este número não está nas opções do menu. Tente novamente.')
    else:
        print('Entrada inválida.')

print('Fim do programa. ')