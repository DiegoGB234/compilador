# main.py
import AnalizadorLexico as lexico
import AnalizadorSintactico as sintatico
import AnalizadorSematico as semantico

anali_lexico = lexico.AnalizadorLexico("int miVariable2 = 12+2*(12/4)")
tokens = anali_lexico.analizar()
print("Tokens:", tokens)

anali_sintatico = sintatico.AnalizadorSintactico(tokens)
ast = anali_sintatico.analicis()
print("\nAST:", ast)

anali_semantico = semantico.AnalizadorSemantico()
anali_semantico.analizar(ast)
