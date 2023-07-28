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


class Methods:
    def octal_binary():
        null = ""
        dash = null.center(55, "-")
        Colors.light_blue("\n     Enter decimal number: ")
        octal = input(colr().hex("#ff0000", "\n     > ", rgb_mode=True))
        octal_digits = list(map(int, str(octal)))
        binary_digits = [format(digit, "03b") for digit in octal_digits]
        binary_result = "".join(binary_digits)
        Colors.light_blue("\n" + "     " + dash)
        print(
            colr().hex("#6666ff", "     |", rgb_mode=True),
            colr().hex("#ff0000", binary_result.center(50), rgb_mode=True),
            colr().hex("#6666ff", " |", rgb_mode=True),
        )
        Colors.light_blue("     " + dash)

    def decimal_to_octal():
        null = ""
        dash = null.center(55, "-")
        Colors.light_blue("\n     Enter decimal number: ")
        decimal_number = input(colr().hex("#ff0000", "\n     > ", rgb_mode=True))
        show_decimal = decimal_number
        decimal_number = int(decimal_number) 
        if decimal_number == 0:
            Colors.red (
                "0"  # Special case for input 0, as its octal representation is also 0
            )

        octal_digits = []
        while decimal_number > 0:
            quotient, remainder = divmod(decimal_number, 8)
            octal_digits.insert(
                0, str(remainder)
            )  # Insert the remainder at the beginning of the list
            decimal_number = quotient

        octal_result= "".join(octal_digits)
        Colors.light_blue("\n" + "     " + dash)
        print(
            colr().hex("#6666ff", "     |", rgb_mode=True),
            colr().hex("#ff0000",octal_result.center(50), rgb_mode=True),
            colr().hex("#6666ff", " |", rgb_mode=True),
        )
        Colors.light_blue("     " + dash)
