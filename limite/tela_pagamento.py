from limite.tela_abstrata import TelaAbstrata


class TelaPagamento(TelaAbstrata):

    def tela_opcoes(self) -> int:
        print("____ Pagamentos ____")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Listar")
        print("4 - Excluir")
        print("0 - Retornar")
        return self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

    def seleciona_atendimento(self) -> int:
        return self.le_num_inteiro("Código do atendimento: ")

    def seleciona_modalidade(self) -> int:
        print("____ Modalidade ____")
        print("1 - Dinheiro")
        print("2 - PIX")
        print("3 - Cartão de crédito")
        return self.le_num_inteiro("Escolha a modalidade: ", [1, 2, 3])

    def pega_dados_pagamento(self, modalidade: int) -> dict:
        print("____ Dados do pagamento ____")
        dados = {"codigo": self.le_num_inteiro("Código: "),
                 "data": self.le_data("Data do pagamento (dd/mm/aaaa): "),
                 "valor_pago": self.le_valor("Valor pago: R$ ")}
        if modalidade == 2:
            dados["cpf_pagador"] = self.le_texto("CPF do pagador: ")
        elif modalidade == 3:
            dados["numero_cartao"] = self.le_texto("Número do cartão: ")
            dados["bandeira"] = self.le_texto("Bandeira: ")
        return dados

    def mostra_pagamento(self, dados_pagamento: dict):
        print(f"Código: {dados_pagamento['codigo']} | {dados_pagamento['modalidade']} | "
              f"{dados_pagamento['data'].strftime('%d/%m/%Y')} | "
              f"R$ {dados_pagamento['valor_pago']:.2f}")

    def seleciona_pagamento(self) -> int:
        return self.le_num_inteiro("Código do pagamento: ")