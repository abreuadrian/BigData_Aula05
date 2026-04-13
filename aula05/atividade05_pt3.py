#Atividade03:
price = float(input('Informe o falor da compra: R$'))
formas_pagamento = {
    1: {'nome': 'DINHEIRO', 'desc': 0.10, 'tax': 0},
    2: {'nome': 'PIX', 'desc': 0, 'tax': 0},
    3: {'nome': 'DÉBITO', 'desc': 0, 'tax': 0.05},
    4: {'nome': 'CRÉDITO', 'desc': 0, 'tax': 0.08},
    5: {'nome': 'CHEQUE', 'desc': 0, 'tax': 0.12}
}
print("\n----- Menu -----")
for i, c in formas_pagamento.items():
    print(f"[{i}] - {c['nome']}")

opt = int(input("\nEscolha sua forma de pagamento: "))
if opt in formas_pagamento.keys():
    print(f"\nVocê escolheu pagamento via: {formas_pagamento[opt]['nome']}")
    match opt:
        case 1:
            desc = price * formas_pagamento[opt]['desc']
            new_price = price - desc
            print(f"""Valor da compra: R${price}
    Valor do desconto: R${desc}
    Valor final: R${new_price}""")
        case 2:
            print(f'Valor da compra: R${price}')
            pass
        case 3 | 4 | 5:
            tax = price * formas_pagamento[opt]['tax']
            new_price = price + tax
            print(f"""Valor da compra: R${price}
    Valor do juros: R${tax}
    Valor final: R${new_price}""")
else:
    print('Opção inválida')
    
# price = float(input('\nInforme o valor da compra: R$'))
# desc = 0
# tax = 0
# opt_pay = int(input("""\n----- Menu -----

# [1] - Dinheiro
# [2] - Pix
# [3] - Débito
# [4] - Crédito
# [5] - Cheque

# Escolha sua forma de pagamento: """))

# match opt_pay:
#     case 1:
#         desc = price * 0.10
#         print('\nVocê escolheu pagamento via: DINHEIRO')
#     case 2:
#         print(f'\nVocê escolheu pagamento via: PIX.\nValor da compra: R${price:.2f}')
#     case 3:
#         tax = price * 0.05
#         print('\nVocê escolheu pagamento via: DÉBITO')
#     case 4:
#         tax = price * 0.08
#         print('\nVocê escolheu pagamento via: CRÉDITO')
#     case 5:
#         tax = price * 0.12
#         print('\nVocê escolheu pagamento via: CHEQUE')
#     case _:
#         print('Erro: Opção Inválida.')

# if desc != 0:
#     new_price = price - desc
#     print(f"""\nValor da compra: R${price:.2f}
# Valor do desconto: R${desc:.2f}
# Valor Final: R${new_price:.2f}""")
# elif tax != 0:
#     new_price = price + tax
#     print(f"""\nValor da compra: R${price:.2f}
# Valor do juros: R${tax:.2f}
# Valor Final: R${new_price:.2f}""")

#Outra forma:
