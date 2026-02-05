list_ = [4, -1, 10, -1, 3, 3, -1, 8, 6, 9]

# предположим, что первый элемент в нашем списке минимальный
min_value_index = 0
min_value = list_[min_value_index]

# TODO заменить на enumerate
for index, i in enumerate(list_):
    current_value = list_[index]
    if current_value <= min_value:
        min_value = current_value
        min_value_index = index

print("Минимальный элемент =", min_value, "находится по индексу", min_value_index)
