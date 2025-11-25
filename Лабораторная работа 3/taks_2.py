# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, separator=','):
    list1 = group1.split(separator)
    list2 = group2.split(separator)

    common = []

    for item in list1:
        if item in list2:
            common.append(item)

    common.sort()

    return common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой
result = find_common_participants(participants_first_group, participants_second_group, separator='|')

print(result)
