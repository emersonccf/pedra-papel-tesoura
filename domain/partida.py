import random

from domain.elemento import Elemento
from domain.pedra import Pedra
from domain.papel import Papel
from domain.tesoura import Tesoura
from domain.jogo import JogoPedraPapelTesoura
from domain.jogador import Jogador
from util.pintar import Pintar as p
from util.tela_abertura import tela_abertura, limpar_tela, texto_para_tela


class Main():
    # Lista de opções de cores, atributo de classe
    cores = ['verde', 'vermelho', 'amarelo', 'azul', 'negrito', ]

    @staticmethod
    def informar_valor_inteiro(mensagem: str) -> int:
        """ Retorna um número inteiro já validado """
        while True:
            try:
                num_inteiro = int(input(mensagem + ": "))
                break
            except ValueError as e:
                print(p.vermelho("Valor informado não é um número inteiro!"),
                      e)
        return num_inteiro

    def verica_intervalo(self, inicio: int, fim: int, mensagem: str) -> int:
        """ Verifica se um determinado valor entá dentro de um intervalo entre
        o incio e o fim informados"""
        opcao = self.informar_valor_inteiro(mensagem)
        while True:
            if opcao not in range(inicio, fim + 1):
                # ou poderia ser if not inicio >= opcao >= fim:
                opcao = self.informar_valor_inteiro(
                    p.vermelho("Opção Inválida! ") + mensagem)
                continue  # para vericar se o novo valor atende as condições
            else:
                break
        return opcao

    def prepara_jogo(self) -> JogoPedraPapelTesoura:
        """ Prepara o ambiente para a realização do jogo:
            - Intancia os jogadores 1 e 2;
            - Define a quantidade de rodadas;
            - E por fim instancia e retorna o ambiente de jogo
            Pedra-Papel-Tesoura
        """
        limpar_tela()
        print("Iniciando Jogo:")
        texto_para_tela("Pedra-Papel-Tesoura", random.choice(self.cores))
        # TODO: Nome de jogador em branco trarar
        jogador1 = Jogador(input("Informe nome do Jogador 1: "))
        jogador2 = Jogador(input("Informe nome do Jogador 2: "))
        qtd_rodadas = self.verica_intervalo(1, 10,
                                            "Informe a quantidade de rodadas"
                                            "entre 1 a 10")
        return JogoPedraPapelTesoura(jogador1, jogador2, qtd_rodadas)

    def menu_op_elementos(self, nm_jogador: str) -> Elemento:
        """ Gera o menu de opções para que o Jogador faça sua escolha """
        print(f"{p.amarelo(nm_jogador)}, faça sua escolha:")
        print(p.MAGENTA, end="")
        print("1- Pedra")
        print("2- Tesoura")
        print("3- Papel")
        print(p.RESET, end="")
        op = self.verica_intervalo(1, 3, f"Informe sua opção {nm_jogador}")
        if op == 1:
            return Pedra()
        elif op == 2:
            return Tesoura()
        elif op == 3:
            return Papel()

    def run(self):
        """ Executa o jogo:
            - Cria um ambiente de jogo (jogadores e rodadas);
            - Cria o elemento desafiante de cada jogador;
            - Executa o jogo;
            - Exibe o placar parcial do jogo;
            - Por fim informa o vencedor;
            - Verifica se os participantes desejam continuar jogando.
        """
        while True:
            tela_abertura()
            jogo = self.prepara_jogo()
            rodada = 0
            continuar = "n"
            while jogo.qtd_rodadas > rodada:
                elem_jog1 = self.menu_op_elementos(jogo.jogador1.nome)
                elem_jog2 = self.menu_op_elementos(jogo.jogador2.nome)
                jogo.jogar(elem_jog1, elem_jog2)
                print(jogo)
                rodada += 1
            print(jogo.vencedor())
            continuar = input(p.amarelo("Deseja continuar jogando (s/n) ? "))
            if continuar.lower() in "naonão":
                break


if __name__ == '__main__':
    Main().run()
