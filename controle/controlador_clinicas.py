from __future__ import annotations
from typing import TYPE_CHECKING
from limite.tela_clinica import TelaClinica
from entidade.clinica import Clinica
from exceptions.clinica_repetida_exception import ClinicaRepetidaException
from exceptions.clinica_inexistente_exception import ClinicaInexistenteException
from exceptions.profissional_inexistente_exception import ProfissionalInexistenteException
from exceptions.profissional_nao_vinculado_exception import ProfissionalNaoVinculadoException

if TYPE_CHECKING:
    from controlador_sistema import ControladorSistema
    from controlador_profissionais import ControladorProfissionais

class ControladorClinicas:
    def __init__(self, controlador_sistema: ControladorSistema, controlador_profissionais: ControladorProfissionais):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_profissionais = controlador_profissionais
        self.__tela_clinica = TelaClinica()
        self.__clinicas = []

    def pega_clinica_por_codigo(self, codigo: str) -> Clinica:
        for clinica in self.__clinicas:
            if clinica.codigo == codigo:
                return clinica
        return None

    def incluir_clinica(self) -> None:
        dados_clinica = self.__tela_clinica.pega_dados_clinica()
        codigo = dados_clinica['código']
        clinica = self.pega_clinica_por_codigo(codigo)
        try:
            if clinica == None:
                clinica = Clinica(dados_clinica['código'], dados_clinica['nome'],
                                  dados_clinica['localização'], dados_clinica['descrição'],
                                  dados_clinica['horário_abertura'], dados_clinica['horário_fechamento'])
                self.__clinicas.append(clinica)
            else:
                raise ClinicaRepetidaException(codigo)
        except ClinicaRepetidaException as e:
            self.__tela_clinica.mostra_mensagem(e)

    def alterar_clinica(self) -> None:
        self.lista_clinicas()
        codigo_clinica = self.__tela_clinica.seleciona_clinica()
        clinica = self.pega_clinica_por_codigo(codigo_clinica)
        try:
            if clinica is not None:
                novos_dados_clinica = self.__tela_clinica.pega_dados_clinica()
                abertura = novos_dados_clinica['horário_abertura']
                fechamento = novos_dados_clinica['horário_fechamento']

                if abertura >= fechamento:
                    raise ValueError('O horário de abertura precisa ser menor que o horário de fechamento')

                clinica.nome = novos_dados_clinica['nome']
                clinica.codigo = novos_dados_clinica['código']
                clinica.descricao = novos_dados_clinica['descrição']

                if abertura >= clinica.horario_fechamento:
                    clinica.horario_fechamento = fechamento
                    clinica.horario_abertura = abertura
                else:
                    clinica.horario_abertura = abertura
                    clinica.horario_fechamento = fechamento

            else:
                raise ClinicaInexistenteException(codigo_clinica)

        except ClinicaInexistenteException as e:
            self.__tela_clinica.mostra_mensagem(e)

    def lista_clinicas(self) -> None:
        if len(self.__clinicas) == 0:
            print('A lista de clínicas está vazia')
        else:
            for clinica in self.__clinicas:
                self.__tela_clinica.mostra_clinica({'nome': clinica.nome, 'código': clinica.codigo, 'localização': clinica.localizacao, 
                                                    'descrição': clinica.descricao, 'horário_abertura': clinica.horario_abertura,
                                                    'horário_fechamento': clinica.horario_fechamento, 'profissionais': clinica.profissionais})

    def excluir_clinica(self):
        self.lista_clinicas()
        codigo_clinica = self.__tela_clinica.seleciona_clinica()
        clinica = self.pega_clinica_por_codigo(codigo_clinica)
        try:
            if clinica is not None:
                self.__clinicas.remove(clinica)
                self.lista_clinicas()
                self.__tela_clinica.mostra_mensagem('Clinica removida com sucesso!')
            else:
                raise ClinicaInexistenteException(codigo_clinica)

        except ClinicaInexistenteException as e:
            self.__tela_clinica.mostra_mensagem(e)

    def vincular_profissional(self):
        self.lista_clinicas()
        codigo_clinica = self.__tela_clinica.seleciona_clinica()
        clinica = self.pega_clinica_por_codigo(codigo_clinica)
        try:
            if clinica is not None:
                cpf = self.__tela_clinica.seleciona_profissional()
                profissional = self.__controlador_profissionais.pega_profissional_por_cpf(cpf)
                if profissional is not None:
                    clinica.incluir_profissional(profissional)
                    self.__tela_clinica.mostra_mensagem('Profissional vinculado com sucesso!')
                else:
                    raise ProfissionalInexistenteException(cpf)
            else:
                raise ClinicaInexistenteException(codigo_clinica)
        except (ClinicaInexistenteException, ProfissionalInexistenteException, TypeError, ValueError) as e:
            self.__tela_clinica.mostra_mensagem(e)

    def desvincular_profissional(self):
            self.lista_clinicas()
            codigo_clinica = self.__tela_clinica.seleciona_clinica()
            clinica = self.pega_clinica_por_codigo(codigo_clinica)
            try:
                if clinica is not None:
                    cpf = self.__tela_clinica.seleciona_profissional()
                    profissional = self.__controlador_profissionais.pega_profissional_por_cpf(cpf)
                    if profissional is not None:
                        if profissional in clinica:
                            clinica.excluir_profissional(profissional)
                            self.__tela_clinica.mostra_mensagem('Profissional desvinculado com sucesso!')
                        else:
                            raise ProfissionalNaoVinculadoException(profissional.nome, clinica.nome)
                    else:
                        raise ProfissionalInexistenteException(cpf)
                else:
                    raise ClinicaInexistenteException(codigo_clinica)
            except (ClinicaInexistenteException, ProfissionalInexistenteException, TypeError, ValueError) as e:
                self.__tela_clinica.mostra_mensagem(e)
    

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_clinica, 2: self.alterar_clinica, 3: self.lista_clinicas, 4: self.excluir_clinica, 5: self.vincular_profissional, 6: self.desvincular_profissional,  0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_clinica.tela_opcoes()]()
    
            