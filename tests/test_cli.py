import subprocess
from pathlib import Path


import subprocess
from pathlib import Path


def test_where_price_gt_500(tmp_path: Path):
    csv_path = tmp_path / "test.csv"
    csv_path.write_text(
        """name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6
"""
    )

    result = subprocess.run(
        ["python", "-m", "csv_tool.cli", str(csv_path), "where", "price>500"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "iphone" in result.stdout
    assert "galaxy" in result.stdout
    assert "redmi" not in result.stdout
