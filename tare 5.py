print("Menu Restaurante")

print("Panes:")
print("1. Frances: $2.000")
print("2. Rollo: $3.000")

print("Frito:")
print("1. Empanada: $5.000")

print("Comida")
print("1. Hamburguesa: $20.000")

print("Bebidas")
print("1. Limonada: $2.000")
print("2. Cerveza: $4.000")

#Matriz de datos del menu
#Columna 0: ID Producto
#Columna 1: Nombre producto
#Columna 2: Categoria
#Columna 3: Precio

DATOS_MENU = [
  ["R1","Frances","Pan",2000],
  ["R2","Rollo","Pan",3000],
  ["R3","Empanada","Frito",5000],
  ["R4","Hamburguesa","Comida",20000],
  ["R5","Limonada","Bebida",2000],
  ["R6","Cerveza","Bebida",4000]
]

categoria_objetivo = "Comida"
umbral = 10000
descuento = 0.15

for producto in DATOS_MENU:
  print(producto)

  nombre = producto[1]
  categoria = producto[2]
  precio = producto[3]
  
  if categoria == categoria_objetivo and precio > umbral:
    precio_final = precio - (precio * descuento)
    print("Descuento aplicado")
  
  else:
    precio_final = precio
    print("Sin descuento")
  
  print(nombre)
  print("Precio original:", precio)
  print("Precio final:", precio_final)

  print("------------------")
  print("Producto:", nombre)
  print("Categoria:", categoria)
  print("Precio original:", precio)
  print("Precio final:", precio_final)
  