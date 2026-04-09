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

#Ex02.: 



