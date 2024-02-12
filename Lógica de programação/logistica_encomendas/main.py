print('Bem vindo a Companhia de Logística X')

def dimensoesObjeto():
    while True:
        try:
            altura = int(input('Qual é a altura do objeto (em cm): \n>> '))
            cpmt = int(input('Digite o comprimento do objeto (em cm): \n>> '))
            largura = int(input('Qual é a largura do objeto (em cm): \n>> '))
            volume = altura * largura * cpmt

            if volume < 1000:
                print(f'O volume do objeto é (em cm²): {volume:.1f}')
                return 10
            elif 1000 <= volume < 10000:
                print(f'O volume do objeto é (em cm²): {volume:.1f}')                
                return 20
            elif 10000 <= volume < 30000:
                print(f'O volume do objeto é (em cm²): {volume:.1f}')
                return 30
            elif 30000 <= volume < 100000:
                print(f'O volume do objeto é (em cm²): {volume:.1f}')
                return 50
            else:
                print(f'O volume do objeto é (em cm²): >> {volume:.1f} <<')
                print('Não aceitamos objetos com dimensões tão grandes')
                continue
            
        except ValueError:
            print('Você digitou alguma dimensão do objeto com valor não numérico')
            print('Por favor entre com as dimensões desejadas novamente!')
            continue

def pesoObjeto():
    while True:
        try:
            peso = float(input('Digite o peso do objeto (em kg): \n>> '))

            if peso <= 0.1:
                return 1
            elif 0.1 <= peso < 1:
                return 1.5
            elif 1 <= peso < 10:
                return 2
            elif 10 <= peso < 30:
                return 3
            else:
                print('Não aceitamos algo tão pesado!!!')
                continue
            
        except ValueError:
            print('Você digitou o peso do objeto com valor não numérico.')
            print('Por favor, informe o peso novamente.')

def rotaObjeto():
    while True:
        try:
            print('Selecione a rota:')
            print('RS - De Rio de Janeiro até São Paulo')
            print('SR - De São Paulo até Rio de Janeiro')
            print('BS - De Brasília até São Paulo')
            print('SB - De São Paulo até Brasília')
            print('BR - De Brasília até Rio de Janeiro')
            print('RB - De Rio de Janeiro até Brasília')
            rota = input("Informe a rota desejada: \n>> ").upper()

            if rota == 'RS' or rota == 'SR':
                return 1
            elif rota == 'BS' or rota == 'SB':
                return 1.2
            elif rota == 'BR' or rota == 'RB':
                return 1.5
            else:
                print('Rota inválida. Por favor, digite uma rota válida.')
                continue
            
        except ValueError:
            print('Erro no valor digitado. Por favor, entre com a rota desejada novamente.')

dimensao_retornado = dimensoesObjeto()
peso_retornado = pesoObjeto()
rota_retornado = rotaObjeto()

total = dimensao_retornado * peso_retornado * rota_retornado

print(f'Total a pagar (R$): {total:.2f} (dimensões: {dimensao_retornado} * peso: {peso_retornado} * rota: {rota_retornado})')
