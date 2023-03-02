import json
from datetime import datetime

# Получение всех данных
def get_data() -> list[dict]:
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


# Выводит на экран список выполненных операций клиентом в банке
def get_filtred_data(data, filtered_empty_from=False):
    # for x in data:
    #     if "state" in x and x["state"] == 'EXECUTED'
    data = [x for x in data if "state" in x and x["state"] == 'EXECUTED']
    if filtered_empty_from:
        data = [x for x in data if "from" in x]
    return data


# Выводит на экран список из 5 последних выполненных клиентом операций
def get_last_data(data, count_last_values):
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:count_last_values]


# Функция, которая выводит на экран список из 5 последних выполненных клиентом операций
def get_formatted_data(data):
    formatted_data = []
    for row in data:
        # Перевод даты в формат ДД.MM.ГГГГ (пример: 13.02.2023)
        date_time_str = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f")
        date = datetime.strftime(date_time_str, "%d.%m.%Y")
#         # date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%M.%Y")
        description = row["description"]

        # Маскировка карты в формате  XXXX XX** **** XXXX (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом)
        sender = row["from"].split()
        sender_bill = sender.pop(-1)
        sender_bill = f'{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}'
        sender_info = " ".join(sender)

        # Номер счета замаскирован и не отображается целиком в формате **XXXX (видны только последние 4 цифры номера счета).
        recipient = f'**{row["to"][-4:]}'
        amount = f'{row["operationAmount"]["amount"]} {row["operationAmount"]["currency"]["name"]}'

        formatted_data.append(f"""\
{date} {description}
{sender_info} {sender_bill} -> Счет {recipient}
{amount}
""")
    return formatted_data


# DATA1 = get_data()
# b = get_formatted_data(DATA1)
# print(b)

# for i in a:
#     print(i)
