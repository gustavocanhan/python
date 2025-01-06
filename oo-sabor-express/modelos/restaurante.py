class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {
                  restaurante.categoria} | {restaurante.ativo}')


restaurante_praca = Restaurante('Pizzaria', 'Pizza')
restaurante_pizza = Restaurante('Pizzaria Saleta ', 'Pizza')
restaurante_mc = Restaurante(nome='Mc Donalds', categoria='FastFood')

Restaurante.listar_restaurantes()
