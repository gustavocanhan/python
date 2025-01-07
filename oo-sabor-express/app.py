from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_mexicano.alternar_estado()

restaurante_praca.receber_avaliacao('Gustavo', 5)
restaurante_praca.receber_avaliacao('André', 10)
restaurante_praca.receber_avaliacao('Gabriel', 7)
restaurante_praca.receber_avaliacao('Desconhecido', 1)


def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
