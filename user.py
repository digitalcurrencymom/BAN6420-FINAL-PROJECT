import csv
from dataclasses import dataclass, field
from typing import Dict

@dataclass
class User:
    age: int
    gender: str
    total_income: float
    expenses: Dict[str, float] = field(default_factory=dict)

    def to_dict(self):
        d = {
            'age': int(self.age) if self.age not in (None, '') else None,
            'gender': self.gender,
            'total_income': float(self.total_income) if self.total_income not in (None, '') else None,
        }
        for k, v in self.expenses.items():
            d[k] = float(v) if v not in (None, '') else 0.0
        return d

    @staticmethod
    def save_csv(rows, csv_path='survey_users.csv'):
        # rows: iterable of dict-like
        if not rows:
            return
        keys = rows[0].keys()
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            for r in rows:
                writer.writerow(r)
