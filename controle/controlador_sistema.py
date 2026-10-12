from limite.tela_sistema import TelaSistema
from controlador_pacientes import ControladorPacientes
from controlador_profissionais import ControladorProfissionais
from controlador_clinicas import ControladorClinicas
from controlador_tipos_atendimento import ControladorTiposAtendimento
# Controlador Atendimentos aqui
# Controlador Procedimentos aqui
# Controlador Pagamentos aqui
from controlador_relatorios import ControladorRelatorios

class ControladorSistema:
    def __init__(self):
        self.__controlador_pacientes = ControladorPacientes(self)
        self.__controlador_profissionais = ControladorProfissionais(self)
        self.__controlador_clinica = ControladorClinicas(self)
        self.__controlador_tipos_atendimento = ControladorTiposAtendimento(self)
        # self.__controlador_atendimentos = ControladorAtendimentos(self)
        # self.__controlador_procedimentos = ControladorProcedimentos(self)
        # self.__controlador_pagamentos = ControladorPagamentos(self)
        self.__controlador_relatorios = ControladorRelatorios(self)
        self.__tela_sistema = TelaSistema()

    def controlador_pacientes(self):
        return self.__controlador_pacientes

    def controlador_profissionais(self):
        return self.__controlador_profissionais

    def controlador_clinica(self):
        return self.__controlador_clinica

    def controlador_tipos_atendimento(self):
        return self.__controlador_tipos_atendimento

    # def controlador_atendimentos(self):
        # return self.__controlador_atendimentos

    # def controlador_procedimentos(self):
        # return self.__controlador_procedimentos

    # def controlador_pagamentos(self):
        # return self.__controlador_pagamentos

    def controlador_relatorios(self):
        return self.__controlador_relatorios

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_pacientes(self):
        self.__controlador_pacientes.abre_tela()

    def cadastra_profissionais(self):
        self.__controlador_profissionais.abre_tela()

    def cadastra_clinica(self):
        self.__controlador_clinica.abre_tela()

    def cadastra_tipos_atendimento(self):
        self.__controlador_tipos_atendimento.abre_tela()

    # def cadastra_atendimentos(self):
        # return self.__controlador_atendimentos

    # def cadastra_procedimentos(self):
        # return self.__controlador_procedimentos

    # def cadastra_pagamentos(self):
        # return self.__controlador_pagamentos

    def cadastra_relatorios(self):
        return self.__controlador_relatorios

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_pacientes, 2: self.cadastra_profissionais,
                        3: self.cadastra_profissionais, 4: self.cadastra_clinica,
                        5: self.cadastra_tipos_atendimento, 6: self.cadastra_atendimentos,
                        7: self.cadastra_procedimentos, 8: self.cadastra_pagamentos,
                        9: self.cadastra_relatorios}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()