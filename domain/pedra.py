from domain.elemento import Elemento


class Pedra(Elemento):
    """ A Pedra ganha para a Tesoura
    Permite instanciar um elemento do tipo pedra
    """
    @property
    def elemento_confronto(self):
        """ Se repete em cada classe por conta do setter """
        return self._elemento_confronto

    @elemento_confronto.setter
    def elemento_confronto(self, elemento: Elemento):
        """ Regra de negócio para definição do estado do confronto baseado no
        elemento que foi o desafiante:
            - Verifica se o objeto passado é do tipo Elemento;
            - Importa a classe para a qual se desafiado vence (Pedra);
            - Caso seja Pedra, alera o estado do confronto para 1;
            - Se for empate ou perda permanece como está - 0;
            - Atribue qual foi o elemento que o desafiou;
        """
        if not issubclass(elemento.__class__, Elemento):
            raise ValueError(
                f"Elemento informado não é válido! -> {type(elemento)}")
        from domain.tesoura import Tesoura  # <--para contornar a ref. circular
        if isinstance(elemento, Tesoura):
            self._estado_confronto = 1
        self._elemento_confronto = elemento

    def __str__(self):
        """ A representação do elemento será de acordo com o estado do
        confronto:
            - Se tiver vencido (1) informa vitória;
            - Senão verifica se o elemento confrontado foi do mesmo tipo dele,
            caso seja informa empate;
            - Caso contrário se trata de uma derrota e informa  que perdeu.
        """
        if self._estado_confronto == 1:
            return "Pedra VENCE a Tesoura"
        else:
            if isinstance(self._elemento_confronto, Pedra):
                return "Pedra EMPATA com a Pedra"
            else:
                return "Pedra PERDE para o Papel"
