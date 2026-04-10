#Atividade 02:
n = int(input('Informe um número inteiro: '))

match n:
    case i if 0 > n:
        print(f'{n} é um número negativo')
    case i if 0 <= n:
        print(f'{n}é um número positivo')