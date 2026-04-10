#Atividade04
list_notes = []

for i in range(2):
    note = float(input(f'Informe a nota da {i+1}ª avaliação: '))
    list_notes.append(note)

second_try = input('\nO estudante realizou a avaliação substituitiva? (s/n): ').lower().strip()
match second_try:
    case 's':
        sec_try_nota = float(input('Informe a nota da avaliação substitutiva: '))
        if sec_try_nota > min(list_notes[0], list_notes[1]):
            if list_notes[0] < list_notes[1]:
                list_notes[0] = sec_try_nota
            else: list_notes[1] = sec_try_nota
    case 'n':
        sec_try_nota = -1
        pass

med = (list_notes[0] + list_notes[1]) / 2
if med >= 6:
    print(f'\nAprovado!\nMédia final: {med}')
elif med >=3: 
    print(f'\nEm recuperação.\nMédia final: {med}')
else: print(f'\nReprovado.\nMédia final: {med}')

# nota1 = float(input('Informe a nota da 1ª avaliação: '))
# nota2 = float(input('Informe a nota da 2ª avaliação: '))
# nota_sec_try = 0

# second_try = input('\nO estudante realizou a avaliação substitutiva? (S/N): ').lower().strip()
# match second_try:
#     case 's':
#         nota_sec_try = float(input('Informe a nota da avaliação substituitiva: '))
#     case 'n':
#         nota_sec_try = -1

# if nota_sec_try > min(nota1, nota2):
#     if nota1 < nota2:
#         nota1 = nota_sec_try
#     else:
#         nota2 = nota_sec_try

# med = (nota1 + nota2) / 2

# if med >= 6:
#     print(f'\nAprovado!\nMédia final: {med}')
# elif med >=3: 
#     print(f'\nEm recuperação.\nMédia final: {med}')
# else: print(f'\nReprovado.\nMédia final: {med}')