from csv_tool.operations.aggregate import Aggregate

def test_from_expr_valid():
    agg = Aggregate.from_expr("price=avg")
    assert agg.column == "price"
    assert agg.func_name == "avg"
    
def test_run_avg():
    rows = [
        {"price": "100"},
        {"price": "200"},
        {"price": "300"},
    ]
    agg = Aggregate.from_expr("price=avg")
    result = agg.run(rows)
    assert result == 200.00
        
def test_min_max():
    rows = [
        {"x": "3"},
        {"x": "9"},
        {"x": "5"},
    ]
    assert Aggregate.from_expr("x=min").run(rows) == 3.0
    assert Aggregate.from_expr("x=max").run(rows) == 9.0
    
