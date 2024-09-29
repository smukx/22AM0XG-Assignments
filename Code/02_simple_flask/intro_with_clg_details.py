from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Guys ' + 'Its me Kavin ' + '7376222AL156 ' + 'Dept of AIML '

if __name__ == '__main__':
    app.run(debug=True)
