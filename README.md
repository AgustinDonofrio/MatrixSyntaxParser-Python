
# MatrixSyntaxParser-Python

## Descripción

Este proyecto implementa un **analizador sintáctico** en Python para validar expresiones de matrices con subíndices en un lenguaje específico. El analizador verifica que el nombre de la matriz y los subíndices cumplan con un conjunto de reglas establecidas.

Una expresión de matriz válida tiene el siguiente formato:


### Reglas de Validación

1. **Nombre de la matriz:**
   - Debe comenzar con una letra.
   - Puede incluir letras, dígitos y guiones bajos (`_`), 
   - Los guiones bajos sólo pueden ir seguidos al final.
   
2. **Subíndices (sub1 y sub2):**
   - Si el nombre de la matriz termina con un número par de guiones bajos, entonces los subíndices tienen la característica del nombre de la matriz (letras, dígitos y guiones bajos) .
   - Caso contrario (cantidad impar de guiones bajos), entonces los subíndices deben ser números enteros positivos sin signo.

## Ejemplos de expresiones

- **Válidas:**
  - `Matriz1[var1,var2]`
  - `M1_ab_c[x1,x2]`
  - `M4tr1z_A__[10,20]`

- **Inválidas:**
  - `1Matriz[var1,var2]`  → El nombre no comienza con letra.
  - `Matriz__X[ab,cd]`  → Los guiones bajos solo pueden ir seguidos al final del nombre.
  - `M123___[10,abc]`  → El subíndice 2 no cumplen con las reglas según el número de guiones bajos.

## Instalación y Ejecución

Para ejecutar el analizador, es necesario de tener **Python 3.x** instalado. Clona este repositorio y ejecuta el script de la siguiente manera:

```bash
git clone https://github.com/tu_usuario/MatrixSyntaxParser-Python.git
cd MatrixSyntaxParser-Python
python matrix_analyzer.py
```
