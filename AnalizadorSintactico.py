class AnalizadorSintactico:

    def __init__(self, tokens):
        self.tokens = tokens
        self.posicion= 0
      

    # para consultar en que token esta
    def actual(self):
        if self.posicion < len(self.tokens):
            return self.tokens[self.posicion]
        return None
    # por idndeificar que cada parantesis tenga su )
    def consumir(self, tipo):
        token = self.actual()
        if token and token['TOKEN'] == tipo:
            self.posicion += 1
            return token
        raise SyntaxError(f"Se esperaba {tipo}")

    # expresiones de +  Y -
    def expresion(self):
        resultado = self.termino()

        while self.actual() and self.actual()['TOKEN'] in ('SUMA','RESTA','DIV'):
            operador = self.actual()['TOKEN']
            self.posicion += 1
            valor = self.termino()

            if operador == 'SUMA':
                resultado += valor
            elif operador == 'RESTA':
                resultado -= valor
            else :
                resultado /= valor

        return resultado

    # termino para ver si es una multi o la miltimi de ()
    def termino(self):
        resultado = self.factor()

        while self.actual() and self.actual()['TOKEN'] == 'MULT':
            self.posicion += 1
            valor = self.factor()
            resultado *= valor

        return resultado

    # si ees numero o expresiopnm
    def factor(self):
        token = self.actual()

        if token['TOKEN'] == 'NUMERO':
            self.posicion += 1
            return int(token['LEXEMA'])

        elif token['TOKEN'] == 'PARENTESIS_IZQ':
            self.posicion += 1
            resultado = self.expresion()
            self.consumir('PARENTESIS_DER')
            return resultado

        else:
            raise SyntaxError("Factor inválido")

    def analizar(self):
        resultado = self.expresion()

        if self.posicion != len(self.tokens):
            raise SyntaxError("Expresión mal formada")

        print("Resultado:", resultado)
        return resultado