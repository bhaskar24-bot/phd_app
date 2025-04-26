from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create the SQLite database and table if they don't exist
def init_db():
    conn = sqlite3.connect('experiments.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS predictions
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data TEXT NOT NULL,
                    result TEXT NOT NULL,
                    date TEXT NOT NULL)''')
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    return render_template('index.html')

@app.route('/yield')
def yield_page():
    return render_template('yield.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form['data']
    # Simple mock prediction (replace with real logic later)
    try:
        predicted_yield = float(data) * 1.1  # Mock: increase by 10%
        result = f"Predicted yield: {predicted_yield:.2f}%"
    except ValueError:
        result = "Error: Please enter a valid number for yield data."

    # Save to SQLite
    conn = sqlite3.connect('experiments.db')
    conn.execute("INSERT INTO predictions (data, result, date) VALUES (?, ?, datetime('now'))", (data, result))
    conn.commit()
    conn.close()

    return render_template('yield.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)