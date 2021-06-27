import os
from art import tprint, FONT_NAMES
from util.pintar import Pintar

cores = {
    "amarelo": Pintar.YELLOW,
    "verde": Pintar.GREEN,
    "vermelho": Pintar.RED,
    "azul": Pintar.BLUE,
    "magenta": Pintar.MAGENTA,
    "negrito": Pintar.BOLD,
}


def limpar_tela():
    os.system('cls')  # se unix os.system('clear')


def texto_para_tela(texto: str, cor: str):
    """ Exibe um texto para tela de abertura nas seguintes cores possíveis:
    amarelo, verde, vermelho, azul, magenta ou negrito(destacado)
    Caso a cor informada não seja localizada, por padrão será atribuída o
    negrito(destacado)"""
    print(cores.get(cor, Pintar.BOLD), end="")
    tprint(texto, font=FONT_NAMES[558])
    print(Pintar.RESET, end="")


def constroi_tela():
    textos = [
        'Pedra-Papel-Tesoura',
        'Papel-Pedra-Tesoura',
        'Papel-Tesoura-Pedra',
        'Tesoura-Pedra-Papel',
        'Papel-Pedra-Tesoura',
    ]
    cores = [
        'verde',
        'vermelho',
        'amarelo',
        'azul',
        'negrito',
    ]
    limpar_tela()
    for i, texto in enumerate(textos):
        texto_para_tela(texto, cores[i])


def tela_abertura():
    while True:
        constroi_tela()
        continuar = input(Pintar.amarelo("Iniciar o jogo? (s/n)? "))
        if continuar.lower() in "sim":
            break


if __name__ == '__main__':
    tela_abertura()
