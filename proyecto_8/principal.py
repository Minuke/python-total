import numeros

def preguntar():
  print("Bienvenido a FarmaPython")
  
  while True:
    print("[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmetica""")
    try:
      rubro = input("Elija su rubro: ").upper()
      ["P", "F", "C"].index(rubro)
    except ValueError:
      print("Esa no es una opcion valida")
    else:
      break
  
  numeros.decorador(rubro)
  
def inicio():
  while True:
    preguntar()
    try:
      otro_turno = input("¿Quieres sacar otro turno? [S] [N]: ").upper()
      ["S", "N"].index(otro_turno)
    except ValueError:
      print("Esa no es una opcion valida")
    else:
      if otro_turno == "N":
        print("Gracias por su visita")
        break

inicio()