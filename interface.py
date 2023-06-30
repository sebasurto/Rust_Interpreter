import tkinter as tk
from lex import reserved
import lex as lxc
import sintaxis as sntx


def create_interface():
    def print_text ():
        texto = text_your_code.get("1.0", tk.END)
        lexic = lxc.test_lex(texto)
        sintax = sntx.test_sintaxis(texto)
        # Limpiar el contenido actual
        text_sintaxis.config(state=tk.NORMAL)
        text_sintaxis.delete("1.0", tk.END) 
        text_sintaxis.insert(tk.END, f"Sintaxis:\n {sintax}\n")
        text_sintaxis.config(state=tk.DISABLED)
        text_lex.config(state=tk.NORMAL)
        text_lex.delete("1.0", tk.END) 
        text_lex.insert(tk.END, f"Lexic:\n {lexic}\n")
        text_lex.config(state=tk.DISABLED)
    window = tk.Tk()
    window.title("Rust Interpreter")
    window.iconbitmap("media\\rust_ico.ico")
    window.config(bg="lightblue")

    # Sección del logo y título
    logo = tk.PhotoImage(file="media\\rust_logo.PNG")  # Reemplaza "ruta_del_logo.png" por la ruta de tu propio logo
    new_width = 200  # Ajusta el ancho deseado
    new_height = 200  # Ajusta el alto deseado
    logo_redimensionado = logo.subsample(int(logo.width() / new_width), int(logo.height() / new_height))

    label_logo = tk.Label(window, image=logo_redimensionado, bg="lightblue")
    label_logo.grid(row=0, column=0)

    label_tittle = tk.Label(window, text="RUST INTERPRETER\nGRUPO 1 LENGUAJES DE PROGRAMACIÓN\nBASURTO SERGIO\nMACIAS RAMON", justify="left", font=("Arial", 14, "bold"), border=1, bg="lightblue")
    label_tittle.grid (row=0, column=1, sticky="w")

    #label_titulo2 = tk.Label(window, text="Grupo 1 lenguajes de programación")
    #label_titulo2.grid (row=0, column=1)
    label_your_code = tk.Label(window, text="YOUR CODE", justify="center",font=("Arial", 11, "bold"), relief="solid")
    label_your_code.grid (row=1, column=0,sticky="nsew")

    label_sintaxis = tk.Label(window, text="SINTAXIS", justify="center",font=("Arial", 11, "bold"), relief="solid")
    label_sintaxis.grid (row=1, column=1, sticky="nsew")
    # Sección de los cuadros de texto

    
    text_your_code = tk.Text(window, state="normal", width=75, height=15)
    text_your_code.grid(row=2, column=0)

    

    #posiciones_reservadas = {}

    for word in reserved.keys():
        text_your_code.tag_configure(word, foreground="blue")

    def resaltar_palabras_reservadas(event):
        for word in reserved.keys():
            posicion = "1.0"  # Inicio del texto
            while True:
                # Buscar la siguiente aparición de la palabra reservada
                posicion = text_your_code.search(word, posicion, stopindex=tk.END, exact=True)
                if not posicion:
                    break
                # Verificar que la palabra encontrada es una palabra completa
                posicion_final = f"{posicion}+{len(word)}c"
                if not posicion_final.endswith((" ", "\n", ".", ",", ";", ":", "!", "?", ")", "]", "}")):
                    posicion = posicion_final
                    continue
                # Aplicar etiqueta de estilo a la palabra reservada encontrada
                text_your_code.tag_add(word, posicion, posicion_final)
                # Actualizar posición para buscar la siguiente aparición
                posicion = posicion_final

# Enlazar evento de teclado para resaltar las palabras reservadas
    text_your_code.bind("<KeyRelease>", resaltar_palabras_reservadas)
    
    text_sintaxis = tk.Text(window, state="disabled", width=75, height=15)
    text_sintaxis.grid(row=2, column=1)

    buttom_run = tk.Button (window, text="RUN", justify="left", command=print_text)
    buttom_run.grid(row=3, column=0, columnspan=2, padx=20)

    label_output = tk.Label(window, text="LEX: ", justify="left", bg="lightblue",font=("Arial", 11, "bold"))
    label_output.grid (row=3, column=0, sticky="w")
    # Sección del último cuadro de texto deshabilitado
    text_lex = tk.Text(window, state="disabled", width=150, height=8)
    text_lex.grid(row=4, columnspan=3)

    # Ejecutar la interfaz
    window.mainloop()
