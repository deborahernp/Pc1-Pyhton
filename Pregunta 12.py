#Mencionar el nombre del archiva tal como aparece en la ruta (Ejemplo: MANUAL DE INGIENIERIA MI 25.pdf)
def obtener_tipo_mime(nombre_archivo):
    # Definir un diccionario con extensiones y tipos MIME correspondientes
    tipos_mime = {
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'zip': 'application/zip'
    }
    # Obtener la extensión del archivo (ignorando mayúsculas y minúsculas)
    extension = nombre_archivo.lower().split('.')[-1]
    # Verificar si la extensión está en el diccionario
    tipo_mime = tipos_mime.get(extension, 'application/octet-stream')
    return tipo_mime
# Solicitar al usuario el nombre del archivo
nombre_archivo = input("Ingrese el nombre del archivo: ")
# Obtener y mostrar el tipo MIME correspondiente
tipo_mime = obtener_tipo_mime(nombre_archivo)
print(f"El tipo MIME para el archivo {nombre_archivo} es: {tipo_mime}")