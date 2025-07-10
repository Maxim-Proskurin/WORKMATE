import pytest
from csv_tool.operations.filters import Filter


def test_from_expr_valid():
    f = Filter.from_expr("price>100")
    assert f.column == "price"
    assert f.raw_value == "100"
    assert callable(f.op)

def test_run_gt_filter():
    rows = [
        {"price": "50"},
        {"price": "150"},
        {"price": "250"}
    ]
    f = Filter.from_expr("price>100")
    result = f.run(rows)
    assert len(result) == 2
    assert result[0]["price"] == "150"
    assert result[1]["price"] == "250"
    
