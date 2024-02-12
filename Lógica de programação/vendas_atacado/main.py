print("Bem vindo a loja")

prod = float(input('Entre com o valor do produto: '))
quant = float(input('Insira a quantidade desejada: '))

if quant < 10:
    pagar = prod * quant 
    com_desc = pagar - (pagar * 0) 
    porcentagem = '(desconto de 0%)'


elif quant >= 10 and quant <= 99:
    pagar = prod * quant 
    com_desc = pagar - (pagar * (5 / 100))
    porcentagem = '(desconto de 5%)'


elif quant >= 100 and quant <= 999:
    pagar = prod * quant 
    com_desc = pagar - (pagar * (10 / 100)) 
    porcentagem = '(desconto de 10%)'
else:
    pagar = prod * quant 
    com_desc = pagar - (pagar * (15 / 100)) 
    porcentagem = '(desconto de 15%)'

print(f'O valor sem desconto foi: R$ {pagar:.2f}')
print(f'O valor com o desconto foi: R$ {com_desc:.2f} | {porcentagem}')