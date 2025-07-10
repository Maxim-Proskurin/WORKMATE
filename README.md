# CSV Tool

CLI-утилита для фильтрации и агрегации CSV-файлов.
[![CI](https://github.com/Maxim-Proskurin/WORKMATE/actions/workflows/python-app.yml/badge.svg)](https://github.com/Maxim-Proskurin/WORKMATE/actions)
[![Coverage Status](https://img.shields.io/badge/coverage-90%25-brightgreen)](#)

## Пример запуска:

```bash
poetry install

python -m csv_tool.cli test.csv where price>100
python -m csv_tool.cli test.csv aggregate price=avg



python -m csv_tool.cli test.csv where price>500
python -m csv_tool.cli test.csv aggregate rating=avg

Тесты: pytest --cov=csv_tool

Покрытие: 90%

Линтер: flake8 - ✅ без ошибок

CLI-проверка: ✅ работает

[csv_tool/cli.py] - точка входа

operations/filters.py - фильтрация

operations/aggregate.py - агрегация

tests/ - тесты
