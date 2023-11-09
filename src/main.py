from config import DATA_PATH
from src.utils import change_date_format, format_payment_info, get_info_from_json_file, pick_five_operations

if __name__ == "__main__":
    transactions = get_info_from_json_file(DATA_PATH)
    for transaction in pick_five_operations(transactions):
        if transaction["description"] == "Открытие вклада":
            print(
                f"""{change_date_format(transaction["date"])} {transaction['description']}
Ваш кошелек -> {format_payment_info(transaction["to"])}
{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']["name"]}
"""
            )
        else:
            print(
                f"""{change_date_format(transaction["date"])} {transaction['description']}
{format_payment_info(transaction["from"])} -> {format_payment_info(transaction["to"])}
{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']["name"]}
"""
            )
