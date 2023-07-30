import class_def
from class_def import Colors
from class_def import Style
from class_def import Methods
from time import sleep
from class_def import Operator

print(
    class_def.colr().hex(
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
    class_def.colr().hex("#6666ff", "1.0", rgb_mode=True),
)


def main_choice():
    Colors.light_blue("\n" + "     " + Style.dash)
    print(
        class_def.colr().hex("#6666ff", "     |", rgb_mode=True),
        class_def.colr().hex(
            "#ff0000", "[1] Octal to Binary         [2] Decimal to Octal", rgb_mode=True
        ),
        class_def.colr().hex("#6666ff", "      |", rgb_mode=True),
    )
    print(
        class_def.colr().hex("#6666ff", "     |", rgb_mode=True),
        class_def.colr().hex(
            "#ff0000",
            "[3] Decimal to Binary       [4] Binary to Decimal ",
            rgb_mode=True,
        ),
        class_def.colr().hex("#6666ff", "    |", rgb_mode=True),
    )
    print(
        class_def.colr().hex("#6666ff", "     |", rgb_mode=True),
        class_def.colr().hex(
            "#ff0000",
            "[5] Decimal to Hexadecimal  [6] Hexadecimal to Binary",
            rgb_mode=True,
        ),
        class_def.colr().hex("#6666ff", " |", rgb_mode=True),
    )
    print(
        class_def.colr().hex("#6666ff", "     |", rgb_mode=True),
        class_def.colr().hex(
            "#ff0000", "[7] Decimal float to binary [8] Exit", rgb_mode=True
        ),
        class_def.colr().hex("#6666ff", "                  |", rgb_mode=True),
    )
    # print(class_def.colr().hex("#6666ff","     |",rgb_mode=True),class_def.colr().hex("#ff0000","",rgb_mode=True),class_def.colr().hex("#6666ff","    |",rgb_mode=True))
    Colors.light_blue("     " + Style.dash)
    choice = input(class_def.colr().hex("#ff0000", "\n     > ", rgb_mode=True))
    if choice == "1":
        Methods.octal_binary()
        sleep(0.8)
        main_choice()
    elif choice == "2":
        Methods.decimal_to_octal()
        sleep(0.8)
        main_choice()
    elif choice == "3":
        Methods.decimal_to_binary()
        sleep(0.8)
        main_choice()
    elif choice == "4":
        Methods.binary_to_decimal()
        sleep(0.8)
        main_choice()
    elif choice == "5":
        Methods.decimal_to_hexadecimal()
        sleep(0.8)
        main_choice()

    elif choice == "8":
        Operator.exit()


main_choice()
