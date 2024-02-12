print('Bem vindo a lanchonete')
print('{}Cardápio{}'.format('*' * 18, '*' * 18))
print('| Código |        Descrição      | Valor |')
print('|   100  |    Cachorro Quente    | 9,00  |')
print('|   101  | Cachorro Quente Duplo | 11,00 |')
print('|   102  |          X-Egg        | 12,00 |')
print('|   103  |        X-Salada       | 12,00 |')
print('|   104  |         X-Bacon       | 14,00 |')
print('|   205  |         X-Tudo        | 17,00 |')
print('|   200  |    Refrigerante Lata  | 5,00  |')
print('|   201  |       Chá Gelado      | 4,00  |')

contador_total = 0

while True:
    cod = int(input('Entre com o código desejado: ')) 

    if cod == 100: 
        print('==== Você pediu um CACHORRO-QUENTE no valor de R$ 9,00. ====') 
        contador_total += 9 

    elif cod == 101: 
        print('==== Você pediu um CACHORRO-QUENTE DUPLO no valor de R$ 11,00. ====') 
        contador_total += 11 

    elif cod == 102: 
        print('==== Você pediu um X-EGG no valor de R$ 12,00. ====')
        contador_total += 12

    elif cod == 103: 
        print('==== Você pediu um X-SALADA no valor de R$ 12,00. ====')
        contador_total += 12

    elif cod == 104:
        print('==== Você pediu um X-BACON no valor de R$ 14,00. ====')
        contador_total += 17

    elif cod == 105:
        print('==== Você pediu um X-TUDO no valor de R$ 17,00. ====') 
        contador_total += 17

    elif cod == 200: 
        print('==== Você pediu um REFRIGERANTE DE LATA no valor de R$ 5,00. ====') 
        contador_total += 5

    elif cod == 201:
        print('==== Você pediu um CHÁ GELADO no valor de R$ 4,00. ====')
        contador_total += 4 

    else:
        print('==== Você escolheu um código inválido ====')
        continue

    resposta = int(input('Deseja pedir mais alguma coisa?\n[1] SIM\n[2] NÃO\n>> '))
    if resposta == 1:
        continue
    else:
        print(f'O total a ser pago é: R$ {contador_total:.2f}')         
        break




