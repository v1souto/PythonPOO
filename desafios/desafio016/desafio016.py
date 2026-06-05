from rich import print
from rich import inspect

class Funcionario:
    # Atributor de classe
    empresa = "Curso em Video"

    def __init__(self, nome, setor, cargo):
        #Atributor de instância
            self.nome = nome
            self.setor = setor
            self.cargo = cargo

    def apresentacao(self) -> str:
        return f":handshake: Olá, sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa}"


# Funcionario.empresa = "Hostnet"
c1 = Funcionario("Maria", "Administração", "Diretora")
c1.empresa = "Estudonauta"
print(c1.empresa)
print(c1.apresentacao())
#inspect(c1)
c2 = Funcionario("Predro", "TI", "Programador")
print(c2.apresentacao())
#inspect(c2)
#inspect(Funcionario)
