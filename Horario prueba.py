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

horarios_personas = []
for nombre in nombres:
  horarios_persona = generar_horario_persona(nombre)
  horarios_personas.append(horarios_persona)




for nombre, horarios in zip(nombres, horarios_personas):
  print(f">>    |     Nombre:    |    >> {nombre}")
  for dia, horario in zip(dias, horarios):
    print(f">>    |     Día       :|    >>{dia} |     |     Horario   :|    <<  {horario[0]} - {horario[1]}")