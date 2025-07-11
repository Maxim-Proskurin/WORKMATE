from typing import Dict, Callable, List
from statistics import mean
from tabulate import tabulate

Row = Dict[str, str]


def agg_avg(values: List[float]) -> float:
    return mean(values)


def agg_min(values: List[float]) -> float:
    return min(values)


def agg_max(values: List[float]) -> float:
    return max(values)


AGG_FUNCTIONS: Dict[str, Callable[[List[float]], float]] = {
    "avg": agg_avg,
    "min": agg_min,
    "max": agg_max,
}


class Aggregate:
    """Вычисляет агрегирующую функцию
    (avg/min/max) для числовой колонки.

    Позволяет легко добавлять новые функции
    агрегации через словарь AGG_FUNCTIONS.
    """

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

        if func_name not in AGG_FUNCTIONS:
            raise ValueError(f"Функция '{func_name}' не поддерживается")

        return cls(column=column, func_name=func_name)

    def run(self, rows: List[Row]) -> float:
        """Возвращает число - результат агрегации"""
        values = [float(r[self.column]) for r in rows]
        func = AGG_FUNCTIONS[self.func_name]
        return func(values)

    @staticmethod
    def cute_print(column: str, value: float) -> None:
        """Выводит результат агрегации в виде таблицы.

        Показывает имя колонки и вычисленное агрегированное
        значение с помощью tabulate для удобства чтения.

        Args:
            column: Имя колонки, по которой выполнена агрегация.
            value: Результат агрегирующей функции.
        """
        print(tabulate([{"column": column, "value": value}], headers="keys"))
