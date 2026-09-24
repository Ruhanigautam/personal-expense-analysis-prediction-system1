import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

class ExpensePredictor:
    """Predicts next-month total expenses from historical monthly totals."""
    def predict_next_month(self, df):
        if df.empty:
            return 0.0

        work = df.copy()
        work["Date"] = pd.to_datetime(work["Date"])
        monthly = work.groupby(work["Date"].dt.to_period("M"))["Amount"].sum().reset_index()
        monthly["month_index"] = np.arange(len(monthly))

        if len(monthly) == 1:
            return round(float(monthly["Amount"].iloc[0]), 2)

        X = monthly[["month_index"]]
        y = monthly["Amount"]
        model = LinearRegression()
        model.fit(X, y)
        next_index = np.array([[len(monthly)]])
        prediction = float(model.predict(next_index)[0])

        # Expense cannot be negative.
        return round(max(0.0, prediction), 2)
