# Propriedade: Manuel Figueiredo
from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []
    # definindo construtor e passar os parametros
    def __init__(self, nome, categoria):
        # o _antes da variavel serve para definir este atributo como privado
        # usando o title depois do argumento, significa que vai converter as iniciais em maiusculas
        # usando o upper vai colocar todo o conteudo em maiusculas
        self._nome = nome.title() 
        self._categoria = categoria.upper()
        self._ativo = False
        # importando objectos
        self._avaliacao = []
        self._cardapio = []
        # colocando ja os atributos na lista
        Restaurante.restaurantes.append(self)
        
    # metodo string para exibir os valores. class especial tem sempre __rts__
    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self.ativo}'
    # usar o classmethod sempre que o metodo referenciado a class e nao com o objecto ou instancia
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)}| {'Status'}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}')
    # modificar como o atributo vai ser lido
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
    
    # metodo para activar o status. Definir um metodo de objeto
    def alternar_estado(self):
        self._ativo = not self._ativo

    # metodo para avaliacao
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota < 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        
    @property
    def media_avaliacao(self):
        # se o resturante n tem avaliacao, retornar 0
        if not self._avaliacao:
              return '-'
        # somar as avaliacoes
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        # pegar as quantidades das notas
        quantidade_de_notas = len(self._avaliacao)
        # achar a media das notas
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    # dicionar no cardapio
    def adicionar_cardapio(self, item):
        # adicionar o item se for uma instancia do item cardapio
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
        
    # metodo para exibir, colocamos property por ser apenas de leitura
    @property
    def exibir_cardapio(self):
        print(f'Cardapio do Restaurante {self._nome}\n')
        # enumerar os itens da lista 
        for i,item in enumerate(self._cardapio, start=1):
            # verificar o atributo se descricao e tamanho
            # o primeiro para o prato
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome.ljust(25)} | Preço:{item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else: 
                mensagem_bebida = f'{i}. Nome: {item._nome.ljust(25)} | Preço:{item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
        