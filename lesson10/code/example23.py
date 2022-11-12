from typing import Final

MIN_NAME_LENGTH: Final = 2

# выдаст ошибку, зафиксированную системой проверки типов
MIN_NAME_LENGTH += 1

class Validator(object):
    MIN_NAME_LENGTH: Final[int] = 4

class UserValidator(Validator):
    # эта строка будет отмечена интерпретатором
    MIN_NAME_LENGTH = 3