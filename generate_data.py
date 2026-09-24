import csv, random
from datetime import date, timedelta
from pathlib import Path

random.seed(42)
categories = {
    "Food": (80, 500),
    "Transport": (50, 400),
    "Shopping": (100, 1200),
    "Bills": (500, 2500),
    "Entertainment": (50, 600),
    "Health": (50, 900),
    "Education": (100, 1000),
    "Other": (50, 700)
}
start = date(2025, 1, 1)
rows = []
for i in range(450):
    d = start + timedelta(days=random.randint(0, 500))
    cat = random.choice(list(categories))
    lo, hi = categories[cat]
    amount = round(random.uniform(lo, hi), 2)
    rows.append([d.isoformat(), cat, amount, f"{cat} expense"])

path = Path("data/expenses.csv")
path.parent.mkdir(exist_ok=True)
with path.open("w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Date", "Category", "Amount", "Description"])
    w.writerows(rows)
print(f"Generated {len(rows)} sample transactions at {path}")
