# Solicitar al usuario que ingrese dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
# Mostrar el menú de opciones
print("Menú:")
print("1. Mostrar suma de los dos números")
print("2. Mostrar resta de los dos números")
print("3. Mostrar multiplicación de los dos números")
# Solicitar al usuario que elija una opción
opcion = int(input("Seleccione una opción (1/2/3): "))
# Calcular y mostrar el resultado según la opción elegida
if opcion == 1:
    resultado = numero1 + numero2
    print(f"La suma es: {resultado}")
elif opcion == 2:
    resultado = numero1 - numero2
    print(f"La resta es: {resultado}")
elif opcion == 3:
    resultado = numero1 * numero2
    print(f"La multiplicación es: {resultado}")
else:
    print("Opción inválida. Por favor, elija una opción válida (1/2/3).")