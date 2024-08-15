# importando a class item_cardapio
from modelos.cardapio.item_cardapio import ItemCardapio
# aplicando heranca
class Prato(ItemCardapio):
    # definindo o construtor
    def __init__(self, nome,preco,descricao):
        # super serve para acessar informacoes de outra class
        # aplicando instancia da class herdade
        super().__init__(nome,preco)
        self.descricao = descricao
    
    # usando o metodo string
    def __str__(self):
        return self._nome