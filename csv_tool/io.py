from pathlib import Path
import csv
from typing import Dict, List

Row = Dict[str, str]                  

def read_csv(path: Path) -> List[Row]:
    """Возвращает список словарей, каждый словарь — это строка CSV-файла."""
    with path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)    
        return list(reader) 