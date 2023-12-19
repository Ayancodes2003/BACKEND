from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')
@app.route("/about")
def oli():
    return "<p>Hello, World!</p>"
app.run(debug=True)