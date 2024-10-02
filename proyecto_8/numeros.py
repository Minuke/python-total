def numeros_perfumeria():
  n = 1
  while True:
    yield f"P - {n}"
    n += 1
    
def numeros_farmacia():
  n = 1
  while True:
    yield f"F - {n}"
    n += 1
    
def numeros_cosmetica():
  n = 1
  while True:
    yield f"C - {n}"
    n += 1
    

p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()

def decorador(rubro):
  print("\n" + "*" * 23)
  print("Su numero es: ")
  if rubro == "P":
    print(next(p))
  elif rubro == "F":
    print(next(f))
  else:
    print(next(c))
  print("Aguarde y sera atendido")
  print("*" * 23 + "\n")