class NodoNumero:
    def __init__(self, valor):
        self.valor = valor

    def __repr__(self):
        return f"Numero({self.valor})"
class NodoString:
    def __init__(self, valor):
        self.valor = valor
    def __repr__(self):
        return f"NodoString({self.valor})"

class NodoOperacion:
    def __init__(self, izquierda, operador, derecha):
        self.izquierda = izquierda
        self.operador = operador
        self.derecha = derecha

    def __repr__(self):
        return f"Operacion({self.izquierda} {self.operador} {self.derecha})"


class NodoDeclaracion:
    def __init__(self, tipo, variable, valor):
        self.tipo = tipo
        self.variable = variable
        self.valor = valor

    def __repr__(self):
        return f"Declaracion(tipo={self.tipo}, var={self.variable}, valor={self.valor})"
