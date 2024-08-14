class Restaurante:
    restaurantes = []
    # definindo construtor e passar os parametros
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        # colocando ja os atributos na lista
        Restaurante.restaurantes.append(self)
        
    # metodo string para exibir os valores. class especial tem sempre __rts__
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'
        
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')
        
restaurante_praca = Restaurante('Arte Doce', 'Cafe')
restaurante_pizza = Restaurante('Huila', 'Restaurante')

# exibir o metodo listar
Restaurante.listar_restaurantes()

# print(restaurante_pizza)
# print(restaurante_praca)
# print(vars(restaurante_praca))
# print(vars(restaurante_pizza))

