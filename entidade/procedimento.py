from entidade.profissional import Profissional


class Procedimento:
    def __init__(self, codigo: str, descricao: str, custo: float, profissional: Profissional):
        if not isinstance(codigo, str):
            raise TypeError("Código deve ser um texto")
        self.__codigo = codigo
        self.descricao = descricao
        self.custo = custo
        self.profissional = profissional

    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if not isinstance(descricao, str):
            raise TypeError("Descrição deve ser texto.")
        if not descricao.strip():
            raise ValueError("Descrição não pode ficar vazia.")
        self.__descricao = descricao

    @property
    def custo(self) -> float:
        return self.__custo

    @custo.setter
    def custo(self, custo: float):
        if not isinstance(custo, (float, int)):
            raise TypeError("Custo deve ser um número")
        if custo <= 0:
            raise ValueError("Custo deve ser maior que zero.")
        self.__custo = custo

    @property
    def profissional(self) -> Profissional:
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional: Profissional):
        if not isinstance(profissional, Profissional):
            raise TypeError("Profissional deve ser do tipo Profissional.")
        self.__profissional = profissional
