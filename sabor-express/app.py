import os

restaurantes = [
    {'nome': 'Pizzaria Saleta', 'categoria': 'Italiano', 'ativo': False},
    {'nome': 'SushiBar', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Mc Donalds', 'categoria': 'Fast-Food', 'ativo': True}
]


def exibir_nome_do_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')


def opcao_invalida():
    exibir_subtitulo('Opção Inválida!')
    voltar_menu_principal()


def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante

        INPUTS
        - Nome do restaurante
        - Categoria

        OUTPUTS
        - Adicionar um novo restaurante à lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input(
        'Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {
                      nome_do_restaurante}: ')

    dados_do_restaurante = {'nome': nome_do_restaurante,
                            'categoria': categoria, 'ativo': False}

    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_menu_principal()


def listar_restaurantes():
    ''' Essa função é para listar todos os restaurantes que estão cadastrado '''
    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Restaurante'.ljust(20)} || {'Categoria'.ljust(20)} || Estado')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'{nome_restaurante.ljust(20)} || {
              categoria.ljust(20)} || {ativo.ljust(20)}')

    voltar_menu_principal()


def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')

    nome_restaurante = input(
        'Digite o nome do restaurante que deseja alterar o estado: ')

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurente {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {
                nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')

    voltar_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def finalizar_app():
    limpar_tela()
    exibir_subtitulo('Finalizando o app')


def main():
    limpar_tela()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


def limpar_tela():
    os.system('cls')


def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()


def exibir_subtitulo(texto):
    limpar_tela()
    return print(texto, '\n')


if __name__ == '__main__':
    main()
