class Pessoa:
    def __init__(self, nome,cpf , identificacao, email):
        self.__nome = nome
        self.__cpf = cpf
        self.__identificacao =  identificacao
        self.__email = email
        self.__ativo = True
        

        
    def get_nome(self):
        return self.__nome
        
    def get_cpf(self):
        return self.__cpf
        
    def get_identificacao(self):
        return self.__identificacao
        
    def get_email(self):
        return self.__email
        
    def get_ativo(self):
        return self.__ativo
        

    
    def set_nome(self, nome):
        self.__nome = nome
        
    def set_cpf(self, cpf):
        self.__cpf = cpf
        
    def set_identificacao(self, identificacao):
        self.__identificacao = identificacao
        
    def set_email(self, email):
        self.__email
        if self.validar_email(email):
            self.__email = email
        
    def set_ativo(self, ativo):
        self.__ativo = ativo

    
    def exibir_dados(self):
        print(f"    DADOS DA PESSOA     ")
        print(f"\nNome: {self.get_nome()}")
        print(f"\nCPF: {self.get_cpf()}")
        print(f"ID: {self.get_identificacao()}")
        print(f"E-mail: {self.get_email()}")
        
        if self.get_ativo:
            print(f"Status : ATIVO")
        else: 
            print(f"Status : INATIVO")
            
            
    def validar_cpf(self):
        if len(self.__cpf) == 11 and self.__cpf.isdigit():
            return True
        return False
        
        
    def validar_email(self, email):
        if "@" in email and ".com" in email:
            return True
        return False

    
