#este file nos permitira ejecuttar las otras partes
import AnalizadorLexico as lexico
import AnalizadorSintactico as sintatico


#Primero obtendremos los tokens y verficar si lo que ser resive de las expresiones regualres se encuentren n los tokes que definimos
anali_lexico = lexico.AnalizadorLexico("12/2")
tokes=anali_lexico.analizar()
# ahoora apartir de los tokens que tenenemos  aplicacmos el analicis sintatico 
anali_sintatico = sintatico.AnalizadorSintactico(tokes)
anali_sintatico.analizar()