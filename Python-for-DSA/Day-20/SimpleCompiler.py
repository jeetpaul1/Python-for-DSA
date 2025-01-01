#Implement a Python program to parse and evaluate arithmetic expressions using a custom compiler. The program should handle addition, subtraction, multiplication, and division, including parenthetical expressions.


class SimpleCompiler: #solution
    def __init__(self, expression):
        self.expression = expression
        self.position = 0

    def _peek(self):
        """Return the current character without advancing."""
        if self.position < len(self.expression):
            return self.expression[self.position]
        return None

    def _advance(self):
        """Advance to the next character."""
        self.position += 1

    def _consume_whitespace(self):
        """Skip over any whitespace."""
        while self._peek() and self._peek().isspace():
            self._advance()

    def parse_number(self):
        """Parse a number from the expression."""
        start = self.position
        while self._peek() and self._peek().isdigit():
            self._advance()
        return int(self.expression[start:self.position])

    def parse_factor(self):
        """Parse a factor (a number or parenthetical expression)."""
        self._consume_whitespace()
        if self._peek() == '(':
            self._advance()  # Skip '('
            value = self.parse_expression()
            self._advance()  # Skip ')'
            return value
        else:
            return self.parse_number()

    def parse_term(self):
        """Parse a term (handles multiplication and division)."""
        value = self.parse_factor()
        while self._peek() in ('*', '/'):
            operator = self._peek()
            self._advance()
            if operator == '*':
                value *= self.parse_factor()
            elif operator == '/':
                value /= self.parse_factor()
        return value

    def parse_expression(self):
        """Parse an expression (handles addition and subtraction)."""
        value = self.parse_term()
        while self._peek() in ('+', '-'):
            operator = self._peek()
            self._advance()
            if operator == '+':
                value += self.parse_term()
            elif operator == '-':
                value -= self.parse_term()
        return value

    def evaluate(self):
        """Evaluate the expression."""
        return self.parse_expression()


# Example usage
expression = "3 + 5 * (2 - 8) / 2"
compiler = SimpleCompiler(expression)
result = compiler.evaluate()

print(f"Expression: {expression}")
print(f"Result: {result}")
