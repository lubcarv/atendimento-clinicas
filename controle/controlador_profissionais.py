from __future__ import annotations
from typing import TYPE_CHECKING
from limite.tela_profissional import TelaProfissional
from entidade.profissional import Profissional
from exceptions.profissional_repetido_exception import ProfissionalRepetidoException
from exceptions.profissional_inexistente_exception import ProfissionalInexistenteException

if TYPE_CHECKING:
    from controle.controlador_sistema import ControladorSistema

class ControladorProfissionais:
    def __init__(self, controlador_sistema: ControladorSistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_profissional = TelaProfissional()
        self.__profissionais = []

    def pega_profissional_por_cpf(self, cpf: str) -> Profissional | None:
        for profissional in self.__profissionais:
            if profissional.cpf == cpf:
                return profissional
        return None

    def incluir_profissional(self) -> None:
        dados_profissional = self.__tela_profissional.pega_dados_profissional()
        cpf = dados_profissional['cpf']
        profissional = self.pega_profissional_por_cpf(cpf)
        try:
            if profissional == None:
                profissional = Profissional(dados_profissional['nome'], dados_profissional['celular'],
                                            dados_profissional['cpf'], dados_profissional['data_nascimento'],
                                            dados_profissional['especialidade'], dados_profissional['registro_profissional'])
                self.__profissionais.append(profissional)
                self.__tela_profissional.mostra_mensagem('Profissional incluído com sucesso!')
            else:
                raise ProfissionalRepetidoException(cpf)

        except ProfissionalRepetidoException as e:
            self.__tela_profissional.mostra_mensagem(e)

    def alterar_profissional(self) -> None:
        self.lista_profissionais()
        cpf_profissional = self.__tela_profissional.seleciona_profissional()
        profissional = self.pega_profissional_por_cpf(cpf_profissional)

        try:
            if profissional is not None:
                novos_dados_profissional = self.__tela_profissional.pega_dados_profissional()
                profissional.nome = novos_dados_profissional['nome']
                profissional.celular = novos_dados_profissional['celular']
                profissional.cpf = novos_dados_profissional['cpf']
                profissional.data_nascimento = novos_dados_profissional['data_nascimento']
                profissional.especialidade = novos_dados_profissional['especialidade']
                profissional.registro_profissional = novos_dados_profissional['registro_profissional']
                self.__tela_profissional.mostra_mensagem('Profissional alterado com sucesso!')
                self.lista_profissionais()
            else:
                raise ProfissionalInexistenteException(cpf_profissional)

        except ProfissionalInexistenteException as e:
            self.__tela_profissional.mostra_mensagem(e)

    def lista_profissionais(self) -> None:
        for profissional in self.__profissionais:
            self.__tela_profissional.mostra_profissional({'nome': profissional.nome, 'celular': profissional.celular,
                                                          'cpf': profissional.cpf, 'data_nascimento': profissional.data_nascimento,
                                                          'especialidade': profissional.especialidade, 'registro_profissional': profissional.registro_profissional})

    def excluir_profissional(self) -> None:
        self.lista_profissionais()
        cpf_profissional = self.__tela_profissional.seleciona_profissional()
        profissional = self.pega_profissional_por_cpf(cpf_profissional)

        try:
            if profissional is not None:
                self.__profissionais.remove(profissional)
                self.__tela_profissional.mostra_mensagem('Profissional excluído com sucesso!')
                self.lista_profissionais()
            else:
                raise ProfissionalInexistenteException(cpf_profissional)

        except ProfissionalInexistenteException as e:
            self.__tela_profissional.mostra_mensagem(e)

    def seleciona_profissional(self) -> Profissional | None:
        self.lista_profissionais()
        identificador = self.__tela_profissional.seleciona_profissional()   # o método que a tela dele já tem
        return self.pega_profissional_por_cpf(identificador)

    def retornar(self) -> None:
        self.__controlador_sistema.abre_tela()

    def abre_tela(self) -> None:
        lista_opcoes = {1: self.incluir_profissional, 2: self.alterar_profissional, 3: self.lista_profissionais, 4: self.excluir_profissional, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_profissional.tela_opcoes()]()