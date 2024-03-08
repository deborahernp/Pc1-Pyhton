# ¿Que hora es? Coloque una hora en formato HH:MM
hora = input("Ingrese una hora en formato HH:MM (24 horas): ")
# Extraer las horas y minutos de la entrada del usuario
try:
    horas, minutos = map(int, hora.split(":"))
except ValueError:
    print("Formato de hora incorrecto. Debe ser HH:MM.")
    exit()
# Verificar si la hora está dentro de los rangos de comidas
if 7 <= horas < 8:
    print("Es hora de desayunar.")
elif 12 <= horas < 13:
    print("Es hora de almorzar.")
elif 18 <= horas < 19:
    print("Es hora de cenar.")
else:
    print("No es hora de comer.")