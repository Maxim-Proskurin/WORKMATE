from __future__ import annotations

import operator
import re
from typing import Any, Callable, Dict, List

from tabulate import tabulate

Row = Dict[str, str]


class Filter:
    """Парсит выражение 'col>value' и фильтрует строки CSV."""

    def __init__(
        self, column: str,
        op: Callable[[Any, Any], bool],
        raw_value: str
    ):
        self.column = column
        self.op = op
        self.raw_value = raw_value

    @classmethod
    def from_expr(cls, expr: str) -> "Filter":
        """Преобразует строку вида 'price>100' в объект Filter."""
        m = re.match(
            r"^(?P<col>[^<>=]+)(?P<sym>[<>=])(?P<val>.+)$",
            expr.strip()
        )
        if not m:
            raise ValueError(f"Неверное выражение фильтра: {expr}")
        col, sym, val = (
            m.group("col"),
            m.group("sym"),
            m.group("val")
        )
        op_map = {"<": operator.lt, ">": operator.gt, "=": operator.eq}

        return cls(col, op_map[sym], val)

    @staticmethod
    def _cast(x: str) -> Any:
        """Ставит float,
        если строка выглядит как число,
        иначе оставляет строку.
        """

        return float(x) if x.replace(".", "", 1).isdigit() else x

    def run(self, rows: List[Row]) -> List[Row]:
        """Вернёт список строк, удовлетворяющих условию."""
        right = self._cast(self.raw_value)

        return [r for r in rows if self.op(self._cast(r[self.column]), right)]

    @staticmethod
    def cute_print(rows: List[Row]) -> None:
        """Таблица или сообщение об отсутствии совпадений."""
        if rows:
            print(tabulate(rows, headers="keys"))
        else:
            print("Нет подходящих строк")
