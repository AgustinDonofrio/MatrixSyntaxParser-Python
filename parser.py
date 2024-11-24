# El programa necesita analizar y validar cadenas que siguen el patrón de una matriz con subíndices.
# Vamos a diseñar el analizador para este patrón. NombreMatriz[sub1, sub2]

# Reglas que debemos implementar:
    # 'NombreMatriz' 
        # Empieza con una letra y puede ir seguido de letras, digitos y guiones bajos.
        # Los guiones bajos sólo pueden ir seguidos al final

    # Sub-índices 'sub1, sub2'
        # Si el 'NombreMatriz' termina con un número par de giones bajos 
        #   => los sub-índices tienen las mismas caracteristicas que 'NombreMatriz'
        # Si no => los sub-índices son numeros enteros positivos sin signo

import re

def analizar_matriz(cadena):
    # Expresión regular para capturar el nombre de la matriz y los subíndices entre corchetes
    patron_matriz = r'^([a-zA-Z][a-zA-Z0-9_]*)(?:\[(.*),(.*)\])?$'
    coincidencia = re.match(patron_matriz, cadena)
    
    if not coincidencia:
        return "Error: Formato inválido"

    nombre_matriz, sub1, sub2 = coincidencia.groups()

    # Validación del nombre de la matriz (debe comenzar con letra y guiones bajos solo al final)
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', nombre_matriz):
        return "Error: Nombre de la matriz inválido"

    if "__" in nombre_matriz[:-2] or (nombre_matriz.endswith('_') and nombre_matriz[-2] == '_'):
        return "Error: Los guiones bajos solo pueden aparecer al final del nombre"

    # Determinar el número de guiones bajos al final
    num_guiones_bajos = len(nombre_matriz) - len(nombre_matriz.rstrip('_'))
    
    # Reglas para subíndices
    if num_guiones_bajos % 2 == 0:  # Si termina con un número par de guiones bajos
        sub_patron = r'^[a-zA-Z][a-zA-Z0-9_]*$'  # Subíndices similares al nombre de matriz
    else:  # Si termina con un número impar de guiones bajos
        sub_patron = r'^\d+$'  # Subíndices deben ser números enteros positivos sin signo

    # Validar sub1 y sub2 si existen
    if sub1 and not re.match(sub_patron, sub1):
        return "Error: Subíndice 1 inválido"
    if sub2 and not re.match(sub_patron, sub2):
        return "Error: Subíndice 2 inválido"

    return "Matriz válida"

# Ejemplos de uso
ejemplos = [
    "Matriz1[3,5]",
    "Matriz__",    # Termina con dos guiones bajos
    "Matriz__5[foo,bar]",
    "Matriz_[2,3]",
    "Matriz_[cad_,12]",
]

for ej in ejemplos:
    print(f"{ej}: {analizar_matriz(ej)}")