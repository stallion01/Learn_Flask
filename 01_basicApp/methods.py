from flask import Flask, request

app = Flask(__name__)


# @ signifies a decorator - way to wrap a function and modifying its behavior
@app.route('/')
def index():
    return "Method used: %s" % request.method

@app.route('/tuna')
def tuna():
    return '<h2>Tuna is good</h2>'


@app.route('/bacon', methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are probably using GET"


if __name__ == "__main__":
    app.run(debug=True)

