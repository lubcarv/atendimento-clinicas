from limite.tela_abstrata import TelaAbstrata


class TelaAtendimento(TelaAbstrata):

    def tela_opcoes(self) -> int:
        print("____ Atendimentos ____")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Listar")
        print("4 - Excluir")
        print("0 - Retornar")
        return self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

    def pega_dados_atendimento(self) -> dict:
        print("____ Dados do atendimento ____")
        codigo = self.le_num_inteiro("Código: ")
        cpf_paciente = self.le_texto("CPF do paciente: ")
        cpf_profissional = self.le_CPF("CPF do profissional: ")
        codigo_clinica = self.le_num_inteiro("Código da clínica: ")
        codigo_tipo_atendimento = self.le_num_inteiro("Código do tipo de atendimento: ")
        data = self.le_data("Data do atendimento (dd/mm/aaaa): ")
        horario_inicio = self.le_horario("Horário de início (hh:mm): ")
        horario_fim = self.le_horario("Horário de fim (hh:mm): ")
        valor = self.le_valor("Valor: R$ ")

        return {"codigo": codigo,
                "cpf_paciente": cpf_paciente,
                "cpf_profissional": cpf_profissional,
                "codigo_clinica": codigo_clinica,
                "codigo_tipo_atendimento": codigo_tipo_atendimento,
                "data": data,
                "horario_inicio": horario_inicio,
                "horario_fim": horario_fim,
                "valor": valor}

    def pega_dados_acompanhante(self) -> dict:
        print("____ Dados do acompanhante ____")
        nome = self.le_texto("Nome do acompanhante: ")
        celular = self.le_texto("Celular do acompanhante: ")
        cpf = self.le_CPF("CPF do acompanhante: ")
        data_nascimento = self.le_data("Data de nascimento do acompanhante (dd/mm/aaaa): ")

        return { "nome": nome,
                 "celular": celular,
                 "cpf": cpf,
                 "data_nascimento": data_nascimento
        }

    def mostra_atendimento(self, dados_atendimento: dict):
        print("____ Atendimento ____")
        print(f"Código: {dados_atendimento['codigo']}")
        print(f"Paciente: {dados_atendimento['paciente']}")
        print(f"Acompanhante: {dados_atendimento['acompanhante']}")
        print(f"Profissional: {dados_atendimento['profissional']}")
        print(f"Clínica: {dados_atendimento['clinica']}")
        print(f"Tipo de atendimento: {dados_atendimento['tipo_atendimento']}")
        print(f"Data: {dados_atendimento['data'].strftime('%d/%m/%Y')}")
        print(f"Horário: {dados_atendimento['horario_inicio'].strftime('%H:%M')} às "
              f"{dados_atendimento['horario_fim'].strftime('%H:%M')}")
        print(f"Valor: R$ {dados_atendimento['valor']:.2f}")
        print(f"Valor pago: R$ {dados_atendimento['valor_pago']:.2f}")
        print(f"Valor restante: R$ {dados_atendimento['valor_restante']:.2f}")

    def pergunta_acompanhante(self, nome_paciente: str) -> bool:
        print(f"O paciente {nome_paciente} é menor de idade e só pode ser atendido com um acompanhante maior de idade.")
        opcao = self.le_num_inteiro("Deseja informar o acompanhante agora? (1 - Sim, 0 - Não): ", [0, 1])
        return opcao == 1

    def seleciona_atendimento(self) -> int:
        return self.le_num_inteiro("Código do atendimento: ")



