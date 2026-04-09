#Atividade 01:
option = int(input("""[1] - Sul\n[2] - Norte\n[3] - Leste\n[4] - Oeste\n[5][6] - Nordeste\n[7][8][9] - Sudeste
[10] - Centro-Oeste\n[11] - Noroeste\n\nInforme o Código: """))

match option:
    case 1:
        print('Sul')
    case 2:
        print('Norte')
    case 3:
        print('Leste')
    case 4:
        print('Oeste')
    case 5|6:
        print('Nordeste')
    case 7|8|9:
        print('Sudeste')
    case 10:
        print('Centro-Oeste')
    case 11:
        print('Noroeste')
    case _:
        print('Importado')

#Usando dicionário

# dict_options = {1:'Sul', 2:'Norte', 3: 'Leste', 4: 'Oeste',5:'Nordeste',6:'Nordeste',
#            7: 'Sudeste',8:'Sudeste',9:'Sudeste',10:'Centro-Oeste',11:'Noroeste'}

# options = int(input("""[1] - Sul\n[2] - Norte\n[3] - Leste\n[4] - Oeste\n[5][6] - Nordeste\n[7][8][9] - Sudeste
# [10] - Centro-Oeste\n[11] - Noroeste\n\nInforme o Código: """))

# print(dict_options.get(options, 'Importado'))