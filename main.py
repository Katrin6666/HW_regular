from pprint import pprint
import re
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
#pprint(contacts_list)



## 1. Поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно.
def name_normalization(rows):
    result = [' '.join(employee[0:3]).split(' ')[0:3] + employee[3:7] for employee in rows]
    return result

## 2. Объединить все дублирующиеся записи о человеке в одну строку.
def remove_duplicates(correct_name_list):
    no_duplicates = []
    for compared in correct_name_list:
        for employee in correct_name_list:
            if compared[0:2] == employee[0:2]:
                list_employee = compared
                compared = list_employee[0:2]
                for i in range(2, 7):
                    if list_employee[i] == '':
                        compared.append(employee[i])
                    else:
                        compared.append(list_employee[i])
        if compared not in no_duplicates:
            no_duplicates.append(compared)

    return no_duplicates

## 3. Привести все телефоны в формат +7(999)999-99-99.
def updating_phone_numbers(rows):
    phonebook = []
    pattern = re.compile(regular)
    phonebook = [[pattern.sub(r'+7(\2)\3-\4-\5', string) for string in strings] for strings in rows]

    return phonebook

correct_name_list = name_normalization(contacts_list)
no_duplicates_list = remove_duplicates(correct_name_list)
regular = r'(\+7|8)+[\s(]*(\d{3,3})[\s)-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})'
correct_list = updating_phone_numbers(no_duplicates_list)


## 2. Сохраните получившиеся данные в другой файл.
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(correct_list)