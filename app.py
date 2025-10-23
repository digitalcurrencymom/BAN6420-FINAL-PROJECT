import os
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from user import User

app = Flask(__name__)

# MongoDB configuration
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(MONGO_URI)
db = client['survey_db']
users_col = db['users']

EXPENSE_CATEGORIES = ['utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', categories=EXPENSE_CATEGORIES)

@app.route('/submit', methods=['POST'])
def submit():
    # Collect basic fields
    age = request.form.get('age')
    gender = request.form.get('gender')
    total_income = request.form.get('total_income')

    # Collect expenses
    expenses = {}
    for cat in EXPENSE_CATEGORIES:
        enabled = request.form.get(f'{cat}_enabled')
        amount = request.form.get(f'{cat}_amount')
        if enabled and amount:
            try:
                expenses[cat] = float(amount)
            except ValueError:
                expenses[cat] = 0.0
        else:
            expenses[cat] = 0.0

    user = User(age=age, gender=gender, total_income=total_income, expenses=expenses)
    doc = user.to_dict()
    users_col.insert_one(doc)

    return render_template('thankyou.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
