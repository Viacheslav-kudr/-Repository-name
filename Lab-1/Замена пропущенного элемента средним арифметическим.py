numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
index_temp = 0
index = 0
sum = 0
for i in numbers:
    if i != None:
        sum += i
    else:
        index =index_temp
    index_temp += 1

numbers[index] = sum / (len(numbers))


# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
