def eliminar_elementos(lista_original):
    # Eliminar elementos en las posiciones 0, 4 y 5
    indices_a_eliminar = [0, 4, 5]
    for indice in sorted(indices_a_eliminar, reverse=True):
        del lista_original[indice]


    return lista_original
# Lista de muestra (ejemplo propio)
lista_muestra = ['Gallina', 'Vaca', 'Caballo', 'Cerdo', 'Oveja', 'Pato']
# Obtener la lista resultante
lista_resultante = eliminar_elementos(lista_muestra)
# Imprimir el resultado
print("Resultado esperado:", lista_resultante)