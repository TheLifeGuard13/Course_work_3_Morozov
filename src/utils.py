import json

from src.models.operation import Operation


def get_info_from_json_file(filename) -> list[dict]:
    """открывает файл о словарями в формате json и превращает в формат питон"""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def get_operation_instances(operations: list[dict]) -> list[Operation]:
    list_ = []
    for operation in operations:
        if operation:
            list_.append(
                Operation(
                    pk=operation["id"],
                    state=operation["state"],
                    date=operation["date"],
                    operation_amount=operation["operationAmount"],
                    description=operation["description"],
                    _from=operation.get("from"),
                    _to=operation["to"],
                )
            )
    return list_


def get_executed_operations(operations: list[Operation]) -> list[Operation]:
    return [operation for operation in operations if operation.state == "EXECUTED"]


def sort_operation(operations: list[Operation]) -> list[Operation]:
    return sorted(operations, key=lambda x: x.date, reverse=True)
