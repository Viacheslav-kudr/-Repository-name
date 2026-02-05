def delete(list_, index=None):
    ...  # TODO реализовать функцию удаления элемента из списка по индексу
    if index is None:
        index = len(list_) - 1
    elif index < 0:
        index = index + len(list_)

    return list_[:index] + list_[index+1:]

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
