# Personal Expense Analysis & Prediction System

A beginner-friendly Flask + Machine Learning project for recording personal expenses, analyzing spending patterns, visualizing category/monthly totals, and predicting the next month's total expense.

## Features
- Add an expense from the web interface
- View total spending and transaction count
- Category-wise expense analysis
- Monthly expense analysis
- Next-month expense prediction using Linear Regression
- Sample dataset included for demonstration
- Simple responsive dashboard

## Technology Stack
- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- HTML/CSS/JavaScript

## Project Structure
```text
personal_expense_project/
├── app.py
├── model.py
├── utils.py
├── generate_data.py
├── requirements.txt
├── README.md
├── data/
│   └── expenses.csv
├── models/
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Installation
1. Install Python 3.10 or newer.
2. Open a terminal in the project folder.
3. Create a virtual environment:
   - Windows: `python -m venv venv`
   - Activate: `venv\Scripts\activate`
4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Run
```bash
python app.py
```
Open `http://127.0.0.1:5000/` in a browser.

## Generate New Sample Data
```bash
python generate_data.py
```
This replaces the sample dataset with a newly generated demonstration dataset.

## Dataset Format
The CSV contains:
- `Date`: transaction date
- `Category`: expense category
- `Amount`: expense amount
- `Description`: short description

## Prediction Method
Monthly expenses are aggregated from transaction data. A Linear Regression model learns the trend across monthly totals and predicts the following month. This is intended for academic demonstration and should not be treated as financial advice.

## Future Enhancements
- Login and multiple-user support
- Budget limits and alerts
- Category-specific forecasting
- Advanced time-series models
- Export to PDF/Excel
- Cloud database
- Mobile-friendly PWA

## Author
Student Project — Personal Expense Analysis & Prediction System
