#Ex01.: match case
n = int(input("""\n-----Menu-----
                 
[1] - Marketing\n[2] - Financeiro\n[3,4,5] - ADM\n[6,7,8,9] - T.I.\n[10] - Serviços Gerais

Informe um número de acesso: """))

match n:
    case 1:
        print('Marketing')
    case 2:
        print('Financeiro')
    case 3|4|5:
        print('ADM')
    case 6|7|8|9:
        print('T.I.')
    case 10:
        print('Serviços Gerais')
    case _:
        print('Código não encontrado')

#Ex02.: verificando faixa etária
age = int(input('Informe sua idade: '))

match age:
    case i if 0 <= age < 12:
        print('Criança')
    case i if 12 <= age < 18:
        print('Adolescente')
    case i if 18 <= age < 65:
        print('Adulto')
    case i if age >= 65:
        print('Idoso')
    case _:
        print('Idade inválida')

#Ex03.: forma de pagamento:
price = float(input('Informe o valor da compra: '))
payment = int(input("""-----Menu-----
                    
[1] - PIX (12% de desconto)
[2] - DÉBITO (8% de desconto)
[3] - CRÉDITO (5% de juros)
[4] - DINHEIRO (15% de desconto)
                    
Escolha a forma de pagamento: """))

match payment:
    case 1:
        print('\nVocê escolheu a opção PIX\n')
        print(f'Sua compra de R${price:.2f}, ganhou o desconto de R${price * 0.12:.2f}\nO valor final ficou em R${price - (price * 0.12):.2f}')
    case 2:
        print('\nVocê escolheu a opção DÉBITO\n')
        print(f'Sua compra de R${price:.2f}, ganhou o desconto de R${price * 0.08:.2f}\nO valor final ficou em R${price - (price * 0.08):.2f}')
    case 3:
        print('\nVocê escolheu a opção CRÉDITO\n')
        print(f'Sua compra de R${price:.2f} teve um JUROS de R${price * 0.05:.2f}\nO valor final ficou em R${price + (price * 0.05):.2f}')
    case 4:
        print('\nVocê escolheu a opção DINHEIRO\n')
        print(f'Sua compra de R${price:.2f}, ganhou o desconto de R${price * 0.15:.2f}\nO valor final ficou em R${price - (price * 0.15):.2f}')
    case _:
        print('Erro: Opção inválida')

#---- OUTRA FORMA DE RESOLUÇÃO -----
desc = 0
price = float(input('Informe o valor da compra: '))
payment = int(input("""-----Menu-----
                    
[1] - PIX (12% de desconto)
[2] - DÉBITO (8% de desconto)
[3] - CRÉDITO (5% de juros)
[4] - DINHEIRO (15% de desconto)
                    
Escolha a forma de pagamento: """))

match payment:
    case 1:
        print('\nVocê escolheu a opção PIX\n')
        desc = price * 0.12
    case 2:
        print('\nVocê escolheu a opção DÉBITO\n')
        desc = price * 0.08
    case 3:
        print('\nVocê escolheu a opção CRÉDITO\n')
        desc = price * 0.05
    case 4:
        print('\nVocê escolheu a opção DINHEIRO\n')
        desc = price * 0.15
    case _:
        print('Erro: Opção inválida')

if desc != 0:
    new_price = price - desc
    print(f'Valor: R${price:.2f}')
    print(f'Valor do desconto: R${desc:.2f}')
    print(f'Valor final: R${new_price:.2f}')
else: print('Informe uma das opções acima')