from limite.tela_abstrata import TelaAbstrata


class TelaClinica(TelaAbstrata):
    def tela_opcoes(self) -> int:
        print('====== Sistema de Clínicas ======')
        print('1. Incluir Clínica')
        print('2. Alterar Clínica')
        print('3. Lista de Clínicas')
        print('4. Excluir Clínica')
        print('5. Vincular Profissional')
        print('6. Desvincular Profissional')
        print('0. Retornar')
        return self.le_num_inteiro('Escolha a opção: ', [0, 1, 2, 3, 4, 5, 6])

    def pega_dados_clinica(self) -> dict:
        print("====== DADOS DA CLÍNICA ======")
        codigo = self.le_texto('Código: ')
        nome = self.le_texto('Nome: ')
        localizacao = self.le_texto('Localização: ')
        descricao = self.le_texto('Descrição: ')
        horario_abertura, horario_fechamento = self.pega_horarios()

        return {'código': codigo,
                'nome': nome,
                'localização': localizacao,
                'descrição': descricao,
                'horário_abertura': horario_abertura,
                'horário_fechamento': horario_fechamento}

    def mostra_clinica(self, dados_clinica: dict) -> None:
        print('====== DETALHES DA CLÍNICA ======')
        print(f'NOME DA CLÍNICA: {dados_clinica["nome"]}')
        print(f'CÓDIGO DA CLÍNICA: {dados_clinica['código']}')
        print(f'LOCALIZAÇÃO DA CLÍNICA: {dados_clinica['localização']}')
        print(f'DESCRIÇÃO: {dados_clinica['descrição']}')
        print(f'HORÁRIO: Das {dados_clinica['horário_abertura']} às {dados_clinica['horário_fechamento']}')
        print('\n')

        profissionais = [profissional.nome for profissional in dados_clinica['profissionais']]
        if len(profissionais) == 0:
            print('Nenhum profissional vinculado no momento')
        else:
            print(f'PROFISSIONAIS VINCULADOS: {profissionais}')

    def pega_horarios(self) -> tuple:
        horario_abertura = self.le_horario('Horário de Abertura (HH:MM): ')
        horario_fechamento = self.le_horario('Horário de Fechamento (HH:MM): ')
        return horario_abertura, horario_fechamento

    def seleciona_clinica(self) -> str:
        codigo = self.le_texto('Código da clínica que deseja selecionar: ')
        return codigo

    def seleciona_profissional(self) -> str:
        cpf = self.le_texto('Digite o CPF do profissional que deseja vincular: ')
        return cpf

    def mostra_mensagem(self, msg) -> None:
        print(msg)

    

        
