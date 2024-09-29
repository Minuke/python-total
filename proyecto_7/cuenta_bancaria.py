from os import system

class Persona:
  
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido
    
class Cliente(Persona):
  def __init__(self, nombre, apellido, numero_cuenta, balance):
    super().__init__(nombre, apellido)
    self.numero_cuenta = numero_cuenta
    self.balance = balance
    
  def __str__(self):
    return print(f"El cliente {self.nombre} {self.apellido} con numero de cuenta {self.numero_cuenta} tiene un balance de {self.balance} euros")
    
  def depositar(self, ingreso):
    self.balance += ingreso
    return print(f"Has ingresado {ingreso} y tu nuevo balanace es de {self.balance} euros")
    
  def retirar(self, retiro):
    nuevo_balance = int(self.balance - retiro)
    if nuevo_balance >= 0:
      self.balance = nuevo_balance
      return print(f"Has retirado {retiro} y tu nuevo balanace es de {self.balance} euros")
    else:
      return print(f"No dispone del saldo suficiente para realizar un retiro de {retiro} euros. Su saldo es de {self.balance} euros")

def crear_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")
    balance = int(input("Ingrese el balance que deseas ingresar en tu cuenta inicialmente: "))
    cliente = Cliente(nombre, apellido, numero_cuenta, balance)
    return cliente

def inicio():
  print("*"*50)
  print("Bienvenido a tu cuenta bancaria")
  print("*"*50)
  
  menu = "x"
  while not menu.isnumeric() or int(menu) not in range(1, 4):
    print("[1] - Depositar dinero\n[2] - Retirar dinero\n[3] - Salir""")
    menu = input("Elige una opcion: ")
  return int(menu)

finalizar_programa = False
cliente = crear_cliente()
while not finalizar_programa:
  menu = inicio()
  
  if menu == 1:
    ingreso = int(input("¿Cuánto dinero quieres ingresar?: "))
    cliente.depositar(ingreso)
  elif menu == 2:
    retiro = int(input("¿Cuánto dinero quieres retirar?: "))
    cliente.retirar(retiro)
  elif menu == 3:
    finalizar_programa = True