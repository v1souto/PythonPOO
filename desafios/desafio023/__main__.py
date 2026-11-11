from rich import print, inspect
from poligono import Quadrado, Circulo

def main():
    q = Quadrado(20)
    #inspect9(q, methods=True)
    print(f"um quadrado de lado {q.lado}cm tem perimetro de {q.perimetro()}cm")
    print(f"Um quadrado de lado {q.lado}cm tem area de {q.area()}cm2")


    c = Circulo(12)
    print(f"Um circulo de raio {c.raio}cm tem perimetro de {c.perimetro():.1f}cm")
    print(f"Um circulo de raio {c.raio}cm tem area de {c.area():1f}cm2")

if __name__ == "__main__":
    main()
