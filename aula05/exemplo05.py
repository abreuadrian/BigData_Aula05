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
