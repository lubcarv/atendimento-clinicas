from limite.tela_paciente import TelaPaciente
from entidade.paciente import Paciente
from exceptions.paciente_repetido_exception import PacienteRepetidoException
from exceptions.paciente_inexistente_exception import PacienteInexistenteException

class ControladorPacientes:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_paciente = TelaPaciente()
        self.__pacientes = []

    def pega_paciente_por_cpf(self, cpf: str):
        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                return paciente
        return None

    def incluir_paciente(self):
        dados_paciente = self.__tela_paciente.pega_dados_paciente()
        cpf = dados_paciente['cpf']
        paciente = self.pega_paciente_por_cpf(cpf)
        try:
            if paciente == None:
                paciente = Paciente(dados_paciente['nome'], dados_paciente['celular'], dados_paciente['cpf'], dados_paciente['data_nascimento'])
                self.__pacientes.append(paciente)
            else:
                raise PacienteRepetidoException(cpf)
        except PacienteRepetidoException as e:
            self.__tela_paciente.mostra_mensagem(e)

    def alterar_paciente(self):
        self.lista_pacientes()
        cpf_paciente = self.__tela_paciente.seleciona_paciente()
        paciente = self.pega_paciente_por_cpf(cpf_paciente)

        try:
            if paciente is not None:
                novos_dados_paciente = self.__tela_paciente.pega_dados_paciente()
                paciente.nome = novos_dados_paciente['nome']
                paciente.celular = novos_dados_paciente['celular']
                paciente.cpf = novos_dados_paciente['cpf']
                paciente.data_nascimento = novos_dados_paciente['data_nascimento']
            else:
                raise PacienteInexistenteException(cpf_paciente)

        except PacienteInexistenteException as e:
            self.__tela_paciente.mostra_mensagem(e)

    def lista_pacientes(self):
        if len(self.__pacientes) == 0:
            print('A lista de pacientes está vazia')
        else:
            for paciente in self.__pacientes:
                self.__tela_paciente.mostra_paciente({'nome': paciente.nome, 'celular': paciente.celular, 
                                                    'cpf': paciente.cpf, 'data_nascimento': paciente.data_nascimento})

    def excluir_paciente(self):
        self.lista_pacientes()
        cpf_paciente = self.__tela_paciente.seleciona_paciente()
        paciente = self.pega_paciente_por_cpf(cpf_paciente)

        try:
            if paciente is not None:
                self.__pacientes.remove(paciente)
                self.lista_pacientes()
            else:
                raise PacienteInexistenteException(cpf_paciente)

        except PacienteInexistenteException as e:
            self.__tela_paciente.mostra_mensagem(e)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_paciente, 2: self.alterar_paciente, 3: self.lista_pacientes, 4: self.excluir_paciente, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_paciente.tela_opcoes()]()

    