from limite.tela_clinica import TelaClinica
from entidade.clinica import Clinica
from exceptions.clinica_repetida_exception import ClinicaRepetidaException
from exceptions.clinica_inexistente_exception import ClinicaInexistenteException

class ControladorClinicas:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_clinica = TelaClinica()
        self.__clinicas = []

    def pega_clinica_por_codigo(self, codigo: int) -> Clinica:
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
                clinica.nome = novos_dados_clinica['nome']
                clinica.telefone = novos_dados_clinica['telefone']
                clinica.codigo = novos_dados_clinica['código']
                clinica.descricao = novos_dados_clinica['descrição']
                clinica.horario_abertura = novos_dados_clinica['horário_abertura']
                clinica.horario_fechamento = novos_dados_clinica['horário_fechamento']
            else:
                raise ClinicaInexistenteException(codigo_clinica)

        except ClinicaInexistenteException as e:
            self.__tela_clinica.mostra_mensagem(e)

    def lista_clinicas(self) -> None:
        if len(self.__pacientes) == 0:
            print('A lista de pacientes está vazia')
        else:
            for clinica in self.__clinicas:
                self.__tela_clinica.mostra_clinica({'nome': clinica.nome, 'localização': clinica.localizacao, 
                                                    'descrição': clinica.descricao, 'horário': clinica.horario,
                                                    'profissionais': clinica.profissionais})

    def excluir_clinica(self):
        self.lista_clinicas()
        codigo_clinica = self.__tela_clinica.seleciona_clinica()
        clinica = self.pega_clinica_por_codigo(codigo_clinica)
        try:
            if clinica is not None:
                self.__clinicas.remove(clinica)
                self.lista_clinicas()
            else:
                raise ClinicaInexistenteException(codigo_clinica)

        except ClinicaInexistenteException as e:
            self.__tela_clinica.mostra_mensagem(e)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_clinica, 2: self.alterar_clinica, 3: self.lista_clinicas, 4: self.excluir_clinica, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_clinica.tela_opcoes()]()
    
            