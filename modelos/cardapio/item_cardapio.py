from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
    
    # class abstracta 
    # vai servir de modelo para que as outras classes possam implementa-la
    @abstractmethod
    def aplicar_desconto(self):
        pass
        