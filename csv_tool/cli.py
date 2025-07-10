from __future__ import annotations
from pathlib import Path
import argparse
from typing import List

from csv_tool.io import read_csv
from csv_tool.operations.filters import Filter

def build_parser() -> argparse.ArgumentParser:
    """Создание и настройка ArgumentParser для csv-tool CLI."""
    parser = argparse.ArgumentParser(
        prog="csv-tool",
        description="Фильтр и агрегация CSV-файла"
    )
    parser.add_argument(
        "path",
        type=Path,
        help="Путь до CSV-файла"
    )
    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )
    p_where = subparsers.add_parser(
        "where",
        help="Фильтр строк"
    )
    p_where.add_argument(
        "expr",
        help='e.g. "price>100"'
    )
    
    p_agg = subparsers.add_parser(
        "aggregate",
        help="Агрегация столбца"
    )
    p_agg.add_argument(
        "expr",
        help='e.g. "price=avg"'
    )
    
    return parser

def main(argv: List[str] | None = None) -> None:
    """Точка входа как для консоли, так и для тестов."""
    args = build_parser().parse_args(argv)
    print(args)
    rows = read_csv(args.path)        
    if args.command == "where":
        result = Filter.from_expr(args.expr).run(rows)
        Filter.cute_print(result)
        return 


if __name__ == "__main__":
    main()