from __future__ import annotations
from typing import TYPE_CHECKING
from limite.tela_relatorios import TelaRelatorio
from collections import Counter

if TYPE_CHECKING:
    from controle.controlador_sistema import ControladorSistema
    from controle.controlador_atendimentos import ControladorAtendimentos
    from entidade.atendimento import Atendimento

class ControladorRelatorios:
    def __init__(self, controlador_sistema: ControladorSistema, controlador_atendimentos: ControladorAtendimentos) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__tela_relatorio = TelaRelatorio()
        self.__controlador_atendimentos = controlador_atendimentos

    def clinica_com_mais_atendimentos(self) -> None:
        titulo, qtd_linhas = self.__tela_relatorio.pega_dados_relatorio()
        atendimentos = self.__controlador_atendimentos.atendimentos
        ranking = Counter(a.clinica for a in atendimentos).most_common(qtd_linhas)
        linhas = [
            f'{pos}º {clinica.nome}: {qtd} atendimentos'
            for pos, (clinica, qtd) in enumerate(ranking, start=1)
        ]

        self.__tela_relatorio.mostra_relatorio(titulo, linhas)

    def atendimentos_mais_caros_e_mais_baratos(self) -> None:
        titulo, qtd_linhas = self.__tela_relatorio.pega_dados_relatorio()

        ordenados = sorted(
            self.__controlador_atendimentos.atendimentos,
            key=lambda a: a.valor_total(), reverse=True,
        )

        def formatar(atendimento: Atendimento):
            nomes = ', '.join(p.descricao for p in atendimento.procedimentos)
            return f'{atendimento.clinica.nome} - {nomes} - R$ {atendimento.valor_total():.2f}'

        linhas = ['-- Mais caros --']
        for pos, a in enumerate(ordenados[:qtd_linhas], start=1):
            linhas.append(f'{pos}º {formatar(a)}')
            
        linhas.append(f'-- Mais baratos --')
        for pos, a in enumerate(reversed(ordenados[-qtd_linhas:]), start=1):
            linhas.append(f'{pos}º {formatar(a)}')

        self.__tela_relatorio.mostra_relatorio(titulo, linhas)

    def procedimentos_mais_realizados(self) -> None:
        titulo, qtd_linhas = self.__tela_relatorio.pega_dados_relatorio()
        atendimentos = self.__controlador_atendimentos.atendimentos
        ranking = Counter(p for a in atendimentos for p in a.procedimentos).most_common(qtd_linhas)
        linhas = [
            f'{pos}º {proc.descricao}: {qtd} vezes'
            for pos, (proc, qtd) in enumerate(ranking, start=1)
        ]
        self.__tela_relatorio.mostra_relatorio(titulo, linhas)

    def procedimentos_mais_caros_e_mais_baratos(self) -> None:
        titulo, qtd_linhas = self.__tela_relatorio.pega_dados_relatorio()

        procedimentos = list({
            p for a in self.__controlador_atendimentos.atendimentos
            for p in a.procedimentos
        })
        
        ordenados = sorted(
                    procedimentos,
                    key=lambda p: p.custo, reverse=True,
                )
        
        linhas = ['-- Mais Caros --']
        for pos, p in enumerate(ordenados[:qtd_linhas], start=1):
            linhas.append(f'{pos}º {p.descricao} - R$ {p.custo:.2f}')

        linhas.append('-- Mais Baratos --')
        for pos, p in enumerate(reversed(ordenados[-qtd_linhas:]), start=1):
            linhas.append(f'{pos}º {p.descricao} - R$ {p.custo:.2f}')
        
        self.__tela_relatorio.mostra_relatorio(titulo, linhas)

    def retornar(self) -> None:
        self.__controlador_sistema.abre_tela()

    def abre_tela(self) -> None:
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