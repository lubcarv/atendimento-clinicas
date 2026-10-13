from limite.tela_abstrata import TelaAbstrata


class TelaProcedimento(TelaAbstrata):

    def tela_opcoes(self) -> int:
        print("____ Procedimentos ____")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Listar")
        print("4 - Excluir")
        print("0 - Retornar")
        return self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

    def seleciona_atendimento(self) -> int:
        return self.le_num_inteiro("Código do atendimento: ")

    def pega_dados_procedimento(self) -> dict:
        print("____ Dados do procedimento ____")
        dados = {"codigo": self.le_num_inteiro("Código do procedimento: "),
                 "descricao": self.le_texto("Descrição do procedimento: "),
                 "custo": self.le_valor("Custo do procedimento: "),
                 "cpf_profissional": self.le_CPF("CPF do profissional: ")}
        return dados

    def mostra_procedimento(self, dados_procedimento: dict):
        print(f"Código: {dados_procedimento['codigo']} | Descrição: {dados_procedimento['descricao']} | "
              f"Custo: R$ {dados_procedimento['custo']:.2f} | "
              f"Profissional: {dados_procedimento['profissional']}")

    def seleciona_procedimento(self) -> int:
        return self.le_num_inteiro("Código do procedimento: ")