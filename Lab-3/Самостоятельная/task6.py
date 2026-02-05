ALLOW_SYMBOLS = ["0", "1"]  # Допустимые символы


def check_string(str_):
    if not str_:
        return False

    for f in set(str_):  # выделяем все уникальные символы из строки
        if f not in ALLOW_SYMBOLS:
            return False
    return True


print(check_string("1010101010"))
print(check_string("101021231010103"))
print(check_string("asdawqe"))
print(check_string(""))
