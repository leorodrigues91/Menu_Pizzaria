from subprocess import call
from colorama import init, Fore

init(autoreset=True)

# Pizzas
sabores = {21: 'Napolitana', 22: 'Margherita', 23: 'Calabresa', 24: 'Toscana', 25: 'Portuguesa', 26: 'Quatro Queijos', 27: 'Frango com Catupiry', 28:'Siciliana'}

pizza_media_precos = {21: 25.0, 22: 25.0, 23: 20.0, 24: 30.0, 25: 30.0, 26: 20.0, 27: 25.0, 28: 30.0}

pizza_grande_precos = {}
for key, value in pizza_media_precos.items():
    pizza_grande_precos[key] = float(value) * 1.3

#print(pizza_grande_precos)

valor_total = 0 #valor que será somado, caso o cliente queira mais de um produto

# Cabeçalho que será impresso ao iniciar o cógigo
def cabecalho():
    print(Fore.YELLOW + f'{"-=" * 30}')
    print(Fore.GREEN + f'{"PIZZARIA PYTHONISTA":^60}')
    print(Fore.YELLOW + f'{"-=" * 30}')
    print(Fore.GREEN + f'{"FAÇA SEU PEDIDO":^60}')

# Rodapé que será impresso ao finalizar do código
def rodape():
    print(Fore.YELLOW + f'{"-=" * 30}')
    print(Fore.GREEN + f'{"AGRADECEMOS A PREFERÊNCIA!":^60}')
    print(Fore.GREEN + f'{"ATÉ LOGO E VOLTE SEMPRE!":^60}')
    print(Fore.YELLOW + f'{"-=" * 30}')
    

# Começando o programa
cabecalho()

# Menu
while True:
    input_menu = int(input(Fore.GREEN + '\nMENU DE OPÇÕES:\n1 - Pizzas médias\n2 - Pizzas grandes\n3 - Sair\n\nDigite a opção desejada: '))

    if input_menu == 1:
        print(Fore.GREEN + f'\nVocê escolheu o tamanho MÉDIO.')
        while True:
            print(Fore.GREEN + f'\nEscolha o sabor da pizza:\n')
            for key, value in sabores.items():
                print(Fore.GREEN + f'{key} - {value}')
            input_pizza = int(input(Fore.GREEN + '\nDigite o código do sabor escolhido: '))
            if input_pizza in sabores:
                print(Fore.GREEN + f'\nPizza {sabores[input_pizza]} selecionada!')
                valor_total += pizza_media_precos[input_pizza]
            else:
                print(Fore.RED + f'\nCódigo inválido!\n')
                continue
            input_opcao = str(input(Fore.GREEN + '\nDeseja mais alguma coisa? [S/N] '))
            if input_opcao not in "SsNn":
                print(Fore.RED + f'\nERRO! UTILIZE APENAS "S" OU "N".')
                continue
            if input_opcao in "Ss":
                input_opcao2 = str(input(Fore.GREEN + '\nDeseja alterar o tamanho da pizza? [S/N] '))
                if input_opcao2 not in "SsNn":
                    print(Fore.RED + f'\nERRO! UTILIZE APENAS "S" OU "N".')
                    continue
                if input_opcao2 in 'Nn':
                    continue
                if input_opcao2 in 'Ss':
                    break
            if input_opcao in "Nn":
                break
        break

    elif input_menu == 2:
        print(Fore.GREEN + f'\nVocê escolheu o tamanho GRANDE.')
        while True:
            print(Fore.GREEN + f'\nEscolha o sabor da pizza:\n')
            for key, value in sabores.items():
                print(Fore.GREEN + f'{key} - {value}')
            input_pizza = int(input(Fore.GREEN + '\nDigite o código do sabor escolhido: '))
            if input_pizza in sabores:
                print(Fore.GREEN + f'\nPizza {sabores[input_pizza]} selecionada!')
                valor_total += pizza_grande_precos[input_pizza]
            else:
                print(Fore.RED + f'\nCódigo inválido!\n')
                continue
            input_opcao = str(input(Fore.GREEN + '\nDeseja mais alguma coisa? [S/N] '))
            if input_opcao not in "SsNn":
                print(Fore.RED + f'\nERRO! UTILIZE APENAS "S" OU "N".')
                continue
            if input_opcao in "Ss":
                input_opcao2 = str(input(Fore.GREEN + '\nDeseja alterar o tamanho da pizza? [S/N] '))
                if input_opcao2 not in "SsNn":
                    print(Fore.RED + f'\nERRO! UTILIZE APENAS "S" OU "N".')
                    continue
                if input_opcao2 in 'Nn':
                    continue
                if input_opcao2 in 'Ss':
                    break
            if input_opcao in "Nn":
                break
        break

    elif input_menu == 3:
        break
    
    else:
        print(Fore.RED + f'\nCódigo inválido!\n')
        continue

print(Fore.GREEN + f'\nO valor total do seu pedido é: ' + Fore.BLUE + f'R$ {valor_total:.2f}\n')

rodape()