# Propriedade: Manuel Figueiredo
# importar 
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

# criar restaurantes
restaurante_praca = Restaurante('praca', 'Gourmet')
bebida_suco = Bebida('Suco de Menlancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_petisco = Prato('Omolete completo', 9.5, 'Omolete com direito a bebida')
prato_petisco.aplicar_desconto()

restaurante_praca.adicionar_cardapio(bebida_suco)
restaurante_praca.adicionar_cardapio(prato_petisco)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()
    