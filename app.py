from flask import Flask, render_template, url_for, flash
import json
app = Flask(__name__)

@app.route('/')
def home():
    with open('rotten.json', 'r') as mv:
        movie = json.load(mv)
    return render_template('home.html', movies=movie)

if __name__ == '__main__':
    app.run(debug=True)