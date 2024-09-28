from pathlib import Path
from os import system
import os

ruta = Path.cwd() / "Proyecto_6" / "Recetas"
total_recetas = len(list(ruta.glob("**/*.txt")))

def inicio():
  system("cls")
  print("*"*50)
  print("Bienvenido al administrador de tareas")
  print("*"*50)
  print(f"\nTus recetas están en el directorio: {ruta}\nTotal de recetas: {total_recetas}\n")
  menu = "x"
  while not menu.isnumeric() or int(menu) not in range(1, 7):
    print("[1] - Leer receta\n[2] - Crear receta\n[3] - Crear categoria\n[4] - Eliminar receta\n[5] - Eliminar categoria\n[6] - Finalizar programa""")
    menu = input("Elige una opcion: ")
  return int(menu)

def mostrar_categorias(ruta):
  print("Categorias:")
  ruta_categorias = Path(ruta)
  lista_categorias = []
  contador = 1
  
  for carpeta in ruta_categorias.iterdir():
    carpeta_str = str(carpeta.name)
    print(f"[{contador}] - {carpeta_str}")
    lista_categorias.append(carpeta)
    contador += 1
  
  return lista_categorias

def elegir_categoria(categorias):
  categoria = "x"
  while not categoria.isnumeric() or int(categoria) not in range(1, len(categorias) + 1):
    categoria = input("\nElige una categoria: ")
    
  return categorias[int(categoria) -1]

def mostrar_recetas(ruta):
  print("Recetas:")
  ruta_recetas = Path(ruta)
  lista_recetas = []
  contador = 1
  
  for receta in ruta_recetas.glob("*.txt"):
    receta_str = str(receta.name)
    print(f"[{contador}] - {receta_str}")
    lista_recetas.append(receta)
    contador += 1
  
  return lista_recetas

def elegir_receta(recetas):
  receta = "x"
  while not receta.isnumeric() or int(receta) not in range(1, len(recetas) + 1):
    receta = input("\nElige una receta: ")
    
  return recetas[int(receta) -1]

def leer_receta(receta):
  print(Path.read_text(receta))

def crear_receta(ruta):
  existe = False
  
  while not existe:
    print("Escribe el nombre de tu receta: ")
    nombre_receta = input() + ".txt"
    print("Escribe tu nueva receta: ")
    contenido_receta = input()
    ruta_nueva = Path(ruta, nombre_receta)
    
    if not os.path.exists(ruta_nueva):
      Path.write_text(ruta_nueva, contenido_receta)
      print(f"Tu receta {nombre_receta} ha sido creada")
      existe = True
    else:
      print("Lo siento, esa receta ya existe")
    
def crear_categoria(ruta):
  existe = False
  
  while not existe:
    print("Escribe el nombre de la nueva categoria: ")
    nombre_categoria = input()
    print(ruta)
    ruta_nueva = Path(ruta, nombre_categoria)
    print(ruta_nueva)
    if not os.path.exists(ruta_nueva):
      ruta_nueva.mkdir()
      print(f"Tu nueva categoria {nombre_categoria} ha sido creada")
      existe = True
    else:
      print("Lo siento, esa categoria ya existe")

def eliminar_receta(receta):
  Path(receta).unlink()
  print(f"La receta {receta.name} ha sido eliminada")

def eliminar_categoria(categoria):
  Path(categoria).rmdir()
  print(f"La categoria {categoria.name} ha sio eliminada")

def volver_inicio():
  eleccion_regresar = "x"
  
  while eleccion_regresar.lower() != "v":
    eleccion_regresar = input("\nPresione 'V' para volver al inicio: ")

finalizar_programa = False
while not finalizar_programa:
  menu = inicio()

  if menu == 1:
    categorias = mostrar_categorias(ruta)
    categoria = elegir_categoria(categorias)
    recetas = mostrar_recetas(categoria)
    if len(recetas) < 1:
      print("No hay recetas en esta categoria")
    else:
      receta = elegir_receta(recetas)
      leer_receta(receta)
    volver_inicio()
  elif menu == 2:
    categorias = mostrar_categorias(ruta)
    categoria = elegir_categoria(categorias)
    crear_receta(categoria)
    volver_inicio()
  elif menu == 3:
    crear_categoria(ruta)
    volver_inicio()
  elif menu == 4:
    categorias = mostrar_categorias(ruta)
    categoria = elegir_categoria(categorias)
    recetas = mostrar_recetas(categoria)
    if len(recetas) < 1:
      print("No hay recetas en esta categoria")
    else:
      receta = elegir_receta(recetas)
      eliminar_receta(receta)
    volver_inicio()
  elif menu == 5:
    categorias = mostrar_categorias(ruta)
    categoria = elegir_categoria(categorias)
    eliminar_categoria(categoria)
    volver_inicio()
  elif menu == 6:
    finalizar_programa = True