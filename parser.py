# El objetivo del analizador es intentar aplicar las reglas de la gramática a partir de S y consumir completamente la cadena de entrada.

# Cada no terminal de la gramática se implementó como una función. Estas funciones:
    # Consumen caracteres de la cadena de entrada si coinciden con lo esperado.
    # Llaman recursivamente a otras funciones si encuentran un no terminal.
    # Retornan True o False para indicar si la regla se cumple para la cadena actual.

class Error:
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message




class Parser:
    def __init__(self, input_string):
        self.input_string = input_string
        self.index = 0  # Para rastrear la posición actual en la cadena


    def handleErrorMatrizName(self):
        actual_char = self.current_char()
        if self.Let() or self.Dig():
            return Error('No pueden venir letras y digitos despues de guiones seguidos')
        if(self.current_char() == ']' or self.current_char() == ','):
            return Error(f'No puede haber "{actual_char}" despues de guiones seguidos')
        return Error(f'El caracter "{actual_char}" no esta en el alfabeto')
    
    def handleErrorID(self):
        actual_char = self.current_char()
        if actual_char == ']':
            return Error('No puede cerrar con "]", todavia no definio los dos sub-íncides')
        if self.Let() or self.Dig():
            return Error(f'No pueden haber "{actual_char}" después de guiones seguidos')
        if(actual_char == ','):
            return Error(f'No pueden haber dos "," dentro de la declaracion')
        if actual_char == '[':
            return Error('La declaración de la matriz ya fué abierta')
        return Error(f'El caracter "{actual_char}" no está en el alfabeto')
    

    def current_char(self):
        # Devuelve el carácter actual o None si se alcanzó el final
        return self.input_string[self.index] if self.index < len(self.input_string) else None

    def consume(self):
        # Avanza al siguiente carácter
        if self.index < len(self.input_string):
            self.index += 1

    def parse(self):
        # Punto de entrada para el análisis
        result = self.S()
        if isinstance(result, Error):  # Si es un error, lo devolvemos
            return result
        # Verificamos si se consumió toda la cadena
        if self.index == len(self.input_string):
            return True
        return Error("La cadena no se consumió completamente.")

    # Producciones de la gramática
    def S(self):
        if self.Let():
            return self.A()
        return Error("La cadena debe comenzar con una letra.")

    def A(self):
        char = self.current_char()
        if self.Let() or self.Dig():
            return self.A()
        elif char == '_':
            self.consume()
            return self.B()
        elif char == '[':
            self.consume()
            return self.X()
        else:
            return Error(f"El caracter {char} no esta en el alfabeto")

    def B(self):
        char = self.current_char()
        if self.Let() or self.Dig():
            return self.A()
        elif char == '_':
            self.consume()
            return self.C()
        elif char == '[':
            self.consume()
            return self.E()
        else:
            return Error(f"El caracter {char} no esta en el alfabeto")

    def C(self):
        char = self.current_char()
        if char == '_':
            self.consume()
            return self.D()
        elif char == '[':
            self.consume()
            return self.X()
        return self.handleErrorMatrizName()

    def D(self):
        char = self.current_char()
        if char == '_':
            self.consume()
            return self.C()
        elif char == '[':
            self.consume()
            return self.E()
        return self.handleErrorMatrizName()


    def E(self):
        if self.Dig():
            return self.F()
        return self.handleErrorID()

    def F(self):
        char = self.current_char()
        if self.Dig():
            return self.F()
        elif char == ',':
            self.consume()
            return self.G()
        return Error(f'En caso impar, solo puede venir una "," o dígitos')

    def G(self):
        if self.Dig():
            return self.H()
        return self.handleErrorID()

    def H(self):
        char = self.current_char()
        if self.Dig():
            return self.H()
        elif char == ']':
            self.consume()
            return self.P()
        return self.handleErrorID()

    def X(self):
        if self.Let():
            return self.J()
        return Error("Caso par, la definicion de los sub-índices debe seguir el mísmo patrón que el nombre de la matriz")

    def J(self):
        char = self.current_char()
        if self.Let() or self.Dig():
            return self.J()
        elif char == '_':
            self.consume()
            return self.K()
        elif char == ',':
            self.consume()
            return self.M()
        return self.handleErrorID()

    def K(self):
        char = self.current_char()
        if self.Let() or self.Dig():
            return self.J()
        elif char == '_':
            self.consume()
            return self.L()
        elif char == ',':
            self.consume()
            return self.M()
        return self.handleErrorID()

    def L(self):
        char = self.current_char()
        if char == '_':
            self.consume()
            return self.L()
        elif char == ',':
            self.consume()
            return self.M()
        return self.handleErrorID()

    def M(self):
        if self.Let():
            return self.N()
        return self.handleErrorID()

    def N(self):
        char = self.current_char()
        if self.Let() or self.Dig():
            return self.N()
        elif char == '_':
            self.consume()
            return self.Ñ()
        elif char == ']':
            self.consume()
            return self.P()
        return self.handleErrorID()

    def Ñ(self):
        char = self.current_char()
        if self.Let() or self.Dig():
            return self.N()
        elif char == '_':
            self.consume()
            return self.O()
        elif char == ']':
            self.consume()
            return self.P()
        return self.handleErrorID()

    def O(self):
        char = self.current_char()
        if char == '_':
            self.consume()
            return self.O()
        elif char == ']':
            self.consume()
            return self.P()
        return self.handleErrorID()

    def P(self):
        return True  # 𝜆 significa vacío

    # Funciones para terminales
    def Let(self):
        # Devuelve True si el carácter actual es una letra (a-z, A-Z)
        char = self.current_char()
        if char and char.isalpha():
            self.consume()
            return True

    def Dig(self):
        # Devuelve True si el carácter actual es un dígito (0-9)
        char = self.current_char()
        if char and char.isdigit():
            self.consume()
            return True
        return False

# Pruebas
if __name__ == "__main__":
    test_strings = [
        "l?t_dig_[123,456]",      # Cadena inválida
        "let_dig_[123,456]",      # Cadena válida
        "abc123[a1,a2]",          # Cadena válida
        "a1_[123,123]",           # Cadena válida
        "a1__[a1_,a1_]",          # Cadena válida      
        "_123",                   # Cadena inválida
        "let[[123_456]]",         # Cadena inválida
        "leta__,_[111,111]",      # Cadena inválida
        "l1l1l_1__[1,111]",       # Cadena inválida
        "l1l1l_1__[aa__a,aa_]",   # Cadena inválida
        "l1l1l_1__[aa__,a,a_]",   # Cadena inválida
        "a1_[12[3,123]",          # Cadena inválida
        "a1_[1"                   # Cadena inválida
    ]
    for s in test_strings:
        parser = Parser(s)
        result = parser.parse()
        if isinstance(result, Error):  # Si es un error, mostramos su mensaje
            print(f"'{s}': Cadena inválida - {result}")
        else:  # Si no, validamos la cadena como antes
            print(f"'{s}': {'Cadena válida' if result else 'Cadena inválida'}")
