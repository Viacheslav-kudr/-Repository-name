def remove_whitespace(str_):
    words_list = str_.split(" ")

    words_list_without_empty_string = []
    for word in words_list:
        if word:
            words_list_without_empty_string.append(word)

    return " ".join(words_list_without_empty_string)


str_with_space = """123.    test bks
print   test11"""  # исходная строка
print(remove_whitespace(str_with_space))
