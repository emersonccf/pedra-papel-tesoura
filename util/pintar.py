class Pintar():
    YELLOW = "\033[1;33m"  # empata
    GREEN = "\033[0;32m"  # ganha
    RED = "\033[1;31m"  # perde
    BLUE = "\033[1;34m"
    MAGENTA = "\033[1;35m"
    RESET = "\033[0;0m"
    BOLD = "\033[;1m"
    REVERSE = "\033[;7m"

    @classmethod
    def amarelo(cls, texto: str) -> str:
        """ Pinta o texto de amarelo e devolve uma string """
        return f'{cls.YELLOW}{texto}{cls.RESET}'

    @classmethod
    def verde(cls, texto: str) -> str:
        """ Pinta o texto de verde e devolve uma string """
        return f'{cls.GREEN}{texto}{cls.RESET}'

    @classmethod
    def vermelho(cls, texto: str) -> str:
        """ Pinta o texto de vermelho e devolve uma string """
        return f'{cls.RED}{texto}{cls.RESET}'

    @classmethod
    def azul(cls, texto: str) -> str:
        """ Pinta o texto de azul e devolve uma string """
        return f'{cls.BLUE}{texto}{cls.RESET}'

    @classmethod
    def magenta(cls, texto: str) -> str:
        """ Pinta o texto de magenta e devolve uma string """
        return f'{cls.MAGENTA}{texto}{cls.RESET}'

    @classmethod
    def negrito(cls, texto: str) -> str:
        """ Pinta o texto de magenta e devolve uma string """
        return f'{cls.BOLD}{texto}{cls.RESET}'


if __name__ == "__main__":
    print(Pintar.vermelho('Atenção:'), Pintar.amarelo('você cometeu um erro!'))
    print(Pintar.verde('Atenção:'), Pintar.azul('você cometeu um erro!'))
    print(Pintar.vermelho('Atenção:'), Pintar.magenta('você cometeu um erro!'))
    print(Pintar.GREEN, end="")
    print("Printa este texto com a cor definida no print acima, reseta no "
          "print de abaixo")
    print(Pintar.RESET, end="")
