def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


inteiro = leiaInt('Digite um Inteiro: ')
real = leiaFloat('Digite um real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
