from limite.tela_sistema import TelaSistema
from controle.controlador_pacientes import ControladorPacientes
from controle.controlador_profissionais import ControladorProfissionais
from controle.controlador_clinicas import ControladorClinicas
from controle.controlador_tipos_atendimento import ControladorTiposAtendimento
from controle.controlador_atendimentos import ControladorAtendimentos
from controle.controlador_pagamentos import ControladorPagamentos
from controle.controlador_procedimentos import ControladorProcedimentos
from controle.controlador_relatorios import ControladorRelatorios

class ControladorSistema:
    def __init__(self):
        self.__controlador_pacientes = ControladorPacientes(self)
        self.__controlador_profissionais = ControladorProfissionais(self)
        self.__controlador_clinica = ControladorClinicas(self, self.__controlador_profissionais)
        self.__controlador_tipos_atendimento = ControladorTiposAtendimento(self)
        self.__controlador_atendimentos = ControladorAtendimentos(self)
        self.__controlador_procedimentos = ControladorProcedimentos(self)
        self.__controlador_pagamentos = ControladorPagamentos(self)
        self.__controlador_relatorios = ControladorRelatorios(self, self.__controlador_atendimentos)
        self.__tela_sistema = TelaSistema()

    def controlador_pacientes(self) -> ControladorPacientes:
        return self.__controlador_pacientes

    def controlador_profissionais(self) -> ControladorProfissionais:
        return self.__controlador_profissionais

    def controlador_clinica(self) -> ControladorClinicas:
        return self.__controlador_clinica

    def controlador_tipos_atendimento(self) -> ControladorTiposAtendimento:
        return self.__controlador_tipos_atendimento

    def controlador_atendimentos(self) -> ControladorAtendimentos:
        return self.__controlador_atendimentos

    def controlador_procedimentos(self) -> ControladorProcedimentos:
        return self.__controlador_procedimentos

    def controlador_pagamentos(self) -> ControladorPagamentos:
        return self.__controlador_pagamentos

    def controlador_relatorios(self) -> ControladorRelatorios:
        return self.__controlador_relatorios

    def inicializa_sistema(self) -> None:
        self.abre_tela()

    def cadastra_pacientes(self) -> None:
        self.__controlador_pacientes.abre_tela()

    def cadastra_profissionais(self) -> None:
        self.__controlador_profissionais.abre_tela()

    def cadastra_clinica(self) -> None:
        self.__controlador_clinica.abre_tela()

    def cadastra_tipos_atendimento(self) -> None:
        self.__controlador_tipos_atendimento.abre_tela()

    def cadastra_atendimentos(self) -> None:
        return self.__controlador_atendimentos.abre_tela()

    def cadastra_procedimentos(self) -> None:
        return self.__controlador_procedimentos.abre_tela()

    def cadastra_pagamentos(self) -> None:
        return self.__controlador_pagamentos.abre_tela()

    def cadastra_relatorios(self) -> None:
        return self.__controlador_relatorios.abre_tela()

    def encerra_sistema(self) -> None:
        exit(0)

    def abre_tela(self) -> None:
        lista_opcoes = {1: self.cadastra_pacientes, 2: self.cadastra_profissionais,
                        3: self.cadastra_clinica, 4: self.cadastra_tipos_atendimento,
                        5: self.cadastra_atendimentos, 6: self.cadastra_procedimentos,
                        7: self.cadastra_pagamentos, 8: self.cadastra_relatorios,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()