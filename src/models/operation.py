import re
from datetime import datetime


class Operation:
    def __init__(self, pk: int, state: str, date: str, operation_amount: dict, description: str, _from: str, _to: str):
        self.pk = pk
        self.state = state
        self.date = date
        self.operation_amount = operation_amount
        self.description = description
        self._from = self.convert_payment(_from) if _from else "Из кошелька"
        self._to = _to

    def convert_date(self, isodate: str):
        date = datetime.fromisoformat(isodate)
        return date.strftime("%d.%m.%Y")

    def convert_payment(self, payment: str):
        list_of_info = payment.split(" ")
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

    def __str__(self):
        return (
            f"{self.convert_date(self.date)} {self.description}\n"
            f"{self._from} -> {self._to}\n"
            f'{self.operation_amount["amount"]} {self.operation_amount["currency"]["name"]}\n'
        )
