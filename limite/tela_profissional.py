from limite.tela_abstrata import TelaAbstrata

class TelaProfissional(TelaAbstrata):
    def tela_opcoes(self) -> int:
        print('====== SISTEMA DE PROFISSIONAIS ======')
        print('1. Incluir Profissional')
        print('2. Alterar Profissional')
        print('3. Listar Profissionais')
        print('4. Excluir Profissional')
        print('0. Retornar')
        return self.le_num_inteiro('Escolha a opção: ', [0, 1, 2, 3, 4])

    def pega_dados_profissional(self) -> dict:
        print('======= DADOS DO PROFISSIONAL ======')
        nome = self.le_texto('NOME DO PROFISSIONAL: ')
        celular = self.le_texto('CELULAR DO PROFISSIONAL: ')
        cpf = self.le_CPF('CPF DO PROFISSIONAL: ')
        data_nascimento = self.le_data('DATA DE NASCIMENTO DO PROFISSIONAL: ')
        especialidade = self.le_texto('ESPECIALIDADE DO PROFISSIONAL')
        registro_profissional = self.le_texto('REGISTRO PROFISSIONAL: ')

        return {'nome': nome, 'celular': celular, 'cpf': cpf, 'data_nascimento': data_nascimento,
                'especialidade': especialidade, 'registro_profissional': registro_profissional}

    def mostra_profissional(self, dados_profissional: dict) -> None:
        print(f'NOME DO PROFISSIONAL: {dados_profissional['nome']}')
        print(f'CELULAR DO PROFISSIONAL: {dados_profissional['celular']}')
        print(f'CPF DO PROFISSIONAL: {dados_profissional['cpf']}')
        print(f'DATA DE NASCIMENTO DO PROFISSIONAL: {dados_profissional['data_nascimento']}')
        print(f'ESPECIALIDADE DO PROFISSIONAL: {dados_profissional['especialidade']}')
        print(f'REGISTRO PROFISSIONAL: {dados_profissional['registro_profissional']}')
        print('\n')

    def seleciona_profissional(self) -> str:
        cpf = self.le_CPF('CPF do Profissional que deseja selecionar: ')
        return cpf

    def mostra_mensagem(self, msg: str) -> None:
        print(msg)


        