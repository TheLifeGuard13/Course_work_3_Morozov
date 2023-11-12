from config import DATA_PATH
from src.utils import (get_executed_operations, get_info_from_json_file,
                       get_operation_instances, sort_operation)


def main():
    if __name__ == "__main__":
        operations = get_info_from_json_file(DATA_PATH)
        operation_instances = get_operation_instances(operations)
        executed_operations = get_executed_operations(operation_instances)
        sorted_operations = sort_operation(executed_operations)[:5]
        for operation in sorted_operations:
            print(operation)


main()
