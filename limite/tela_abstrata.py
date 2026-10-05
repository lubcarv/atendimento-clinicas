import math
from datetime import datetime, date, time
from abc import ABC, abstractmethod

class TelaAbstrata(ABC):

    @abstractmethod
    def tela_opcoes(self) -> int:
        pass

    def le_num_inteiro(self, mensagem: str = "", ints_validos: list = None) -> int:
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError
                return valor_int
            except ValueError:
                print("Valor incorreto")
                if ints_validos:
                    print("Valores válidos:", ints_validos)

    def le_valor(self, mensagem: str = "") -> float:
        while True:
            valor_lido = input(mensagem).strip().replace(",", ".")
            try:
                valor = float(valor_lido)
                if not math.isfinite(valor) or valor < 0:
                    raise ValueError
                return valor
            except ValueError:
                print("Valor incorreto! Digite um número maior ou igual a zero.")

    def le_data(self, mensagem: str = "") -> date:
        while True:
            valor_lido = input(mensagem).strip()
            try:
                return datetime.strptime(valor_lido, "%d/%m/%Y").date()
            except ValueError:
                print("Data incorreta! Use o formato dd/mm/aaaa")

    def le_horario(self, mensagem: str = "") -> time:
        while True:
            valor_lido = input(mensagem).strip()
            try:
                return datetime.strptime(valor_lido, "%H:%M").time()
            except ValueError:
                print("Hora incorreta! Use o formato hh:mm")

    def le_texto(self, mensagem: str = "") -> str:
        while True:
            texto = input(mensagem).strip()
            if texto:
                return texto
            print("Este campo não pode ficar vazio")

    def mostra_mensagem(self, msg: str) -> None:
        print(msg)