from domain.jogador import Jogador
from domain.elemento import Elemento
from util.pintar import Pintar as p


class JogoPedraPapelTesoura():
    """ Desenvolvimento do Jogo Pedra-Papel-Tesoura """

    def __init__(self, jogador1: Jogador, jogador2: Jogador, qtd_rodadas: int):
        """Inicia um novo jogo solicitando:
            - Dois Jogadores (1 e 2);
            - A quantidade de rodadas;
            - Cria um lista vazia para armazenar as informaçõe de cada rodada
        """
        self._jogador1 = jogador1
        self._jogador2 = jogador2
        self._qtd_rodadas = qtd_rodadas
        self._rodadas = list()

    @property
    def jogador1(self):
        return self._jogador1

    @property
    def jogador2(self):
        return self._jogador2

    @property
    def qtd_rodadas(self):
        return self._qtd_rodadas

    def jogar(self, elem_jog1: Elemento, elem_jog2: Elemento):
        """Inicia uma joganda, da seguinte forma:
            - recebe os elementos escolhidos tanto pelo jogador 1 quanto pelo
            jogador 2;
            - informa para o elemto do desafiante qual foi o elemeto do seu
            oponete e ele já irá saber se venceu ou perdeu;
            - seta a pontuação da jogada atual passando os elemntos do
            confronto para os jogadores;
            - adiciona na lista de rodadas uma tupla contendo as informações da
            rodada atual. 
        """
        elem_jog1.elemento_confronto = elem_jog2
        elem_jog2.elemento_confronto = elem_jog1
        self.jogador1.pontuacao = elem_jog1
        self.jogador2.pontuacao = elem_jog2
        # lista de tuplas com os elementos confrontados pelos jogadores e suas
        # respectivas pontuações acumuladas por rodada
        self._rodadas.append((elem_jog1, self.jogador1.pontuacao,
                              elem_jog2, self.jogador2.pontuacao))

    def vencedor(self) -> str:
        """ Retorna uma string com informações sobre o vencedor do jogo ou se
        hove empate"""
        if self.jogador1.pontuacao > self.jogador2.pontuacao:
            return p.verde(self.jogador1.nome) + " é o vencedor com " + \
                p.vermelho(str(self.jogador1.pontuacao) + " ponto(s)")
        elif self.jogador1.pontuacao < self.jogador2.pontuacao:
            return p.verde(self.jogador2.nome) + " é o vencedor com " + \
                p.vermelho(str(self.jogador2.pontuacao) + " ponto(s)")
        else:
            return "Houve empate entre " + p.amarelo(self.jogador1.nome) + \
                " e " + p.amarelo(self.jogador2.nome) + " com " + \
                p.vermelho(str(self.jogador1.pontuacao) + " ponto(s)")

    def __str__(self):
        """ A representação da Jogo é a construção do placar que se dá através
        da itração sobre as informações armazenadas na lista de rodadas
        sinalizando a situação do confronto e a pontuação acumulada em cada
        rodada por jogador """
        placar = ""
        i = 1
        for el1, pt1, _, pt2 in self._rodadas:
            placar += p.amarelo(f"Rodada {i}ª ---- \n")
            placar += f"{p.vermelho(self.jogador1.nome)}" \
                f" Pontuação => [{p.vermelho(pt1)}] >> {p.magenta(el1)} << " \
                f"{p.vermelho(self.jogador2.nome)}" \
                f" Pontuação => [{p.vermelho(pt2)}] \n"
            i += 1
        return placar
