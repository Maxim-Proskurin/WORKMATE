# CSV Tool

CLI-утилита для фильтрации и агрегации CSV-файлов.

## Пример запуска:

```bash
python -m csv_tool.cli test.csv where price>100
python -m csv_tool.cli test.csv aggregate price=avg
