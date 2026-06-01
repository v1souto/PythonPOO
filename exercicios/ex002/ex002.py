class Gafanhoto:
    """
    Essa classe cira um gafanhoto que é uma pessoa que tem nome e  idade

    Para criar uma nova pessoa, use
    variavel = gafanhoto(nome, idade)
    """
    def __init__(self, nome = "Vazio", idade = 0):
        # Atributos de instancia
        self.nome = nome
        self.idade = idade

    # Metodos de instancia
    def aniversario(self):
        self.idade = self.idade + 1


    def __str__(self): #Dunder Method
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"estado: nome = {self.nome} ; idade = {self.idade}"


# Declaracao de objetos
g1 = Gafanhoto(nome = "Maria", idade = 17)
g1.aniversario()
#print(g1)
print(g1.__dict__) # Attribute
print(g1.__getstate__()) # Method
print(g1.__class__)
print(g1.__doc__) #Dunder Attribute




