from pessoa import Pessoa

class Funcionario (Pessoa):
    def __init__(self, nome, cpf, identificacao, email, cargo, setor):
        super().__init__(nome, cpf , identificacao, email)
        
        self.__cargo =  cargo
        self.__setor =  setor
        
        self.__horarioEntrada = ""
        self.__horarioSaida = ""
        
        self.__horarioAlmoco = ""
        self.__horarioVoltaAlmoco = ""
        
        
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
        
        
        
    def set_cargo(self, cargo):
        self.__cargo = cargo
        
        
    def set_setor(self, setor):
        self.__setor = setor
        
    def get_horarioEntrada(self, horarioEntrada):
        self.__horarioEntrada = horario
        
    def get_chorarioSaida(self, horarioSaida):
        self.__horarioSaida = horario
        
    def get_horarioAlmoco(self, horarioAlmoco):
        self.__horarioAlmoco = horario
        
    def get_horarioVoltaAlmoco(self, horarioVoltaAlmoco):
        self.__horarioVoltaAlmoco = horario
        
        
        
    def registrar_entrada(self, horario):
        self.__horarioEntrada = horario
        print(f"\nRegistro com sucesso")
        
    def registrar_saida(self, horario):
        self.__horarioSaida = horario
        print(f"\nRegistro com sucesso")
        
    def registrar_saida_almoco(self, horario):
        self.__horarioAlmoco = horario
        print(f"\nRegistro com sucesso")
        
    def registrar_volta_almoco(self, horario):
        self.__horarioVoltaAlmoco = horario
        print(f"\nRegistro com sucesso")
        
    def exibir_funcionario(self):
        self.exibir_dados()
        
        print(f"Cargo: ", self.__cargo)
        print(f"Setor: ", self.__setor)
        
        print(f"Entarda: ", self.__horarioEntrada)
        print(f"Saida do Almoço: ", self.__horarioAlmoco)
        print(f"Volta do Almoço: ", self.__horarioVoltaAlmoco)
        print(f"Saida:",self.__horarioSaida)
    
        