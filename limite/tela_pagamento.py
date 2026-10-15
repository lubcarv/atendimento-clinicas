from limite.tela_abstrata import TelaAbstrata


class TelaPagamento(TelaAbstrata):

    def tela_opcoes(self) -> int:
        print("\n____ Pagamentos ____")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Listar")
        print("4 - Excluir")
        print("0 - Retornar")
        return self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

    def seleciona_atendimento(self) -> str:
        return self.le_texto("\nCódigo do atendimento: ")

    def seleciona_modalidade(self) -> int:
        print("\n____ Modalidade ____")
        print("1 - Dinheiro")
        print("2 - PIX")
        print("3 - Cartão de crédito")
        return self.le_num_inteiro("Escolha a modalidade: ", [1, 2, 3])

    def pega_dados_pagamento(self, modalidade: int, pede_codigo: bool = True) -> dict:
        print("\n____ Dados do pagamento ____")
        dados = {}
        if pede_codigo:
            dados["codigo"] = self.le_texto("CÓDIGO DO PAGAMENTO: ")
        dados["data"] = self.le_data("DATA DO PAGAMENTO (dd/mm/aaaa): ")
        dados["valor_pago"] = self.le_valor("VALOR PAGO: R$ ")
        if modalidade == 2:
            dados["cpf_pagador"] = self.le_CPF("CPF DO PAGADOR: ")
        elif modalidade == 3:
            dados["numero_cartao"] = self.le_texto("NÚMERO DO CARTÃO: ")
            dados["bandeira"] = self.le_texto("BANDEIRA: ")
        return dados

    def mostra_pagamento(self, dados_pagamento: dict):
        print(f"Código: {dados_pagamento['codigo']} | {dados_pagamento['modalidade']} | "
              f"{dados_pagamento['data'].strftime('%d/%m/%Y')} | "
              f"R$ {dados_pagamento['valor_pago']:.2f}")

    def seleciona_pagamento(self) -> str:
        return self.le_texto("Código do pagamento: ")