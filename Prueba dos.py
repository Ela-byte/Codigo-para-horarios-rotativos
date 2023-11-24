import tkinter as tk
from tkinter import ttk
import datetime
import random

# Lista de nombres de las personas
nombres = ["Andres", "Moises", "Jose", "Irak", "Daniela", "Eduardo", "Fabian", "Miguel", "Evelin"]

# Lista de horarios
horarios = [["7:00", "16:00"], ["9:00", "18:00"], ["11:00", "20:00"], ["15:00", "23:00"]]

# Días de la semana
dias = ["Lunes     ",         "Martes    ",         "Miércoles ",         "Jueves    ",         "Viernes   ",         "Sábado    ",         "Domingo   "]

def generar_horario():
  # Generamos un número aleatorio entre 0 y 3
  horario = random.randint(0, 3)
  return horarios[horario]

def generar_horario_persona(nombre):
  # Generamos un horario aleatorio para cada día de la semana
  horarios = []
  for dia in dias:
    horario = generar_horario()
    horarios.append(horario)
  return horarios
#Generacion de los datos
horarios_personas = []
for nombre in nombres:
  horarios_persona = generar_horario_persona(nombre)
  horarios_personas.append(horarios_persona)
#Impresion de los datos 
for nombre, horarios in zip(nombres, horarios_personas):
  print(f">>    |     Nombre:    |    >> {nombre}")
  for dia, horario in zip(dias, horarios):
    print(f">>    |     Día       :|    >>{dia} |     |     Horario   :|    <<  {horario[0]} - {horario[1]}")

#Comando de entrada para el acomodo de tablas con un interfaz GIU

# Crear la ventana
ventana = tk.Tk()
ventana.title("Horarios de las personas")

# Crear el marco principal
marco_principal = ttk.Frame(ventana, padding="20")
marco_principal.grid()

# Crear la etiqueta de título
etiqueta_titulo = ttk.Label(marco_principal, text="Horarios de las personas")
etiqueta_titulo.grid(columnspan=len(dias)+1)

# Crear las etiquetas de los días
for i, dia in enumerate(dias):
    etiqueta_dia = ttk.Label(marco_principal, text=dia)
    etiqueta_dia.grid(row=1, column=i+1)

# Crear las etiquetas de nombres y horarios
for i, nombre in enumerate(nombres):
    etiqueta_nombre = ttk.Label(marco_principal, text=nombre)
    etiqueta_nombre.grid(row=i+2, column=0)

    for j, horario in enumerate(horarios_personas[i]):
        etiqueta_horario = ttk.Label(marco_principal, text=f"{horario[0]} - {horario[1]}")
        etiqueta_horario.grid(row=i+2, column=j+1)

# Ajustar el tamaño de las columnas
marco_principal.grid_columnconfigure(0, weight=1)
for i in range(len(dias)):
    marco_principal.grid_columnconfigure(i+1, weight=1)

# Ajustar el tamaño de las filas
for i in range(len(nombres)+1):
    marco_principal.grid_rowconfigure(i, weight=1)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()