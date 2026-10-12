from limite.tela_atendimento import TelaAtendimento
from entidade.atendimento import Atendimento
from exceptions.atendimento_repetido_exception import AtendimentoRepetidoException
from exceptions.atendimento_inexistente_exception import AtendimentoInexistenteException
from exceptions.paciente_inexistente_exception import PacienteInexistenteException
from exceptions.profissional_inexistente_exception import ProfissionalInexistenteException
from exceptions.clinica_inexistente_exception import ClinicaInexistenteException
from exceptions.tipo_atendimento_inexistente_exception import TipoAtendimentoInexistenteException

class ControladorAtendimentos:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__atendimentos = []
        self.__tela_atendimento = TelaAtendimento()
        self.__continua = True

    @property
    def atendimentos(self) -> list:
        return self.__atendimentos

    def pega_atendimento_por_codigo(self, codigo: int):
        for atendimento in self.__atendimentos:
            if atendimento.codigo == codigo:
                return atendimento
        return None

    # ---------- métodos auxiliares (privados), usados no incluir e no alterar

    def __busca_cadastros(self, dados: dict):
        sistema = self.__controlador_sistema

        paciente = sistema.controlador_pacientes.pega_paciente_por_cpf(dados["cpf_paciente"])
        if paciente is None:
            raise CadastroInexistenteException("Paciente", dados["cpf_paciente"])

        profissional = sistema.controlador_profissionais.pega_profissional_por_cpf(dados["cpf_profissional"])
        if profissional is None:
            raise CadastroInexistenteException("Profissional", dados["cpf_profissional"])

        clinica = sistema.controlador_clinicas.pega_clinica_por_codigo(dados["codigo_clinica"])
        if clinica is None:
            raise CadastroInexistenteException("Clínica", dados["codigo_clinica"])

        tipo_atendimento = sistema.controlador_tipos_atendimento.pega_tipo_atendimento_por_codigo(
            dados["codigo_tipo_atendimento"])
        if tipo_atendimento is None:
            raise CadastroInexistenteException("Tipo de atendimento", dados["codigo_tipo_atendimento"])

        return paciente, profissional, clinica, tipo_atendimento

    def __verifica_regras_da_clinica(self, profissional, clinica, horario_inicio, horario_fim):
        if profissional not in clinica.profissionais:
            raise ProfissionalNaoVinculadoException(profissional.nome, clinica.nome)
        if not clinica.esta_aberta(horario_inicio, horario_fim):
            raise HorarioForaDoFuncionamentoException(clinica.nome)

    def __verifica_acompanhante(self, atendimento: Atendimento):
        paciente = atendimento.paciente
        if paciente.maior_de_idade(atendimento.data) or atendimento.acompanhante is not None:
            return
        if not self.__tela_atendimento.pergunta_acompanhante(paciente.nome):
            raise PacienteMenorDeIdadeException(paciente.nome)
        dados = self.__tela_atendimento.pega_dados_acompanhante()
        atendimento.incluir_acompanhante(dados["nome"], dados["celular"],
                                         dados["cpf"], dados["data_nascimento"])

    # ---------- CRUD

    def incluir_atendimento(self):
        dados = self.__tela_atendimento.pega_dados_atendimento()
        try:
            if self.pega_atendimento_por_codigo(dados["codigo"]) is not None:
                raise CadastroRepetidoException("Atendimento", dados["codigo"])

            paciente, profissional, clinica, tipo_atendimento = self.__busca_cadastros(dados)
            self.__verifica_regras_da_clinica(profissional, clinica,
                                              dados["horario_inicio"], dados["horario_fim"])

            atendimento = Atendimento(dados["codigo"], clinica, paciente, profissional,
                                      tipo_atendimento, dados["data"], dados["horario_inicio"],
                                      dados["horario_fim"], dados["valor"])
            self.__verifica_acompanhante(atendimento)

            self.__atendimentos.append(atendimento)
            self.__tela_atendimento.mostra_mensagem("Atendimento incluído com sucesso.")

        except (CadastroRepetidoException, CadastroInexistenteException,
                ProfissionalNaoVinculadoException, HorarioForaDoFuncionamentoException,
                PacienteMenorDeIdadeException, AcompanhanteMenorDeIdadeException,
                TypeError, ValueError) as e:
            self.__tela_atendimento.mostra_mensagem(e)

    def alterar_atendimento(self):
        pass  # você faz

    def lista_atendimentos(self):
        if not self.__atendimentos:
            self.__tela_atendimento.mostra_mensagem("Nenhum atendimento cadastrado.")
            return
        for atendimento in self.__atendimentos:
            if atendimento.acompanhante is not None:
                acompanhante = atendimento.acompanhante.nome
            else:
                acompanhante = "Nenhum"
            self.__tela_atendimento.mostra_atendimento({
                "codigo": atendimento.codigo,
                "paciente": atendimento.paciente.nome,
                "acompanhante": acompanhante,
                "profissional": atendimento.profissional.nome,
                "clinica": atendimento.clinica.nome,
                "tipo_atendimento": atendimento.tipo_atendimento.nome,
                "data": atendimento.data,
                "horario_inicio": atendimento.horario_inicio,
                "horario_fim": atendimento.horario_fim,
                "valor": atendimento.valor,
                "valor_pago": atendimento.valor_pago(),
                "valor_restante": atendimento.valor_restante()})

    def excluir_atendimento(self):
        self.lista_atendimentos()
        codigo = self.__tela_atendimento.seleciona_atendimento()
        try:
            atendimento = self.pega_atendimento_por_codigo(codigo)
            if atendimento is None:
                raise CadastroInexistenteException("Atendimento", codigo)
            self.__atendimentos.remove(atendimento)
            self.__tela_atendimento.mostra_mensagem("Atendimento excluído.")
        except CadastroInexistenteException as e:
            self.__tela_atendimento.mostra_mensagem(e)

    def retornar(self):
        self.__continua = False

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_atendimento, 2: self.alterar_atendimento,
                        3: self.lista_atendimentos, 4: self.excluir_atendimento,
                        0: self.retornar}
        self.__continua = True
        while self.__continua:
            lista_opcoes[self.__tela_atendimento.tela_opcoes()]()