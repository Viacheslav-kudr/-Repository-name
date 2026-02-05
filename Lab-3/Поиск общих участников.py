# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, n=','):
	first = set(group1.split(n))
	second = set(group2.split(n))
	participants = first.intersection(second)
	return sorted(participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", participants)
# TODO Провеьте работу функции с разделителем отличным от запятой
