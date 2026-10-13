from limite.tela_relatorios import TelaRelatorio
from typing import TYPE_CHECKING
from collections import Counter

if TYPE_CHECKING:
    from controle.controlador_sistema import ControladorSistema
    from controle.controlador_atendimentos import ControladorAtendimentos
    from controle.controlador_procedimentos import ControladorProcedimentos

class ControladorRelatorios:
    def __init__(self, controlador_sistema: ControladorSistema, controlador_procedimentos: ControladorProcedimentos,
                controlador_atendimentos: ControladorAtendimentos):
        self.__controlador_sistema = controlador_sistema
        self.__tela_relatorio = TelaRelatorio()
        self.__procedimentos = controlador_procedimentos
        self.__controlador_atendimentos = controlador_atendimentos

    def clinica_com_mais_atendimentos(self):
        titulo, qtd_linhas = self.__tela_relatorio.pega_dados_relatorio()
        ranking = Counter(a.clinica for a in self.__controlador_atendimentos).most_common(qtd_linhas)
        linhas = [
            f'{pos}º {clinica.nome}: {qtd} atendimentos'
            for pos, (clinica, qtd) in enumerate(ranking, start=1)
        ]

        return {'titulo': titulo.strip(), 'linhas': linhas}

    def atendimentos_mais_caros_e_mais_baratos(self):
        titulo, qtd_linhas = self.__tela_relatorio.pega_dados_relatorio()

        ordenados = sorted(
            self.__controlador_atendimentos.atendimentos,
            key=lambda a: a.valor, reverse=True,
        )
        linhas = ['-- Mais caros --']
        for pos, a in enumerate(ordenados[:qtd_linhas], start=1):
            linhas.append(f'{pos}º {a.clinica.nome} - {a.procedimento.nome} - R$ {a.valor:.2f}')
            linhas.append(f'-- Mais baratos --')
            for pos, a in enumerate(reversed(ordenados[-qtd_linhas]), start=1):
                linhas.append(f'{pos}º {a.clinica.nome} - {a.procedimento.nome} - R$ {a.valor:.2f}')
        self.__tela_relatorio.mostra_relatorio(titulo, linhas)

    def procedimentos_mais_realizados(self):
        titulo, qtd_linhas = self.__tela_relatorio.pega_dados_relatorio()
        atendimentos = self.__controlador_atendimentos.atendimentos
        ranking = Counter(a.procedimento for a in atendimentos).most_common(qtd_linhas)
        linhas = [
            f'{pos}º {proc.nome}: {qtd} vezes'
            for pos, (proc, qtd) in enumerate(ranking, start=1)
        ]
        self.__tela_relatorio.mostra_relatorio(titulo, linhas)

    def procedimentos_mais_caros_e_mais_baratos(self):
        titulo, qtd_linhas = self.__tela_relatorio.pega_dados_relatorio()
        ordenados = sorted(
                    self.__co,
                    key=lambda a: a.valor, reverse=True,
                )
        linhas = ['-- Mais Caros --']
        for pos, p in enumerate(ordenados[:qtd_linhas], start=1):
            linhas.append(f'{pos}º {p.nome} - R$ {p.valor:.2f}')

        linhas.append('-- Mais Baratos --')
        for pos, p in enumerate(ordenados[-qtd_linhas:], start=1):
            linhas.append(f'{pos}º {p.nome} - R$ {p.valor:.2f}')
        self.__tela_relatorio.mostra_relatorio(titulo, linhas)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.clinica_com_mais_atendimentos,
            2: self.atendimentos_mais_caros_e_mais_baratos,
            3: self.procedimentos_mais_realizados,
            4: self.procedimentos_mais_caros_e_mais_baratos,
            0: self.retornar,
        }
        continua = True
        while continua:
            lista_opcoes[self.__tela_relatorio.tela_opcoes()]()