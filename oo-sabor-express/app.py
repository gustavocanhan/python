from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praca', 'Gourmet')
# restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
# restaurante_japones = Restaurante('Japa', 'Japonesa')

# restaurante_mexicano.alternar_estado()

# restaurante_praca.receber_avaliacao('Gustavo', 5)
# restaurante_praca.receber_avaliacao('André', 10)
# restaurante_praca.receber_avaliacao('Gabriel', 7)
# restaurante_praca.receber_avaliacao('Desconhecido', 1)

bebida = Bebida('Coca-Cola', 12.00, '2 Litros')
prato = Prato('Lasanha', 25.00, 'Lasanha de microondas')

bebida.aplicar_desconto()
prato.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida)
restaurante_praca.adicionar_no_cardapio(prato)


def main():
    # Restaurante.listar_restaurantes()
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()
