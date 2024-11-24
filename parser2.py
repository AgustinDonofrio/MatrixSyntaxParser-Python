# El objetivo del analizador es intentar aplicar las reglas de la gramática a partir de S y consumir completamente la cadena de entrada.

# Cada no terminal de la gramática se implementó como una función. Estas funciones:
    # Consumen caracteres de la cadena de entrada si coinciden con lo esperado.
    # Llaman recursivamente a otras funciones si encuentran un no terminal.
    # Retornan True o False para indicar si la regla se cumple para la cadena actual.


class Parser:
    def __init__(self, input_string):
        self.input_string = input_string
        self.index = 0  # Para rastrear la posición actual en la cadena

    def current_char(self):
        # Devuelve el carácter actual o None si se alcanzó el final
        return self.input_string[self.index] if self.index < len(self.input_string) else None

    def consume(self):
        # Avanza al siguiente carácter
        if self.index < len(self.input_string):
            self.index += 1

    def parse(self):
        # Punto de entrada para el análisis
        return self.S() and self.index == len(self.input_string)

    # Producciones de la gramática
    def S(self):
        if self.Let():
            return self.A()
        return False

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
        return False

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
        return False

    def C(self):
        char = self.current_char()
        if char == '_':
            self.consume()
            return self.D()
        elif char == '[':
            self.consume()
            return self.X()
        return False

    def D(self):
        char = self.current_char()
        if char == '_':
            self.consume()
            return self.C()
        elif char == '[':
            self.consume()
            return self.E()
        return False

    def E(self):
        if self.Dig():
            return self.F()
        return False

    def F(self):
        char = self.current_char()
        if self.Dig():
            return self.F()
        elif char == ',':
            self.consume()
            return self.G()
        return True  # Permitir vacío

    def G(self):
        if self.Dig():
            return self.H()
        return False

    def H(self):
        char = self.current_char()
        if self.Dig():
            return self.H()
        elif char == ']':
            self.consume()
            return self.P()
        return False

    def X(self):
        if self.Let():
            return self.J()
        return False

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
        return False

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
        return False

    def L(self):
        char = self.current_char()
        if char == '_':
            self.consume()
            return self.L()
        elif char == ',':
            self.consume()
            return self.M()
        return False

    def M(self):
        if self.Let():
            return self.N()
        return False

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
        return False

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
        return False

    def O(self):
        char = self.current_char()
        if char == '_':
            self.consume()
            return self.O()
        elif char == ']':
            self.consume()
            return self.P()
        return False

    def P(self):
        return True  # 𝜆 significa vacío

    # Funciones para terminales
    def Let(self):
        # Devuelve True si el carácter actual es una letra (a-z, A-Z)
        char = self.current_char()
        if char and char.isalpha():
            self.consume()
            return True
        return False

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
        "let_dig_[123,456]",  # Cadena válida
        "abc123[a1,a2]",       # Cadena válida
        "a1_[123]",             # Cadena válida
        "_123",                 # Cadena inválida
        "let[[123_456]]",       # Cadena inválida
    ]
    for s in test_strings:
        parser = Parser(s)
        print(f"'{s}': {'Cadena válida' if parser.parse() else 'Cadena inválida'}")
