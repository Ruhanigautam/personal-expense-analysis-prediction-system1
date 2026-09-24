from flask import Flask, render_template, request, jsonify
from model import ExpensePredictor
from utils import load_expenses, save_expense, category_summary, monthly_summary, build_forecast_data

app = Flask(__name__)
predictor = ExpensePredictor()
DATA_PATH = "data/expenses.csv"

@app.route("/")
def index():
    df = load_expenses(DATA_PATH)
    summary = category_summary(df)
    monthly = monthly_summary(df)
    forecast = predictor.predict_next_month(df)
    return render_template(
        "index.html",
        total=float(df["Amount"].sum()) if not df.empty else 0,
        transactions=len(df),
        categories=summary.to_dict("records"),
        monthly=monthly.to_dict("records"),
        forecast=forecast,
        expenses=df.tail(10).sort_values("Date", ascending=False).to_dict("records")
    )

@app.route("/add", methods=["POST"])
def add():
    data = request.form
    try:
        amount = float(data["amount"])
        if amount <= 0:
            raise ValueError
        save_expense(DATA_PATH, data["date"], data["category"], amount, data.get("description", ""))
        return jsonify({"success": True})
    except Exception:
        return jsonify({"success": False, "message": "Please enter valid expense details."}), 400

@app.route("/api/summary")
def api_summary():
    df = load_expenses(DATA_PATH)
    return jsonify({
        "category": category_summary(df).to_dict("records"),
        "monthly": monthly_summary(df).to_dict("records"),
        "forecast": predictor.predict_next_month(df)
    })

if __name__ == "__main__":
    app.run(debug=True)
