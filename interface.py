import tkinter as tk

def create_interface():
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

    label_tittle = tk.Label(window, text="RUST INTERPRETER\nGRUPO 1 LENGUAJES DE PROGRAMACIÓN\n\BASURTOS SERGIO\nMACIAS RAMON", justify="left", font=("Arial", 14, "bold"), border=1, bg="lightblue")
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

    text_sintaxis = tk.Text(window, state="disabled", width=75, height=15)
    text_sintaxis.grid(row=2, column=1)

    buttom_run = tk.Button (window, text="RUN", justify="left")
    buttom_run.grid(row=3, column=0, columnspan=2, padx=20)

    label_output = tk.Label(window, text="OUTPUT: ", justify="left", bg="lightblue",font=("Arial", 11, "bold"))
    label_output.grid (row=3, column=0, sticky="w")
    # Sección del último cuadro de texto deshabilitado
    text_output = tk.Text(window, state="disabled", width=150, height=8)
    text_output.grid(row=4, columnspan=3)

    # Ejecutar la interfaz
    window.mainloop()