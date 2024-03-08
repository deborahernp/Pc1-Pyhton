# Monto del consumo en el restaurante
monto_consumo = float(input("Ingresa el monto del consumo en la comida: "))

# Porcentaje de propina deseado
porcentaje_propina = float(input("Porcentaje de propina que desea dejar: "))

# Calcular la cantidad de propina
propina = (monto_consumo * porcentaje_propina) / 100

# Mostrar la cantidad de dinero a dejar como propina
print(f"Debes dejar ${propina:.2f} como propina al mozo.")