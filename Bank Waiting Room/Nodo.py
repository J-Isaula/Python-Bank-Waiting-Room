class Nodo:
    def __init__(self, n, padre):
        self.valor = n
        self.raiz = padre
        self.hijos = {}
