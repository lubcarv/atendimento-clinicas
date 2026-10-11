from tela_abstrata import TelaAbstrata

class TelaPaciente(TelaAbstrata):
    def tela_opcoes(self) -> int:
        print('====== Sistema de Pacientes ======')
        print('1. Procurar Paciente por CPF')
        print('2. Incluir Paciente')
        print('3. Alterar Paciente')
        print('4. Listar Pacientes')
        print('5. Excluir Paciente')
        print('0. Retornar')

        opcao = int(input('Escolha a opção: '))
        return opcao

    def pega_dados_paciente(self) -> dict:
        print("====== DADOS DO PACIENTE ======")
        nome = input('Nome: ')
        celular = input('Celular: ')
        cpf = self.le_CPF('CPF: ')
        data_nascimento = self.le_data('Data de Nascimento: ')

        return {'nome': nome, 'celular': celular, 'cpf': cpf, 'data_nascimento': data_nascimento}

    def mostra_paciente(self, dados_paciente) -> None:
        print(f'NOME DO PACIENTE: {dados_paciente['nome']}')
        print(f'CELULAR DO PACIENTE: {dados_paciente['celular']}')
        print(f'CPF: {dados_paciente['cpf']}')
        print(f'DATA DE NASCIMENTO: {dados_paciente['data_nascimento']}')
        print('\n')

    def seleciona_paciente(self) -> str:
        cpf = input('CPF do paciente que deseja selecionar: ')
        return cpf

    def mostra_mensagem(self, msg) -> None:
        print(msg)

    