from limite.tela_pagamento import TelaPagamento
from entidade.pagamento_pix import PagamentoPix
from entidade.pagamento_cartao import PagamentoCartao
from exceptions.atendimento_inexistente_exception import AtendimentoInexistenteException
from exceptions.pagamento_repetido_exception import PagamentoRepetidoException
from exceptions.pagamento_inexistente_exception import PagamentoInexistenteException
from exceptions.pagamento_apos_atendimento_exception import PagamentoAposAtendimentoException
from exceptions.valor_pago_excedente_exception import ValorPagoExcedenteException


class ControladorPagamentos:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_pagamento = TelaPagamento()
        self.__continua = True

    def pega_pagamento_por_codigo(self, atendimento, codigo: int):
        for pagamento in atendimento.pagamentos:
            if pagamento.codigo == codigo:
                return pagamento
        return None

    # ---------- métodos auxiliares (privados)

    def __seleciona_atendimento(self):
        controlador_atendimentos = self.__controlador_sistema.controlador_atendimentos()
        if not controlador_atendimentos.atendimentos:
            raise ValueError("Nenhum atendimento cadastrado.")
        controlador_atendimentos.lista_atendimentos()
        codigo = self.__tela_pagamento.seleciona_atendimento()
        atendimento = controlador_atendimentos.pega_atendimento_por_codigo(codigo)
        if atendimento is None:
            raise AtendimentoInexistenteException(codigo)
        return atendimento

    def __mostra_pagamentos(self, atendimento):
        if not atendimento.pagamentos:
            self.__tela_pagamento.mostra_mensagem("Nenhum pagamento registrado neste atendimento.")
            return
        for pagamento in atendimento.pagamentos:
            self.__tela_pagamento.mostra_pagamento({
                "codigo": pagamento.codigo,
                "modalidade": pagamento.modalidade(),
                "data": pagamento.data,
                "valor_pago": pagamento.valor_pago})
        self.__tela_pagamento.mostra_mensagem(f"Valor restante: R$ {atendimento.valor_restante():.2f}")

    def __modalidade_de(self, pagamento) -> int:
        if isinstance(pagamento, PagamentoPix):
            return 2
        if isinstance(pagamento, PagamentoCartao):
            return 3
        return 1

    # ---------- CRUD

    def incluir_pagamento(self):
        try:
            atendimento = self.__seleciona_atendimento()
            modalidade = self.__tela_pagamento.seleciona_modalidade()
            dados = self.__tela_pagamento.pega_dados_pagamento(modalidade)
            if self.pega_pagamento_por_codigo(atendimento, dados["codigo"]) is not None:
                raise PagamentoRepetidoException(dados["codigo"])

            if modalidade == 1:
                atendimento.incluir_pagamento_dinheiro(dados["codigo"], dados["data"], dados["valor_pago"])
            elif modalidade == 2:
                atendimento.incluir_pagamento_pix(dados["codigo"], dados["data"], dados["valor_pago"],
                                                  dados["cpf_pagador"])
            else:
                atendimento.incluir_pagamento_cartao(dados["codigo"], dados["data"], dados["valor_pago"],
                                                     dados["numero_cartao"], dados["bandeira"])
            self.__tela_pagamento.mostra_mensagem("Pagamento incluído com sucesso.")
            self.__tela_pagamento.mostra_mensagem(f"Valor restante: R$ {atendimento.valor_restante():.2f}")

        except (AtendimentoInexistenteException, PagamentoRepetidoException,
                PagamentoAposAtendimentoException, ValorPagoExcedenteException,
                TypeError, ValueError) as e:
            self.__tela_pagamento.mostra_mensagem(e)

    def alterar_pagamento(self):
        try:
            atendimento = self.__seleciona_atendimento()
            if not atendimento.pagamentos:
                raise ValueError("Nenhum pagamento registrado neste atendimento.")
            self.__mostra_pagamentos(atendimento)
            codigo = self.__tela_pagamento.seleciona_pagamento()
            pagamento = self.pega_pagamento_por_codigo(atendimento, codigo)
            if pagamento is None:
                raise PagamentoInexistenteException(codigo)

            modalidade = self.__modalidade_de(pagamento)
            dados = self.__tela_pagamento.pega_dados_pagamento(modalidade)

            # As regras são conferidas ANTES de mudar qualquer coisa.
            if dados["data"] > atendimento.data:
                raise PagamentoAposAtendimentoException(dados["data"], atendimento.data)
            if dados["valor_pago"] <= 0:
                raise ValueError("O valor pago deve ser maior que zero.")
            limite = atendimento.valor_restante() + pagamento.valor_pago
            if dados["valor_pago"] > limite:
                raise ValorPagoExcedenteException(dados["valor_pago"], limite)

            # O número do cartão é o único setter que ainda pode recusar, por isso vem primeiro.
            if modalidade == 3:
                pagamento.numero_cartao = dados["numero_cartao"]
                pagamento.bandeira = dados["bandeira"]
            elif modalidade == 2:
                pagamento.cpf_pagador = dados["cpf_pagador"]
            pagamento.valor_pago = dados["valor_pago"]
            pagamento.data = dados["data"]
            self.__tela_pagamento.mostra_mensagem("Pagamento alterado com sucesso.")

        except (AtendimentoInexistenteException, PagamentoInexistenteException,
                PagamentoAposAtendimentoException, ValorPagoExcedenteException,
                TypeError, ValueError) as e:
            self.__tela_pagamento.mostra_mensagem(e)

    def lista_pagamentos(self):
        try:
            atendimento = self.__seleciona_atendimento()
            self.__mostra_pagamentos(atendimento)
        except (AtendimentoInexistenteException, ValueError) as e:
            self.__tela_pagamento.mostra_mensagem(e)

    def excluir_pagamento(self):
        try:
            atendimento = self.__seleciona_atendimento()
            if not atendimento.pagamentos:
                raise ValueError("Nenhum pagamento registrado neste atendimento.")
            self.__mostra_pagamentos(atendimento)
            codigo = self.__tela_pagamento.seleciona_pagamento()
            pagamento = self.pega_pagamento_por_codigo(atendimento, codigo)
            if pagamento is None:
                raise PagamentoInexistenteException(codigo)
            atendimento.excluir_pagamento(pagamento)
            self.__tela_pagamento.mostra_mensagem("Pagamento excluído.")
        except (AtendimentoInexistenteException, PagamentoInexistenteException, ValueError) as e:
            self.__tela_pagamento.mostra_mensagem(e)

    def retornar(self):
        self.__continua = False

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_pagamento, 2: self.alterar_pagamento,
                        3: self.lista_pagamentos, 4: self.excluir_pagamento,
                        0: self.retornar}
        self.__continua = True
        while self.__continua:
            lista_opcoes[self.__tela_pagamento.tela_opcoes()]()