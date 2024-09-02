def lang_info(ltr: str) -> str:
    if 'A' <= ltr <= 'Z' or 'a' <= ltr <= 'z':
        return 'eng'
    elif 'А' <= ltr <= 'Я' or 'а' <= ltr <= 'я':
        return 'ru'


def reg_info(ltr: str) -> str:
    if ltr == ltr.lower() and ltr.isalpha():
        return "low"
    elif ltr == ltr.upper() and ltr.isalpha():
        return "up"
    else:
        return "not a letter"


def big_letters(ltr, step) -> str:
    if lang_info(ltr) == 'eng':
        return chr(ord('A') + (ord(ltr) + step - ord('A')) % 26) #при делении отр числа остаток от деления - разница (-4 % 10 = 6)
    elif lang_info(ltr) == 'ru':
        return chr(ord('А') + (ord(ltr) + step - ord('А')) % 32)
    else:
        return ltr


def small_letters(ltr, step) -> str:
    if lang_info(ltr) == 'eng':
        return chr(ord('a') + (ord(ltr) + step - ord('a')) % 26)
    elif lang_info(ltr) == 'ru':
        delt = abs(ord('а') + (ord(ltr) + step - ord('а')) % 32)
    else:
        return ltr


def default(ltr: str):
    return ltr


displacement = int(input())
for i in input():
    switch = {
        "low": small_letters(i, displacement),
        "up": big_letters(i, displacement),
        "not a letter": default(i)
    }
    print(switch.get(reg_info(i)), end='')


# Интересный свособ присвоения: a = ('b', 'c')[условие]