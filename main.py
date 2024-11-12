import os


class Colors:
    WHITE = "\033[37m"
    GREEN = "\033[32m"
    RED = "\033[31m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"


messages = {
    'welcome': f'{Colors.CYAN}-== Bem vindo ao even-or-odd! ==-',
    'first_ask': f'{Colors.WHITE}Em que número você está pensando? ',
    'second_ask': f'Digite outro número ou digite "{Colors.CYAN}sair{Colors.WHITE}" para sair: ',
    'par': f'Esse é um número {Colors.GREEN}par{Colors.WHITE}!',
    'impar': f'Esse é um número {Colors.GREEN}ímpar{Colors.WHITE}!',
    'invalid_number': 'Por favor, insira um número válido.',
    'invalid_entry': f'{Colors.RED}Entrada inválida! {Colors.WHITE}Digite um número ou "{Colors.CYAN}sair{Colors.WHITE}" para sair.',
    'exit': f'{Colors.CYAN}- Saindo do programa. Até logo!'
}


def check_number():
    clear_screen()

    print(messages['welcome'])

    while True:
        first_ask = input(messages['first_ask'])

        if first_ask.lower() in ['sair', 'close', 'exit']:
            print(messages['exit'])
            return

        try:
            first_ask = int(first_ask)
        except ValueError:
            print(messages['invalid_number'])
            continue

        if first_ask % 2 == 0:
            print(messages['par'])
        else:
            print(messages['impar'])

        while True:
            second_ask = input(messages['second_ask'])

            if second_ask.lower() in ['sair', 'close', 'exit']:
                print(messages['exit'])
                return

            try:
                second_ask = int(second_ask)
                if second_ask % 2 == 0:
                    print(messages['par'])
                else:
                    print(messages['impar'])
            except ValueError:
                print(messages['invalid_entry'])
                continue


def clear_screen():
    system = os.name
    if system == 'nt':  # windows
        os.system('cls')
    else:
        os.system('clear')


check_number()
