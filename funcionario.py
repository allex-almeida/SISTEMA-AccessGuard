from pessoa import Pessoa
from datetime import datetime


class Funcionario(Pessoa):

    def __init__(self, nome, cpf, identificacao, email,
                 cargo, setor, dataCadastro=None):

        super().__init__(nome, cpf, identificacao, email)

        self.__cargo = cargo
        self.__setor = setor

        self.__horarioEntrada = ""
        self.__horarioSaida = ""

        self.__horarioAlmoco = ""
        self.__horarioVoltaAlmoco = ""

        if dataCadastro is None:
            self.__dataCadastro = datetime.now().strftime("%d/%m/%Y")
        else:
            self.__dataCadastro = dataCadastro

    def get_cargo(self):
        return self.__cargo

    def get_setor(self):
        return self.__setor

    def get_horarioEntrada(self):
        return self.__horarioEntrada

    def get_horarioSaida(self):
        return self.__horarioSaida

    def get_horarioAlmoco(self):
        return self.__horarioAlmoco

    def get_horarioVoltaAlmoco(self):
        return self.__horarioVoltaAlmoco

    def get_dataCadastro(self):
        return self.__dataCadastro

    def set_cargo(self, cargo):
        self.__cargo = cargo

    def set_setor(self, setor):
        self.__setor = setor

    def set_horarioEntrada(self, horario):
        self.__horarioEntrada = horario

    def set_horarioSaida(self, horario):
        self.__horarioSaida = horario

    def set_horarioAlmoco(self, horario):
        self.__horarioAlmoco = horario

    def set_horarioVoltaAlmoco(self, horario):
        self.__horarioVoltaAlmoco = horario

    def registrar_entrada(self, horario):

        self.__horarioEntrada = horario

        print("\nEntrada registrada com sucesso")

    def registrar_saida(self, horario):

        self.__horarioSaida = horario

        print("\nSaída registrada com sucesso")

    def registrar_saida_almoco(self, horario):

        self.__horarioAlmoco = horario

        print("\nSaída para almoço registrada")

    def registrar_volta_almoco(self, horario):

        self.__horarioVoltaAlmoco = horario

        print("\nVolta do almoço registrada")

    def exibir_funcionario(self):

        self.exibir_dados()

        print(f"Cargo: {self.__cargo}")
        print(f"Setor: {self.__setor}")

        print(f"Data Cadastro: {self.__dataCadastro}")

        print(f"Entrada: {self.__horarioEntrada}")
        print(f"Saída Almoço: {self.__horarioAlmoco}")
        print(f"Volta Almoço: {self.__horarioVoltaAlmoco}")
        print(f"Saída Final: {self.__horarioSaida}")