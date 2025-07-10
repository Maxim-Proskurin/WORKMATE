from typing import Dict
from statistics import mean
from tabulate import tabulate

Row = Dict[str, str]
ALLOWED_FUNC = {"avg", "min", "max"}


class Aggregate:
    """Вычисляет avg/min/max для числовой колонки."""

    def __init__(self, column: str, func_name: str):
        self.column = column
        self.func_name = func_name

    @classmethod
    def from_expr(cls, expr: str) -> "Aggregate":
        """Строка 'price=avg' == Aggregate(column='price', func_name='avg')"""
        if "=" not in expr or expr.count("=") != 1:
            raise ValueError(f"Неверное выражение агрегации: {expr}")

        column, func_name = expr.split("=", 1)
        func_name = func_name.lower().strip()
        column = column.strip()

        if func_name not in ALLOWED_FUNC:
            raise ValueError(f"Функция '{func_name}' не поддерживается")

        return cls(column=column, func_name=func_name)

    def run(self, rows: list[Row]) -> float:
        """Возвращает число - результат агрегации"""
        values = [float(r[self.column]) for r in rows]
        if self.func_name == "avg":
            return mean(values)
        if self.func_name == "min":
            return min(values)
        return max(values)

    @staticmethod
    def cute_print(column: str, value: float) -> None:
        print(tabulate([{"column": column, "value": value}], headers="keys"))
