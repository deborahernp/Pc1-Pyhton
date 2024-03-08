# Pedir al usuario la cantidad de shows musicales vistos en el último año
cantidad_shows = int(input("¿Cuántos shows musicales has visto en el último año? "))
# Verificar si ha visto más de 3 shows
Mas_de_3 = cantidad_shows > 3
# Mostrar el resultado
print(f"¿Has visto más de 3 shows? {Mas_de_3}")
