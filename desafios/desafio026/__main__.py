from rich import inspect
from funcionarios import *

def main():
    f1 = FuncionarioMensalista( "Jose da silva", 8500)
    f2 = FuncionarioHorista( "Maria de Souza", 25, 250)
    f1.calcular_salario()
    f2.calcular_salario()
    f2.analisar_salario()
    #inspect(f1)
