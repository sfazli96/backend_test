from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "caio!"


@app.route("/greet")
def greet():
    return "Good Morning"

if __name__ == '__main__':
    app.run(port=8500, debug=True)