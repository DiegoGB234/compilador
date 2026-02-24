import re

class AnalizadorLexico:
    
    def __init__(self, expresion: str):
        self.expresion = expresion
        self.tokens = []
        
        # definifoms la expresiones reguarales
        self.patrones = [
            ("NUMERO", r'\d+'),
            ("SUMA", r'\+'),
            ("RESTA", r'-'),
            ("MULT", r'\*'),
            ("DIV", r'/'),
            ("PARENTESIS_IZQ", r'\('),
            ("PARENTESIS_DER", r'\)'),
            ("ESPACIO", r'\s+'),
            ("")
        ]

    def analizar(self):
        texto = self.expresion
        posicion=0
        while posicion < len(texto):
            for tipo, patron  in self.patrones:
                #obtenesmo ñas expresiones regularares que estan en una cadema cruda y los converiutmos en un objecto
                expresion_regulares= re.compile(patron)
                # paraa ver si conicide al inicio con las expresionde regulares y agregamos la poscione paara iterar o pasar al siguioente
                coincide= expresion_regulares.match(texto,posicion)
                if coincide:
                    # para mostrar los que conincidio
                    valor= coincide.group(0)
                    #ignoramos los espacion
                    if tipo != 'ESPACIO':
                        #lo agregamos en los tokens y 
                        self.tokens.append({"TOKEN": tipo, "LEXEMA": valor})
                    # obetneidop el ultimo indice
                    posicion= coincide.end()
                    break
            if not coincide:
                raise SyntaxError(f"Error lexcion. simbolo no encontrado {texto[posicion]}")

        return self.tokens
    
