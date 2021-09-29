from entities.operations import InvestmentOperation
from entities.constants import InvestmentNature, ExchangeOperation
from datetime import datetime
from typing import List, Dict, Union


def add_operation_messages() -> Dict[str, Union[str, Dict]]:
    operation_types = {
        "c": ExchangeOperation.BUY,
        "v": ExchangeOperation.SELL,
        "t": ExchangeOperation.TRANSFER
    }
    investment_nature = {
        "f": InvestmentNature.FIXED,
        "v": InvestmentNature.VARIABLE,
    }
    messages = {
        "title": "Cadastro de operações!\n",
        "add_value": "\t Valor: R$",
        "add_type": f"\t Tipo da operação {operation_types.keys()}: ",
        "add_title": "\t Título do investimento: ",
        "add_nature": f"\t Natureza do investimento {investment_nature.keys()}: ",
        "add_description": "\t Descrição (Opcional): ",
        "do_more_operations": "\t\t Deseja adicionar uma nova operação? [S/N]: ",
        "operation_types": operation_types,
        "investment_nature": investment_nature,
        "separate_forms": "\t"+"="*30
    }
    return messages


def fill_operations_from_user(do: bool=True) -> List[InvestmentOperation]:
    if not do:
        return []
    messages = add_operation_messages()
    print(messages["title"])
    operations = []

    do_more_operations = True
    while do_more_operations:

        value = input(messages["add_value"])
        if isinstance(value, str):
            if "," in value:
                value = value.replace(",", ".")
            value = float(value)

        op_type = input(messages["add_type"]).strip().lower()
        operation = InvestmentOperation(
            date=datetime.now(),
            type=messages["operation_types"][op_type],
            value=value
        )
        if op_type in ["c", "v"]:
            operation.title = input(messages["add_title"]).strip().lower()
            nature = input(messages["add_nature"]).strip().lower()
            if nature in messages["investment_nature"]:
                operation.investment_nature = messages['investment_nature'][nature]
            operation.description = input(messages["add_description"])

        operations.append(operation)

        do_more_operations = input(messages["do_more_operations"]).strip().lower() == "s"
        print(messages["separate_forms"])

    return operations


if __name__ == "__main__":
    from pprint import pprint
    operations = fill_operations_from_user()
    print()
    pprint([op.dict() for op in operations])
