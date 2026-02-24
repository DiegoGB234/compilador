import tkinter as tk
from tkinter import scrolledtext
import sys
import io

import AnalizadorLexico as lexico
import AnalizadorSintactico as sintatico


#Primero obtendremos los tokens y verficar si lo que ser resive de las expresiones regualres se encuentren n los tokes que definimos



## RUN CODE
def ejecutar_codigo():
    codigo = area_codigo.get("1.0", tk.END)

    consola.delete("1.0", tk.END)

    # Capturar salida
    salida = io.StringIO()
    sys.stdout = salida

    try:
        ## Ejecutar el código ingresado
        anali_lexico = lexico.AnalizadorLexico(codigo)
        tokes=anali_lexico.analizar()

        # ahoora apartir de los tokens que tenenemos  aplicacmos el analicis sintatico 
        anali_sintatico = sintatico.AnalizadorSintactico(tokes)
        anali_sintatico.analizar()
        ##exec(codigo)

    except Exception as e:
        print("Error:", e)

    sys.stdout = sys.__stdout__
    consola.insert(tk.END, salida.getvalue())


# -----------------------------
# VENTANA PRINCIPAL
# -----------------------------
ventana = tk.Tk()
ventana.title("Compilador TTT")
ventana.geometry("800x600")

# -----------------------------
# AREA DE CODIGO
# -----------------------------
label_codigo = tk.Label(ventana, text="Código Fuente")
label_codigo.pack()

area_codigo = scrolledtext.ScrolledText(
    ventana,
    height=15,
    font=("Consolas", 12)
)
area_codigo.pack(fill="both", expand=True, padx=10, pady=5)

# -----------------------------
# BOTON EJECUTAR
# -----------------------------
btn_ejecutar = tk.Button(
    ventana,
    text="Ejecutar",
    command=ejecutar_codigo,
    bg="green",
    fg="white",
    font=("Arial", 12)
)
btn_ejecutar.pack(pady=5)


label_consola = tk.Label(ventana, text="Salida / Consola")
label_consola.pack()

consola = scrolledtext.ScrolledText(
    ventana,
    height=10,
    bg="black",
    fg="lime",
    font=("Consolas", 11)
)
consola.pack(fill="both", expand=True, padx=10, pady=5)

ventana.mainloop()
