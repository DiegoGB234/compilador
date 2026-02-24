# AnalizadorLexico.py
import re

class AnalizadorLexico:
    def __init__(self, expresion: str):
        self.expresion = expresion
        self.tokens = []
        self.patrones = [
            ("NUMERO",         r'\d+'),
            ("CADENA",         r"'[^']*'"),
            ("OP",             r'int|string'),
            ("VAR",            r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ("SUMA",           r'\+'),
            ("RESTA",          r'-'),
            ("MULT",           r'\*'),
            ("DIV",            r'/'),
            ("IGUAL",          r'\='),
            ("PARENTESIS_IZQ", r'\('),
            ("PARENTESIS_DER", r'\)'),
            ("ESPACIO",        r'\s+'),
        ]

    def analizar(self):
        texto = self.expresion
        posicion = 0
        while posicion < len(texto):
            coincide = None
            for tipo, patron in self.patrones:
                expresion_regular = re.compile(patron)
                coincide = expresion_regular.match(texto, posicion)
                if coincide:
                    valor = coincide.group(0)
                    if tipo != 'ESPACIO':
                        self.tokens.append({"TOKEN": tipo, "LEXEMA": valor})
                    posicion = coincide.end()
                    break
            if not coincide:
                raise SyntaxError(f"Error lexicon. simbolo no encontrado {texto[posicion]}")

        return self.tokens