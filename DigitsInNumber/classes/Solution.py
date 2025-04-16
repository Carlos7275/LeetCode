class Solution:
    def digitsInNumber(self, number: float) -> int:
        """
        Cuenta el número total de dígitos en un número flotante,
        incluyendo los de la parte entera y decimal.

        Args:
            number (float): El número flotante del cual se contarán los dígitos.

        Returns:
            int: El total de dígitos en la parte entera y decimal del número.
        """
        # Contar dígitos de la parte entera
        integer_part = int(number)
        digits_integer = 0 if integer_part == 0 else 0
        
        while integer_part > 0:
            integer_part //= 10
            digits_integer += 1

        # Contar dígitos de la parte decimal
        decimal_part = number - int(number)  # Extraemos la parte decimal
        digits_decimal = 0

        while decimal_part > 0:
            decimal_part *= 10
            decimal_digit = int(decimal_part)
            decimal_part -= decimal_digit
            decimal_part = round(decimal_part, 10)
            digits_decimal += 1

        return digits_integer + digits_decimal
