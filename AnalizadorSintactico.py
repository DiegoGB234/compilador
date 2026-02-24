
from AST import NodoNumero, NodoOperacion, NodoDeclaracion

class AnalizadorSintactico:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def token_actual(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consumir(self, tipo_esperado):
        token = self.token_actual()
        if token and token['TOKEN'] == tipo_esperado:
            self.pos += 1
            return token['LEXEMA']
        else:
            raise SyntaxError(f"Se esperaba '{tipo_esperado}' pero se encontró '{token}'")

    def analicis(self):
        return self.declaracion()

    def declaracion(self):
        tipo     = self.consumir('OP')
        variable = self.consumir('VAR')
        self.consumir('IGUAL')
        valor = self.expresion()
        return NodoDeclaracion(tipo, variable, valor)  # ← retorna nodo

    def expresion(self):
        izq = self.termino()
        while self.token_actual() and self.token_actual()['TOKEN'] in ('SUMA', 'RESTA'):
            op = self.token_actual()['LEXEMA']
            self.pos += 1
            der = self.termino()
            izq = NodoOperacion(izq, op, der)  # ← retorna nodo
        return izq

    def termino(self):
        izq = self.factor()
        while self.token_actual() and self.token_actual()['TOKEN'] in ('MULT', 'DIV'):
            op = self.token_actual()['LEXEMA']
            self.pos += 1
            der = self.factor()
            izq = NodoOperacion(izq, op, der)  # ← retorna nodo
        return izq

    def factor(self):
        token = self.token_actual()
        if token is None:
            raise SyntaxError("Se esperaba un valor pero se llegó al final")

        if token['TOKEN'] == 'NUMERO':
            self.pos += 1
            return NodoNumero(token['LEXEMA'])  # ← retorna nodo

        elif token['TOKEN'] == 'PARENTESIS_IZQ':
            self.pos += 1
            valor = self.expresion()
            self.consumir('PARENTESIS_DER')
            return valor

        else:
            raise SyntaxError(f"Se esperaba un número o '(' pero se encontró '{token}'")