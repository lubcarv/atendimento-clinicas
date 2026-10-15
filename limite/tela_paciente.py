from limite.tela_abstrata import TelaAbstrata

class TelaPaciente(TelaAbstrata):
    def tela_opcoes(self) -> int:
        print('\n====== Sistema de Pacientes ======')
        print('1. Incluir Paciente')
        print('2. Alterar Paciente')
        print('3. Listar Pacientes')
        print('4. Excluir Paciente')
        print('0. Retornar')

        return self.le_num_inteiro('Escolha a opção: ', [0, 1, 2, 3, 4])

    def pega_dados_paciente(self) -> dict:
        print("\n====== DADOS DO PACIENTE ======")
        nome = self.le_texto('Nome: ')
        celular = self.le_texto('Celular: ')
        cpf = self.le_CPF('CPF: ')
        data_nascimento = self.le_data('Data de Nascimento: ')

        return {'nome': nome, 
                'celular': celular, 
                'cpf': cpf, 
                'data_nascimento': data_nascimento}

    def mostra_paciente(self, dados_paciente) -> None:
        print(f'NOME DO PACIENTE: {dados_paciente['nome']}')
        print(f'CELULAR DO PACIENTE: {dados_paciente['celular']}')
        print(f'CPF: {dados_paciente['cpf']}')
        print(f'DATA DE NASCIMENTO (dd/mm/aaaa): {dados_paciente['data_nascimento']}')
        print('\n')

    def seleciona_paciente(self) -> str:
        cpf = self.le_CPF('CPF do paciente que deseja selecionar: ')
        return cpf

    def mostra_mensagem(self, msg) -> None:
        print(msg)

    