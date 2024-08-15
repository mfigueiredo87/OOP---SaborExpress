# Propriedade: Manuel Figueiredo
# importar 
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

# criar restaurantes
restaurante_praca = Restaurante('praca', 'Gourmet')
bebida_suco = Bebida('Suco de Menlancia', 5.0, 'grande')
prato_petisco = Prato('Omolete completo', 9.5, 'Omolete com direito a bebida')


def main():
    print(bebida_suco)
    print(prato_petisco)

if __name__ == '__main__':
    main()
    