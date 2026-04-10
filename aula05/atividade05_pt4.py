#Atividade04
nota1 = float(input('Informe a nota da 1ª avaliação: '))
nota2 = float(input('Informe a nota da 2ª avaliação: '))
nota_sec_try = 0

second_try = input('\nO estudante realizou a avaliação substitutiva? (S/N): ').lower().strip()
match second_try:
    case 's':
        nota_sec_try = float(input('Informe a nota da avaliação substituitiva: '))
    case 'n':
        nota_sec_try = -1

if nota_sec_try > min(nota1, nota2):
    if nota1 < nota2:
        nota1 = nota_sec_try
    else:
        nota2 = nota_sec_try

med = (nota1 + nota2) / 2

if med >= 6:
    print(f'\nAprovado!\nMédia final: {med}')
elif med >=3: 
    print(f'\nEm recuperação.\nMédia final: {med}')
else: print(f'\nReprovado.\nMédia final: {med}')