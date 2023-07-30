from colr import Colr as colr
from time import sleep as sleep


class Colors:
    def red(self):
        print(colr().hex("#ff0000", self, rgb_mode=True))

    def rose(self):
        print(colr().hex("#ff0066", self, rgb_mode=True))

    def green(self):
        print(colr().hex("#00ff8d", self, rgb_mode=True))

    def gnome_green(self):
        print(colr().hex("#2ed1b4", self, rgb_mode=True))

    def dark_orange(self):
        print(colr().hex("#cf301b", self, rgb_mode=True))

    def light_gnome(self):
        print(colr().hex("#00ffc4", self, rgb_mode=True))

    def yellow_green(self):
        print(colr().hex("#7ed666", self, rgb_mode=True))

    def violet(self):
        print(colr().hex("#cc33ff", self, rgb_mode=True))

    def light_green(self):
        print(colr().hex("#21ff00", self, rgb_mode=True))

    def orange(self):
        print(colr().hex("#ff8e35", self, rgb_mode=True))

    def yellow(self):
        print(colr().hex("#fff300", self, rgb_mode=True))

    def sky_blue(self):
        print(colr().hex("#00ccff", self, rgb_mode=True))

    def blue(self):
        print(colr().hex("#0000ff", self, rgb_mode=True))

    def cream(self):
        print(colr().hex("#ff9999", self, rgb_mode=True))

    def dark_rose(self):
        print(colr().hex("#cc0066", self, rgb_mode=True))

    def dark_red(self):
        print(colr().hex("#cc0000", self, rgb_mode=True))

    def dark_green(self):
        print(colr().hex("#009933", self, rgb_mode=True))

    def light_blue(self):
        print(colr().hex("#6666ff", self, rgb_mode=True))


class Style:
    null = ""
    dash = null.center(58, "-")


class Operator:
    def exit():
        Colors.red("\n     You exited")

    def invalid():
        print(
            colr().hex(
                "#ff8e35",
                """                        (__) 
                        (oo) 
                  /------\/ 
                 / |    ||   
                *  /\---/\ 
                   ~~   ~~   
            """,
                rgb_mode=True,
            ),
            colr().hex("#ff0000", "...invalid input...", rgb_mode=True),
        )


