def eliminar_duplicados(lista_original):
    # Usamos un conjunto para eliminar duplicados
    conjunto_sin_duplicados = set(lista_original)
    lista_resultante = list(conjunto_sin_duplicados)
    return lista_resultante

# Lista original
lista_original = [1, 1, 2, 3, 4, 4, 5, 1]

# Obtener la lista procesada
lista_procesada = eliminar_duplicados(lista_original)

# Imprimir el resultado
print("Lista procesada:", lista_procesada)