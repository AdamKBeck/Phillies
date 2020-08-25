"""
Fetches and parses the MLB dataset
"""
from bs4 import BeautifulSoup
from enum import Enum
from urllib.request import urlopen


DATASET_URL = "https://questionnaire-148920.appspot.com/swe/data.html"

class SalaryStatus(Enum):
    NONE = 'No salary value was present'
    NO_SALARY_DATA = "'no salary data' was present for the value"
    UNKNOWN = 'An unknown error occurred when parsing salary data'
    GOOD = 'Salary was parsed'


class Player:
    CSV_HEADER = [
        'Player',
        'Salary',
        'Salary Status Code',
        'Salary Status Message',
        'Year',
        'Level',
        'Is Top Player'
    ]

    def __init__(self, name, salary, year, level):
        self.name = name
        self.salary, self.salary_status = self._parse_salary(salary)
        self.year = year
        self.level = level
        self.is_top_player = False

    def _parse_salary(self, salary):
        if not salary:
            return salary, SalaryStatus.NONE
        if salary.lower() == 'no salary data':
            return salary, SalaryStatus.NO_SALARY_DATA

        # Keep only the digits of the salary string, convert to int.
        try:
            salary = int(''.join(filter(str.isdigit, salary)))
            return salary, SalaryStatus.GOOD
        except ValueError:
            return salary, SalaryStatus.UNKNOWN

    def to_csv_row(self):
        return [
            self.name,
            self.salary,
            self.salary_status.name,
            self.salary_status.value,
            self.year,
            self.level,
            self.is_top_player,
        ]


def fetch():
    """
    Fetches the MLB player dataset
    rtype: List[Player]
    """
    html = urlopen(DATASET_URL).read()
    soup = BeautifulSoup(html, features="html.parser")
    rows = soup.find("tbody")

    row_value = lambda row, x: row.find("td", {"class": f"player-{x}"}).get_text()
    all_players = [
        Player(
            name=row_value(row, "name"),
            salary=row_value(row, "salary"),
            year=row_value(row, "year"),
            level=row_value(row, "level"),
        )
        for row in rows.findAll("tr")
    ]

    return all_players
