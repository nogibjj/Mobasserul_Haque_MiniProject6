"""
Test for ETL and complex SQL queries
"""

import subprocess


def test_extract():
    """tests extract()"""
    result = subprocess.run(
        ["python", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout


def test_transform_load():
    """tests transform_load"""
    result = subprocess.run(
        ["python", "main.py", "load"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming data..." in result.stdout


def test_general_query():
    """tests general_query"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "query",
            """SELECT 
                rg.Major, 
                rg.Employed AS Undergrad_Employed, 
                gs.Grad_employed AS Grad_Employed,
                rg.Unemployment_rate AS Undergrad_Unemployment_Rate,
                gs.Grad_unemployment_rate AS Grad_Unemployment_Rate,
                (gs.Grad_median - rg.Median) AS Salary_Premium
            FROM RecentGradsDB rg
            JOIN GradStudentsDB gs
                ON rg.Major_code = gs.Major_code
            WHERE rg.Unemployment_rate < 0.05  -- High undergraduate employment rate
              AND gs.Grad_unemployment_rate < 0.05  -- High graduate employment rate
            ORDER BY Salary_Premium DESC;"""
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


if __name__ == "__main__":
    test_extract()
    test_transform_load()
    test_general_query()
