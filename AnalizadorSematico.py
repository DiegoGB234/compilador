# AnalizadorSemantico.py
from AST import NodoNumero, NodoOperacion, NodoDeclaracion,NodoString

class AnalizadorSemantico:
    def __init__(self):
        self.tabla_simbolos = {}  # guarda variables declaradas

    def analizar(self, nodo):
        if isinstance(nodo, NodoDeclaracion):
            return self.analizar_declaracion(nodo)

        elif isinstance(nodo, NodoOperacion):
            return self.analizar_operacion(nodo)

        elif isinstance(nodo, NodoNumero):
            return self.analizar_numero(nodo)
        elif isinstance(nodo,NodoString):
            return self.abnalizar_cadena(nodo)
        else:
            raise Exception(f"Nodo desconocido: {nodo}")

    def analizar_declaracion(self, nodo):
        # verificamos que la variable no este declarada ya
        if nodo.variable in self.tabla_simbolos:
            raise Exception(f"Error semántico: la variable '{nodo.variable}' ya fue declarada")

        valor = self.analizar(nodo.valor)

        # verificamos que el tipo coincida
        if nodo.tipo == 'int' and not isinstance(valor, (int, float)):
            raise Exception(f"Error semántico: se esperaba un número pero se obtuvo '{valor}'")
        if nodo.tipo == 'string' and not isinstance(valor, str):
            raise Exception(f"Error semántico: se esperaba un string pero se obtuvo '{valor}'")

        # guardamos en la tabla de simbolos
        self.tabla_simbolos[nodo.variable] = {
            'tipo': nodo.tipo,
            'valor': valor
        }

        print(f"Variable '{nodo.variable}' declarada como '{nodo.tipo}' con valor '{valor}'")
        print(f"Tabla de símbolos: {self.tabla_simbolos}")
        return valor

    def analizar_operacion(self, nodo):
        izq = self.analizar(nodo.izquierda)
        der = self.analizar(nodo.derecha)

        # verificamos division entre cero
        if nodo.operador == '/' and der == 0:
            raise Exception("Error semántico: división entre cero")

        # aplicamos la operacion real
        if nodo.operador == '+':
            return izq + der
        elif nodo.operador == '-':
            return izq - der
        elif nodo.operador == '*':
            return izq * der
        elif nodo.operador == '/':
            return izq / der

    def analizar_numero(self, nodo):
        return int(nodo.valor)
    def abnalizar_cadena(self,nodo):
        return str(nodo.valor)