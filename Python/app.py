from flask import Flask
from Python.surveys import Survey, Question
app = Flask(__name__)

@app.route("/welcome")
def hello():
    return """
        <body>
        <h1>Welcome!</h1>
        </body>
    """

if __name__ == '__main__':
    app.run()