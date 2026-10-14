from exceptions.atendimento_inexistente_exception import AtendimentoInexistenteException
from limite.tela_procedimento import TelaProcedimento
from exceptions.procedimento_repetido_exception import ProcedimentoRepetidoException
from exceptions.procedimento_inexistente_exception import ProcedimentoInexistenteException
from exceptions.profissional_inexistente_exception import ProfissionalInexistenteException


class ControladorProcedimentos:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_procedimento = TelaProcedimento()
        self.__continua = True


    def pega_procedimento_por_codigo(self, atendimento, codigo: int):
        for procedimento in atendimento.procedimentos:
            if procedimento.codigo == codigo:
                return procedimento
        return None

    def __seleciona_atendimento(self):
        self.__controlador_sistema.controlador_atendimentos().lista_atendimentos()
        codigo = self.__tela_procedimento.seleciona_atendimento()
        atendimento = self.__controlador_sistema.controlador_atendimentos().pega_atendimento_por_codigo(codigo)
        if atendimento is None:
            raise AtendimentoInexistenteException(codigo)
        return atendimento

    def __mostra_procedimentos(self, atendimento):
        if not atendimento.procedimentos:
            self.__tela_procedimento.mostra_mensagem("Nenhum procedimento registrado neste atendimento.")
            return
        for procedimento in atendimento.procedimentos:
            self.__tela_procedimento.mostra_procedimento({
                "codigo": procedimento.codigo,
                "descricao": procedimento.descricao,
                "custo": procedimento.custo,
                "profissional": procedimento.profissional.nome})

    def incluir_procedimento(self):
        try:
            atendimento = self.__seleciona_atendimento()
            dados = self.__tela_procedimento.pega_dados_procedimento()
            if self.pega_procedimento_por_codigo(atendimento, dados["codigo"]) is not None:
                raise ProcedimentoRepetidoException(dados["codigo"])

            profissional = self.__controlador_sistema.controlador_profissionais.pega_profissional_por_cpf(
                dados["cpf_profissional"])
            if profissional is None:
                raise ProfissionalInexistenteException(dados["cpf_profissional"])

            atendimento.incluir_procedimento(dados["codigo"], dados["descricao"], dados["custo"], profissional)
            self.__tela_procedimento.mostra_mensagem("Procedimento incluído com sucesso.")

        except (AtendimentoInexistenteException, ProcedimentoRepetidoException,
                ProfissionalInexistenteException, TypeError, ValueError) as e:
            self.__tela_procedimento.mostra_mensagem(e)

    def lista_procedimentos(self):
        try:
            atendimento = self.__seleciona_atendimento()
            self.__mostra_procedimentos(atendimento)
        except AtendimentoInexistenteException as e:
            self.__tela_procedimento.mostra_mensagem(e)

    def alterar_procedimento(self):
        try:
            atendimento = self.__seleciona_atendimento()
            self.__mostra_procedimentos(atendimento)
            codigo = self.__tela_procedimento.seleciona_procedimento()
            procedimento = self.pega_procedimento_por_codigo(atendimento, codigo)
            if procedimento is None:
                raise ProcedimentoInexistenteException(codigo)

            dados = self.__tela_procedimento.pega_dados_procedimento()
            profissional = self.__controlador_sistema.controlador_profissionais().pega_profissional_por_cpf(
                dados["cpf_profissional"])
            if profissional is None:
                raise ProfissionalInexistenteException(dados["cpf_profissional"])

            procedimento.custo = dados["custo"]
            procedimento.descricao = dados["descricao"]
            procedimento.profissional = profissional
            self.__tela_procedimento.mostra_mensagem("Procedimento alterado com sucesso.")
        except (AtendimentoInexistenteException, ProcedimentoInexistenteException,
                ProfissionalInexistenteException, TypeError, ValueError) as e:
            self.__tela_procedimento.mostra_mensagem(e)

    def excluir_procedimento(self):
        try:
            atendimento = self.__seleciona_atendimento()
            self.__mostra_procedimentos(atendimento)
            codigo = self.__tela_procedimento.seleciona_procedimento()
            procedimento = self.pega_procedimento_por_codigo(atendimento, codigo)
            if procedimento is None:
                raise ProcedimentoInexistenteException(codigo)
            atendimento.excluir_procedimento(procedimento)
            self.__tela_procedimento.mostra_mensagem("Procedimento excluído.")
        except (AtendimentoInexistenteException, ProcedimentoInexistenteException) as e:
            self.__tela_procedimento.mostra_mensagem(e)

    def retornar(self):
        self.__continua = False

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_procedimento, 2: self.alterar_procedimento,
                        3: self.lista_procedimentos, 4: self.excluir_procedimento,
                        0: self.retornar}
        self.__continua = True
        while self.__continua:
            lista_opcoes[self.__tela_procedimento.tela_opcoes()]()