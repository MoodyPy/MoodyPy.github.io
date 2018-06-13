from flask import Flask, render_template, jsonify, redirect

app = Flask(__name__)

@app.route('/')
def index():
    text = 'Hi My name is pratham'
    return render_template('index.html',text = text)

if __name__ == "__main__":
    app.run(debug=True)