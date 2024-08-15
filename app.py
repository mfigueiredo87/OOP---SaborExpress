# Propriedade: Manuel Figueiredo
# importar 
from modelos.restaurante import Restaurante

# criar restaurantes
restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_huila = Restaurante('arte doce', 'Cafe')
restaurante_sul = Restaurante('huila sul', 'comida do sul')

restaurante_praca.receber_avaliacao('Manuel',8)
restaurante_praca.receber_avaliacao('Figueiredo', 8)

restaurante_praca.alternar_estado()
def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
    