import os
import pandas as pd

COLUMNS = ["Date", "Category", "Amount", "Description"]

def load_expenses(path):
    if not os.path.exists(path):
        return pd.DataFrame(columns=COLUMNS)
    df = pd.read_csv(path)
    if df.empty:
        return pd.DataFrame(columns=COLUMNS)
    df["Date"] = pd.to_datetime(df["Date"])
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce").fillna(0)
    return df

def save_expense(path, date, category, amount, description):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    exists = os.path.exists(path)
    row = pd.DataFrame([[date, category, amount, description]], columns=COLUMNS)
    row.to_csv(path, mode="a", header=not exists, index=False)

def category_summary(df):
    if df.empty:
        return pd.DataFrame(columns=["Category", "Amount"])
    return df.groupby("Category", as_index=False)["Amount"].sum().sort_values("Amount", ascending=False)

def monthly_summary(df):
    if df.empty:
        return pd.DataFrame(columns=["Month", "Amount"])
    result = df.groupby(df["Date"].dt.to_period("M"))["Amount"].sum().reset_index()
    result["Month"] = result["Date"].astype(str)
    return result[["Month", "Amount"]]

def build_forecast_data(df):
    return monthly_summary(df)
