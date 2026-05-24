

from pessoa import Pessoa

class Visitante(Pessoa):

    def __init__(self, nome, cpf, identificacao, email,
                 empresaVisitada, validadeID, limiteAcessos):

        super().__init__(nome, cpf, identificacao, email)

        self.__empresaVisitada = empresaVisitada
        self.__validadeID = validadeID

        self.__horaEntrada = ""
        self.__horaSaida = ""

        self.__contadorAcessos = 5
        self.__limiteAcessos = limiteAcessos


    def get_empresaVisitada(self):
        return self.__empresaVisitada

    def get_validadeID(self):
        return self.__validadeID

    def get_horaEntrada(self):
        return self.__horaEntrada

    def get_horaSaida(self):
        return self.__horaSaida

    def get_contadorAcessos(self):
        return self.__contadorAcessos

    def get_limiteAcessos(self):
        return self.__limiteAcessos


    def set_empresaVisitada(self, empresaVisitada):
        self.__empresaVisitada = empresaVisitada

    def set_validadeID(self, validadeID):
        self.__validadeID = validadeID

    def set_horaEntrada(self, horaEntrada):
        self.__horaEntrada = horaEntrada

    def set_horaSaida(self, horaSaida):
        self.__horaSaida = horaSaida


    def registrar_entrada(self, horario):

        if self.__contadorAcessos < self.__limiteAcessos:

            self.__horaEntrada = horario
            self.__contadorAcessos += 1

            print("\nEntrada registrada com sucesso")

        else:
            print("\nLimite de acessos atingido")


    def registrar_saida(self, horario):

        self.__horaSaida = horario

        print("\nSaída registrada com sucesso")


    def validar_horario(self, hora):

        if hora >= 8 and hora <= 18:
            return True

        return False


    def exibir_visitante(self):

        self.exibir_dados()

        print(f"Empresa Visitada: {self.__empresaVisitada}")
        print(f"Validade ID: {self.__validadeID}")
        print(f"Hora Entrada: {self.__horaEntrada}")
        print(f"Hora Saída: {self.__horaSaida}")
        print(f"Acessos usados: {self.__contadorAcessos}")
