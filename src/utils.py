import json
import os
import re


# JOINED_PATH = os.path.join(os.getcwd(), 'operations.json')
# print(os.getcwd())

def get_info_from_json_file() -> list[dict]:
    """открывает файл в формате json и превращает в формат питон"""
    with open('/home/vlad/PycharmProjects/Course_work_3_Morozov/src/operations.json', encoding="utf-8") as f:
        operations_json = f.read()
        operations = json.loads(operations_json)
    return operations


def pick_five_operations(any_list: list[dict]) -> list[dict]:
    """выбирает из списка словарей, словари с определенным значением,
    упорядочивает словари по дате (начиная с большей) и выбирает 5 словарей"""
    new_list = []
    for one_dict in any_list:
        if one_dict == {}:
            pass
        elif one_dict["state"] == "EXECUTED":
            new_list.append(one_dict)
    sorted_list = sorted(new_list, key=lambda x: x["date"], reverse=True)
    five_operations = sorted_list[:5]
    return five_operations


def change_date_format(string: str) -> str:
    """принимает на вход строку, вида '2018-07-11T02:26:18.671407'
    и возвращает строку с датой в виде '11.07.2018'"""
    date_old_string = string.split("T")[0]
    date = date_old_string.split("-")[2]
    month = date_old_string.split("-")[1]
    year = date_old_string.split("-")[0]
    return f"{date}.{month}.{year}"


def format_payment_info(info: str) -> str:
    """принимает на вход строку с информацией тип и номер карты/счета
    и возвращает эту строку с замаскированным номером карты/счета
    в формате XXXX XX** **** XXXX для карты и
    в формате **XXXX для счета."""
    list_of_info = info.split(" ")
    payment_number = list_of_info.pop()
    payment_type = " ".join(list_of_info)

    if len(payment_number) == 16:
        list_of_segments = re.findall(".{%s}" % 4, payment_number)
        list_of_segments[1] = list_of_segments[1][:2] + "**"
        list_of_segments[2] = "****"
        card_number = " ".join(list_of_segments)
        return f"{payment_type} {card_number}"
    elif len(payment_number) == 20:
        acc_number = "**" + payment_number[16:]
        return f"{payment_type} {acc_number}"
