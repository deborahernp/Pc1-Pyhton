def invertir_lista(lista_original):
    # Usamos el método .reverse() para invertir la lista original
    lista_invertida = lista_original.copy()
    lista_invertida.reverse()
    return lista_invertida
# Ejemplo de uso
lista_original = ['Di', 'buen', 'día', 'a', 'papa']
lista_resultante = invertir_lista(lista_original)
print("Lista original:", lista_original)
print("Lista invertida:", lista_resultante)