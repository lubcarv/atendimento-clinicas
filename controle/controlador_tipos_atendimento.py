from __future__ import annotations
from typing import TYPE_CHECKING
from limite.tela_tipo_atendimento import TelaTipoAtendimento
from entidade.tipo_atendimento import TipoAtendimento
from exceptions.tipo_atendimento_repetido_exception import TipoAtendimentoRepetidoException
from exceptions.tipo_atendimento_inexistente_exception import TipoAtendimentoInexistenteException

if TYPE_CHECKING:
    from controle.controlador_sistema import ControladorSistema

class ControladorTiposAtendimento:
    def __init__(self, controlador_sistema: ControladorSistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_tipo_atendimento = TelaTipoAtendimento()
        self.__tipos_atendimento = []

    def pega_tipo_atendimento_por_codigo(self, codigo: str) -> TipoAtendimento | None:
        for tipo_atendimento in self.__tipos_atendimento:
            if tipo_atendimento.codigo == codigo:
                return tipo_atendimento
        return None

    def incluir_tipo_atendimento(self) -> None:
        dados_tipo_atendimento = self.__tela_tipo_atendimento.pega_dados_tipo_atendimento()
        codigo = dados_tipo_atendimento['código']
        tipo_atendimento = self.pega_tipo_atendimento_por_codigo(codigo)
        try:
            if tipo_atendimento == None:
                tipo_atendimento = TipoAtendimento(dados_tipo_atendimento['código'], dados_tipo_atendimento['nome'])
                self.__tipos_atendimento.append(tipo_atendimento)
                self.__tela_tipo_atendimento.mostra_mensagem('Tipo de atendimento incluído com sucesso!')

            else:
                raise TipoAtendimentoRepetidoException

        except TipoAtendimentoRepetidoException as e:
            self.__tela_tipo_atendimento.mostra_mensagem(e)

    def alterar_tipo_atendimento(self) -> None:
        self.lista_tipos_atendimento()
        codigo_tipo_atendimento = self.__tela_tipo_atendimento.seleciona_tipo_atendimento()
        tipo_atendimento = self.pega_tipo_atendimento_por_codigo(codigo_tipo_atendimento)
        
        try:
            if tipo_atendimento is not None:
                novos_dados_tipo_atendimento = self.__tela_tipo_atendimento.pega_dados_tipo_atendimento()
                tipo_atendimento.codigo = novos_dados_tipo_atendimento['código']
                tipo_atendimento.nome = novos_dados_tipo_atendimento['nome']
                self.__tela_tipo_atendimento.mostra_mensagem('Tipo de atendimento alterado com sucesso!')
            else:
                raise TipoAtendimentoInexistenteException

        except TipoAtendimentoInexistenteException as e:
            self.__tela_tipo_atendimento.mostra_mensagem(e)

    def lista_tipos_atendimento(self) -> None:
        for tipo_atendimento in self.__tipos_atendimento:
            self.__tela_tipo_atendimento.mostra_tipo_atendimento({'código': tipo_atendimento.codigo, 'nome': tipo_atendimento.nome})

    def excluir_tipo_atendimento(self) -> None:
        self.lista_tipos_atendimento()
        codigo_tipo_atendimento = self.__tela_tipo_atendimento.seleciona_tipo_atendimento()
        tipo_atendimento = self.pega_tipo_atendimento_por_codigo(codigo_tipo_atendimento)

        try:
            if tipo_atendimento is not None:
                self.__tipos_atendimento.remove(tipo_atendimento)
                self.__tela_tipo_atendimento.mostra_mensagem('Tipo de atendimento removido com sucesso!')
                self.lista_tipos_atendimento()
            else:
                raise TipoAtendimentoInexistenteException

        except TipoAtendimentoInexistenteException as e:
            self.__tela_tipo_atendimento.mostra_mensagem(e)

    def retornar(self) -> None:
        self.__controlador_sistema.abre_tela()

    def abre_tela(self) -> None:
        lista_opcoes = {1: self.incluir_tipo_atendimento, 2: self.alterar_tipo_atendimento, 
                        3: self.lista_tipos_atendimento, 4: self.excluir_tipo_atendimento,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_tipo_atendimento.tela_opcoes()]()

