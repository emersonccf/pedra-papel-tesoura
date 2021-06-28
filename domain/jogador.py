from domain.elemento import Elemento


class Jogador():
    """Cria uma intância de Jogador que sabe informar seu nome e sua 
    pontuação"""

    def __init__(self, nome: str):
        self._nome = nome
        self._pontuacao = 0

    @property
    def nome(self):
        return self._nome

    @property
    def pontuacao(self):
        return self._pontuacao

    @pontuacao.setter
    def pontuacao(self, elemento: Elemento):
        """Adiciona a pontuação de acordo com o estado do elemento que o
        jogador escolheu para realizar o confronto"""
        if not issubclass(elemento.__class__, Elemento):
            raise ValueError(
                f"Elemento informado não é válido! -> {type(elemento)}")
        self._pontuacao += elemento.estado_confronto

    def __str__(self):
        return f"Nome: {self._nome} -> Pontuação {self._pontuacao}"
