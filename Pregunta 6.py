# La edad del cliente
edad = int(input("¿Cuántos años tiene el cliente? "))
# Precio de la entrada según la edad
if edad < 4:
    precio_entrada = 0
elif 4 <= edad <= 18:
    precio_entrada = 5
else:
    precio_entrada = 10
# Mostrar el precio de la entrada
print(f"El precio de la entrada es: ${precio_entrada}")