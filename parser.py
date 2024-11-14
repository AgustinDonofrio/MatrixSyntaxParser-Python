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

