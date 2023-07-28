from functools import reduce
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


def main_choice():
    print(
        colr().hex(
            "#ff0000",
            """
     :'######:::'#######::'##::: ##:'##::::'##:'########:'########::'########:'########:'########::
     '##... ##:'##.... ##: ###:: ##: ##:::: ##: ##.....:: ##.... ##:... ##..:: ##.....:: ##.... ##:
      ##:::..:: ##:::: ##: ####: ##: ##:::: ##: ##::::::: ##:::: ##:::: ##:::: ##::::::: ##:::: ##:
      ##::::::: ##:::: ##: ## ## ##: ##:::: ##: ######::: ########::::: ##:::: ######::: ########::
      ##::::::: ##:::: ##: ##. ####:. ##:: ##:: ##...:::: ##.. ##:::::: ##:::: ##...:::: ##.. ##:::
      ##::: ##: ##:::: ##: ##:. ###::. ## ##::: ##::::::: ##::. ##::::: ##:::: ##::::::: ##::. ##::
     . ######::. #######:: ##::. ##:::. ###:::: ########: ##:::. ##:::: ##:::: ########: ##:::. ##:
     :......::::.......:::..::::..:::::...:::::........::..:::::..:::::..:::::........::..:::::..::""",
            rgb_mode=True,
        ),
        colr().hex("#6666ff", "1.0", rgb_mode=True),
    )

    Colors.light_blue("\n" + "     " + Style.dash)
    print(
        colr().hex("#6666ff", "     |", rgb_mode=True),
        colr().hex(
            "#ff0000", "[1] Octal to Binary         [2] Decimal to Octal", rgb_mode=True
        ),
        colr().hex("#6666ff", "      |", rgb_mode=True),
    )
    print(
        colr().hex("#6666ff", "     |", rgb_mode=True),
        colr().hex(
            "#ff0000",
            "[3] Decimal to Binary       [4] Binary to Decimal ",
            rgb_mode=True,
        ),
        colr().hex("#6666ff", "    |", rgb_mode=True),
    )
    print(
        colr().hex("#6666ff", "     |", rgb_mode=True),
        colr().hex(
            "#ff0000",
            "[5] Decimal to Hexadecimal  [6] Hexadecimal to Binary",
            rgb_mode=True,
        ),
        colr().hex("#6666ff", " |", rgb_mode=True),
    )
    print(
        colr().hex("#6666ff", "     |", rgb_mode=True),
        colr().hex("#ff0000", "[7] Decimal float to binary [8] Exit", rgb_mode=True),
        colr().hex("#6666ff", "                  |", rgb_mode=True),
    )
    # print(colr().hex("#6666ff","     |",rgb_mode=True),colr().hex("#ff0000","",rgb_mode=True),colr().hex("#6666ff","    |",rgb_mode=True))
    Colors.light_blue("     " + Style.dash)
    choice = input(colr().hex("#ff0000","\n     > ",rgb_mode=True))

main_choice()
