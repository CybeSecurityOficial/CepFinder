import os
import requests
import time

def consultar():
    os.system('clear')

    cep = input('\033[1;36mDigite o CEP pata consultar:\033[1;92m ')
    api = requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()

    if 'message' not in api:
        os.system('clear')

        print('\033[1;97mCEP: {}'.format(api['cep']))
        print('Rua: {}'.format(api['logradouro']))
        print('Complemento: {}'.format(api['complemento']))
        print('Bairro: {}'.format(api['bairro']))
        print('Cidade: {}'.format(api['localidade']))
        print('Estado UF: {}'.format(api['uf']))
        print('IBGE: {}'.format(api['ibge']))
        print('DDD: {}'.format(api['ddd']))
        print('GIA: {}\n'.format(api['gia']))

    else:
        print('\033[1;31mCEP invalido')

    opc = input('\033[1;97mDeseja consultar um novo CEP? \033[1;92ms\033[1;97m/\033[1;31mn\033[1;97m: ')

    if opc == 'S' or opc == 's':
        consultar()

    else:
        main()

def main():
    os.system('clear')
    print('''
\033[1;101m\033[1;97mBem vindo ao CepFinder\033[0;0m

\033[1;95m ██████╗███████╗██████╗ ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗
\033[1;96m██╔════╝██╔════╝██╔══██╗██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
\033[1;94m██║     █████╗  ██████╔╝█████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
\033[1;93m██║     ██╔══╝  ██╔═══╝ ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
\033[1;91m╚██████╗███████╗██║     ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
 \033[1;92m╚═════╝╚══════╝╚═╝     ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝

                              \033[1;101m\033[1;97m_Cyber Security_\033[0;0m

\033[1;96m[\033[1;95m01\033[1;96m] \033[1;95m= \033[1;96mConsultar CEP
\033[1;96m[\033[1;95m02\033[1;96m] \033[1;95m= \033[1;96mSair
''')

    es = input('\033[1;92m-->\033[1;36m ')

    if es == '1' or es == '01':

        consultar()

    elif es == '2' or es == '02':

        os.system('clear')
        print('\033[1;101m\033[1;97m_Cyber Security_\033[0;0m\n')
        exit()

    else:

        os.system('clear')
        print('\033[1;31mOpção invalida\n')
        time.sleep(2)
        main()

main()
