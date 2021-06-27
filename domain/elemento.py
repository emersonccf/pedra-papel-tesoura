from abc import ABC, abstractmethod


class Elemento(ABC):
    """ Classe base abstrata para os elementos do jogo. Todo elemento do jogo
    que herda desta classe deve ser capaz de:
    - informar o estado de confronto com outro elemeto: 
        > Se vence recebe seu estado será igual a 1:
            self._estado_confronto = 1
        > Se perde ou empata permanece 0:
            self._estado_confronto = 0
    - é capaz de dizer qual elemento foi confrontado:
        > self._elemento_confronto
    """

    def __init__(self):
        """ Inicia um elemento com um estado padão:
                - por padão, o estado do confronto é iniciado como 0; e
                - é inicializado com um objeto do tipo None, não defindo.
        """
        self._estado_confronto = 0
        self._elemento_confronto = None

    @property
    def estado_confronto(self):
        return self._estado_confronto

    @abstractmethod
    def __str__(self):
        pass
