import tkinter as tk
from tkinter import ttk
from game_with_visual import Duelos, Caracter, Personaje, Enemigo

duelos = Duelos()

def buscar_por_id():
    try:
        id_val = int(entry_id.get())
        temp = Caracter(id_val, 0.0)
        resultado = duelos.search_caracter(temp)
        resultado_label.config(text=resultado)
    except ValueError:
        resultado_label.config(text="ID inválido")

def realizar_duelo_ui():
    try:
        id1 = int(entry_duelo1.get())
        id2 = int(entry_duelo2.get())

        c1 = next((c for c in duelos.caracteres if c.id == id1), None)
        c2 = next((c for c in duelos.caracteres if c.id == id2), None)

        if not c1 or not c2:
            resultado_duelo.config(text="Uno o ambos caracteres no encontrados")
            return

        resultado = duelos.realizar_duelo(c1, c2)
        resultado_duelo.config(text=resultado)
    except Exception as e:
        resultado_duelo.config(text=str(e))

def maldad_vs_potencia_ui():
    resultado = duelos.maldadvspotencia()
    texto = "Maldad es MAYOR que potencia" if resultado else "Potencia es MAYOR o igual que maldad"
    resultado_comparacion.config(text=texto)

def registrar_caracter():
    try:
        id_val = int(entry_id_new.get())
        energia = float(entry_energia_new.get())
        ofensiva = int(entry_ofensiva_new.get())
        vidas = int(entry_vidas_new.get())

        tipo = tipo_var.get()

        if tipo == "Personaje":
            magia = int(entry_magia.get())
            potencia = float(entry_potencia.get())
            nuevo = Personaje(magia, id_val, energia)
            nuevo.set_factor_potencia(potencia)
        else:
            maldad = int(entry_maldad.get())
            nuevo = Enemigo(maldad, id_val, energia)

        nuevo.set_capacidad_ofenciva(ofensiva)
        nuevo.set_numero_vida(vidas)

        duelos.add_caracter(nuevo)
        resultado_comparacion.config(text=f"{tipo} con ID {id_val} registrado.")
        actualizar_treeview()
    except Exception as e:
        resultado_comparacion.config(text=f"Error: {str(e)}")

def actualizar_campos(*args):
    tipo = tipo_var.get()
    if tipo == "Personaje":
        entry_magia.config(state="normal")
        entry_potencia.config(state="normal")
        entry_maldad.config(state="disabled")
    else:
        entry_magia.config(state="disabled")
        entry_potencia.config(state="disabled")
        entry_maldad.config(state="normal")

def actualizar_treeview():
    treeview.delete(*treeview.get_children())
    for c in duelos.caracteres:
        tipo = "Personaje" if isinstance(c, Personaje) else "Enemigo"
        treeview.insert("", "end", values=(c.id, tipo, c.n_energia, c.numero_vida, c.capacidad_ofenciva))

root = tk.Tk()
root.title("Juego de Estrategia - Visual Interface")
root.geometry("1200x450")

frame_contenedor = ttk.Frame(root)
frame_contenedor.pack(fill="both", expand=True, padx=10, pady=5)
frame_contenedor.columnconfigure(1, weight=1)
frame_contenedor.rowconfigure(0, weight=1)


# Insercion de jugadores
frame_registro = ttk.LabelFrame(frame_contenedor, text="Registrar Carácter")
frame_registro.grid(row=0, column=0, sticky="n", padx=10, pady=5)

ttk.Label(frame_registro, text="Tipo:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
tipo_var = tk.StringVar(value="Personaje")
tipo_selector = ttk.Combobox(frame_registro, textvariable=tipo_var, values=["Personaje", "Enemigo"], state="readonly", width=15)
tipo_selector.grid(row=0, column=1, padx=5, pady=2)
tipo_var.trace_add('write', actualizar_campos)

labels = ["ID", "Energía", "Ofensiva", "Vidas", "Magia", "Potencia", "Maldad"]
entries = []

for i, label in enumerate(labels, start=1):
    ttk.Label(frame_registro, text=f"{label}:").grid(row=i, column=0, sticky="w", padx=5, pady=2)
    entry = ttk.Entry(frame_registro, width=15)
    entry.grid(row=i, column=1, padx=5, pady=2)
    entries.append(entry)

entry_id_new, entry_energia_new, entry_ofensiva_new, entry_vidas_new, entry_magia, entry_potencia, entry_maldad = entries

btn_registrar = ttk.Button(frame_registro, text="Registrar", command=registrar_caracter)
btn_registrar.grid(row=8, column=0, columnspan=2, pady=10)

actualizar_campos()

# panel de busquedas
frame_busqueda = ttk.LabelFrame(root, text="Buscar carácter por ID")
frame_busqueda.pack(fill="x", padx=10, pady=5)

entry_id = ttk.Entry(frame_busqueda)
entry_id.pack(side="left", padx=5)

btn_buscar = ttk.Button(frame_busqueda, text="Buscar", command=buscar_por_id)
btn_buscar.pack(side="left", padx=5)

resultado_label = ttk.Label(frame_busqueda, text="")
resultado_label.pack(side="left", padx=10)

# Panel de duelos
frame_duelos = ttk.LabelFrame(root, text="Realizar Duelo")
frame_duelos.pack(fill="x", padx=10, pady=5)

entry_duelo1 = ttk.Entry(frame_duelos, width=10)
entry_duelo1.pack(side="left", padx=5)
entry_duelo2 = ttk.Entry(frame_duelos, width=10)
entry_duelo2.pack(side="left", padx=5)

btn_duelo = ttk.Button(frame_duelos, text="Duelo!", command=realizar_duelo_ui)
btn_duelo.pack(side="left", padx=5)

resultado_duelo = ttk.Label(frame_duelos, text="")
resultado_duelo.pack(side="left", padx=10)

# Maldad vs Potencia
frame_comparacion = ttk.LabelFrame(root, text="Comparación")
frame_comparacion.pack(fill="x", padx=10, pady=5)

btn_comparar = ttk.Button(frame_comparacion, text="Verificar Malicia vs Potencia", command=maldad_vs_potencia_ui)
btn_comparar.pack(side="left", padx=5)

resultado_comparacion = ttk.Label(frame_comparacion, text="")
resultado_comparacion.pack(side="left", padx=10)


frame_lista = ttk.LabelFrame(frame_contenedor, text="Carácteres Registrados")
frame_lista.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)

treeview = ttk.Treeview(frame_lista, columns=("ID", "Tipo", "Energía", "Vidas", "Ofensiva"), show="headings", height=10)
treeview.pack(fill="both", expand=True)

# Cabeceras
for col in ("ID", "Tipo", "Energía", "Vidas", "Ofensiva"):
    treeview.heading(col, text=col)
    treeview.column(col, anchor="center")
    
root.mainloop()