class Methods:
    def octal_binary():
        null = ""
        dash = null.center(58, "-")
        Colors.light_blue("\n     Enter decimal number: ")
        octal = input(colr().hex("#ff0000", "\n     > ", rgb_mode=True))
        try:
            octal_digits = list(map(int, str(octal)))
            binary_digits = [format(digit, "03b") for digit in octal_digits]
            binary_result = "".join(binary_digits)
            Colors.light_blue("\n" + "     " + dash)
            binary = f"      ({binary_result})2"
            Colors.red(f"{binary.center(60)}")
            Colors.light_blue("     " + dash)
        except ValueError:
            Colors.light_blue("\n" + "     " + dash)
            error = "      Error: Invalid octal input!"
            Colors.red(f"{error.center(60)}")
            Colors.light_blue("     " + dash)

    def decimal_to_octal():
        null = ""
        dash = null.center(58, "-")
        Colors.light_blue("\n     Enter decimal number: ")
        decimal_number = input(colr().hex("#ff0000", "\n     > ", rgb_mode=True))
        show_decimal = decimal_number
        try:
            decimal_number = int(decimal_number)
            if decimal_number == 0:
                Colors.red(
                    "0"  # Special case for input 0, as its octal representation is also 0
                )

            octal_digits = []
            while decimal_number > 0:
                quotient, remainder = divmod(decimal_number, 8)
                octal_digits.insert(
                    0, str(remainder)
                )  # Insert the remainder at the beginning of the list
                decimal_number = quotient

            octal_result = "".join(octal_digits)
            Colors.light_blue("\n" + "     " + dash)
            octal = f"      ({octal_result})8"
            Colors.red(f"{octal.center(60)}")
            Colors.light_blue("     " + dash)
        except ValueError:
            Colors.light_blue("\n" + "     " + dash)
            error = "Error: Invalid decimal input!"
            Colors.red(f"{error.center(60)}")
            Colors.light_blue("     " + dash)

    def decimal_to_binary():
        null = ""
        dash = null.center(58, "-")
        Colors.light_blue("\n     Enter decimal number: ")
        decimal_number = input(colr().hex("#ff0000", "\n     > ", rgb_mode=True))
        decimal_number = int(decimal_number)
        try:
            if decimal_number == 0:
                Colors.red(
                    "0"  # Special case for input 0, as its octal representation is also 0
                )
            binary_digits = []
            while decimal_number > 0:
                quotient, remainder = divmod(decimal_number, 2)
                binary_digits.insert(
                    0, str(remainder)
                )  # Insert the remainder at the beginning of the list
                decimal_number = quotient

            binary_result = "".join(binary_digits)
            Colors.light_blue("\n" + "     " + dash)
            binary = f"      ({binary_result})2"
            Colors.red(f"{binary.center(60)}")
            Colors.light_blue("     " + dash)
        except ValueError:
            Colors.light_blue("\n" + "     " + dash)
            error = "Error: Invalid decimal input!"
            Colors.red(f"{error.center(60)}")
            Colors.light_blue("     " + dash)

    def binary_to_decimal():
        null = ""
        dash = null.center(58, "-")
        Colors.light_blue("\n     Enter decimal number: ")
        binary_number = input(colr().hex("#ff0000", "\n     > ", rgb_mode=True))
        try:
            decimal_number = 0

            # Iterate over the binary digits in reverse order
            for i, bit in enumerate(reversed(binary_number)):
                if bit == "1":
                    decimal_number += 2**i

            decimal_result = str(decimal_number)
            Colors.light_blue("\n" + "     " + dash)
            decimal = f"      ({decimal_result})2"
            Colors.red(f"{decimal.center(60)}")
            Colors.light_blue("     " + dash)
        except ValueError:
            Colors.light_blue("\n" + "     " + dash)
            error = "Error: Invalid binary input!"
            Colors.red(f"{error.center(60)}")
            Colors.light_blue("     " + dash)

    def decimal_to_hexadecimal():
        null = ""
        dash = null.center(58, "-")
        Colors.light_blue("\n     Enter decimal number: ")
        decimal_number = input(colr().hex("#ff0000", "\n     > ", rgb_mode=True))
        try:
            decimal_number = int(decimal_number)
            if decimal_number == 0:
                Colors.red(
                    "0"  # Special case for input 0, as its octal representation is also 0
                )
            hex_digits = "0123456789ABCDEF"
            hexadecimal_string = ""

            while decimal_number > 0:
                remainder = decimal_number % 16
                hexadecimal_string = hex_digits[remainder] + hexadecimal_string
                decimal_number //= 16
            Colors.light_blue("\n" + "     " + dash)
            hexadecimal = f"      ({hexadecimal_string})16"
            Colors.red(f"{hexadecimal.center(60)}")
            Colors.light_blue("     " + dash)
        except ValueError:
            Colors.light_blue("\n" + "     " + dash)
            error = "Error: Invalid decimal input!"
            Colors.red(f"{error.center(60)}")
            Colors.light_blue("     " + dash)

    def hex_to_binary():
        null = ""
        dash = null.center(58, "-")
        Colors.light_blue("\n     Enter hexadecimal number: ")
        hex_string = input(colr().hex("#ff0000", "\n     > ", rgb_mode=True))
        hex_string = hex_string.upper()
        try:
            hex_digits = "0123456789ABCDEF"
            binary_digits = [
                bin(hex_digits.index(digit))[2:].zfill(4) for digit in hex_string
            ]
            binary_string = "".join(binary_digits)
            Colors.light_blue("\n" + "     " + dash)
            binary = f"      ({binary_string})2"
            Colors.red(f"{binary.center(60)}")
            Colors.light_blue("     " + dash)
        except ValueError:
            Colors.light_blue("\n" + "     " + dash)
            error = "Error: Invalid hexadecimal input!"
            Colors.red(f"{error.center(60)}")
            Colors.light_blue("     " + dash)

    def decimal_float_binary():
        null = ""
        dash = null.center(58, "-")
        Colors.light_blue("\n     Enter decimal number: ")
        decimal_fraction = input(colr().hex("#ff0000", "\n     > ", rgb_mode=True))
        decimal_fraction = float(decimal_fraction)
        try:
            integral_part = int(decimal_fraction)
            fractional_part = decimal_fraction - integral_part

            integral_binary = bin(integral_part)[2:]

            fractional_binary = ""
            while fractional_part > 0:
                fractional_part *= 2
                bit = int(fractional_part)
                fractional_binary += str(bit)
                fractional_part -= bit
            binary_string = f"{integral_binary}.{fractional_binary}"
            Colors.light_blue("\n" + "     " + dash)
            binary = f"      ({binary_string})2"
            Colors.red(f"{binary.center(60)}")
            Colors.light_blue("     " + dash)
        except ValueError:
            Colors.light_blue("\n" + "     " + dash)
            error = "Error: Invalid float decimal input!"
            Colors.red(f"{error.center(60)}")
            Colors.light_blue("     " + dash)
