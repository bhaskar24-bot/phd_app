from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    return f"Welcome, {username}! (This is a placeholder - login not fully implemented yet.)"

if __name__ == '__main__':
    app.run(debug=True)