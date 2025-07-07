from flask import Flask, render_template
from data_simulator import generate_data
from behavior_analysis import analyze_behavior
from risk_model import risk_score
from premium_calculator import calculate_premium
from feedback import get_feedback

app = Flask(__name__)

@app.route('/')
def index():
    generate_data()
    df = analyze_behavior()
    score = risk_score(df)
    premium = calculate_premium(5000, score)
    suggestions = get_feedback(df)
    return render_template('index.html', score=score, premium=round(premium), tips=suggestions)

if __name__ == '__main__':
    app.run(debug=True)
