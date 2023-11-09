import pytest

from config import DATA_PATH
from src.utils import change_date_format, format_payment_info, get_info_from_json_file, pick_five_operations

actions = get_info_from_json_file(DATA_PATH)


def test_get_info_from_json_file():
    assert get_info_from_json_file(DATA_PATH)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def all_transactions():
    return actions


def test_pick_five_operations(all_transactions):
    five_transactions = pick_five_operations(all_transactions)
    assert five_transactions == [
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}},
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907",
        },
        {
            "id": 114832369,
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890",
            "operationAmount": {"amount": "48150.39", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Visa Classic 2842878893689012",
            "to": "Счет 35158586384610753655",
        },
        {
            "id": 154927927,
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614",
            "operationAmount": {"amount": "30153.72", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 7810846596785568",
            "to": "Счет 43241152692663622869",
        },
        {
            "id": 482520625,
            "state": "EXECUTED",
            "date": "2019-11-13T17:38:04.800051",
            "operationAmount": {"amount": "62814.53", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 38611439522855669794",
            "to": "Счет 46765464282437878125",
        },
        {
            "id": 801684332,
            "state": "EXECUTED",
            "date": "2019-11-05T12:04:13.781725",
            "operationAmount": {"amount": "21344.35", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 77613226829885488381",
        },
    ]


def test_change_date_format(all_transactions):
    five_transactions = pick_five_operations(all_transactions)
    assert [change_date_format(item["date"]) for item in five_transactions] == [
        "08.12.2019",
        "07.12.2019",
        "19.11.2019",
        "13.11.2019",
        "05.11.2019",
    ]


def test_format_payment_info(all_transactions):
    five_transactions = pick_five_operations(all_transactions)
    assert [format_payment_info(item["to"]) for item in five_transactions] == [
        "Счет **5907",
        "Счет **3655",
        "Счет **2869",
        "Счет **8125",
        "Счет **8381",
    ]
    assert format_payment_info("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"
