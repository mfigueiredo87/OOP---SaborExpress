from modelos.cardapio.item_cardapio import ItemCardapio
class Bebida(ItemCardapio):
    # definindo o construtor
    def __init__(self,nome,preco,tamanho):
        super().__init__(nome,preco)
        self.tamanho = tamanho
    
    # usando o metodo string
    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)