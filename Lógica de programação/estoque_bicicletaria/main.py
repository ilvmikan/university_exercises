print('Bem vindo ao Controle de Estoque da Bibicletaria')

peca_lista = []
cod_peca = 0

def cadastrarPeca(codigo):
    print('-----------------')
    print('Menu de Cadastro de Peças')
    print(f'Código da peça {codigo}')
    print('-----------------')

    nome = input('Digite o nome da peça: ')
    fab = input('Digite o fabricante da peça: ')
    valor = int(input('Digite o valor da peça: '))
    pecas = {'codigo': codigo, 'nome': nome, 'fabricante': fab, 'preço': valor}
    peca_lista.append(pecas.copy())

def consultarPeca():
    print('----------------------------')
    print('Menu de Consultar de Peças\n')
    print('----------------------------')
    while True:
        print('Escolha a opção desejada:')
        print('1 - Consultar todas as peças')
        print('2 - Consultar as peças por código')
        print('3 - Consultar as preças por fabricante')
        print('4 - Voltar')
        consulta = input('Escolha uma opção acima:\n>> ')

        if consulta == '1':
            print('Você escolheu \'Consultar todos as peças\'')
            for peca in peca_lista:
                print('---------------------')
                for key, value in peca.items():
                    print(f'{key}: {value}')

        elif consulta == '2':
            print('Você escolheu \'Consultar peça por código\'')
            escolha = int(input('Digite o código:\n>> '))
            for peca in peca_lista:
                if peca['codigo'] == escolha:
                    print('---------------------')
                    for key, value in peca.items():
                        print(f'{key}: {value}')
                print('---------------------')

        elif consulta == '3':
            print('Você escolheu \'Consultar peça por fabricante\'')
            escolha = input('Digite o código:\n>> ')
            for peca in peca_lista:
                if peca['fabricante'] == escolha:
                    print('---------------------')
                    for key, value in peca.items():
                        print(f'{key}: {value}')
                print('---------------------')

        elif consulta == '4':
            return
        else:
            print('Você digitou uma opção inválida.')

def removerPeca():
    print('----------------------')
    print('Menu de Remover Peças')
    print('----------------------')

    if len(peca_lista) == 0:
        print('Não existe peça para remover')
        print('-----------------------------')
        return
    
    remover = int(input('Digite o código da peça que deseja remover:\n>> '))
    for peca in peca_lista:
        if peca['codigo'] == remover:
            peca_lista.remove(peca)
            print('Peça removida!')

while True:
    print('========== MENU ==========')
    print('1 - Cadastrar Peça')
    print('2 - Consultar Peça')
    print('3 - Remover Peça')
    print('4 - Sair')
    escolha = input('Escolha uma opção acima:\n>> ')

    if escolha == '1':
        cod_peca += 1
        cadastrarPeca(cod_peca)
    elif escolha == '2':
        consultarPeca()
    elif escolha == '3':
        removerPeca()
    elif escolha == '4':
        print('Saindo...') 
        break
    else:
        print('Opção inválida!')
