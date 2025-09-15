import tkinter as tk
from tkinter import messagebox

# Función para agregar tarea
def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea.strip() != "":
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Por favor, ingresa una tarea.")

# Función para limpiar todas las tareas
def limpiar_tareas():
    lista_tareas.delete(0, tk.END)
    entrada_tarea.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Tareas")
ventana.geometry("400x400")
ventana.resizable(False, False)

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingresa una nueva tarea:")
etiqueta.pack(pady=10)

# Campo de texto
entrada_tarea = tk.Entry(ventana, width=40)
entrada_tarea.pack(pady=5)

# Botón Agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_tarea)
boton_agregar.pack(pady=5)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, width=50, height=10)
lista_tareas.pack(pady=10)

# Botón Limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_tareas)
boton_limpiar.pack(pady=5)

# Ejecutar aplicación
ventana.mainloop()
