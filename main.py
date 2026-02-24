# main.py
import AnalizadorLexico as lexico
import AnalizadorSintactico as sintatico
import AnalizadorSematico as semantico

anali_lexico = lexico.AnalizadorLexico("string sexo = 'Me vengo'")
tokens = anali_lexico.analizar()
print("Tokens:", tokens)

anali_sintatico = sintatico.AnalizadorSintactico(tokens)
ast = anali_sintatico.analicis()
print("\nAST:", ast)

anali_semantico = semantico.AnalizadorSemantico()
anali_semantico.analizar(ast)
