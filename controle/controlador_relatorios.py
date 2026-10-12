from limite.tela_relatorios import TelaRelatorio
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controlador_sistema import ControladorSistema
    from controlador_clinicas import ControladorClinicas
    # from controlador_procedimentos import ControladorProcedimentos

class ControladorRelatorios:
    def __init__(self, controlador_sistema: ControladorSistema, controlador_procedimentos,  controlador_clinicas: ControladorClinicas):
        self.__controlador_sistema = controlador_sistema
        self.__tela_relatorio = TelaRelatorio()
        self.__procedimentos = controlador_procedimentos
        self.__controlador_clinica = controlador_clinicas

    def clinica_com_mais_atendimentos(self):
        # Preciso do Controller de atendimentos e preciso de um método que faça a quantidade de atendimentos
        # por clínica

