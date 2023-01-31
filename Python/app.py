from flask import Flask
from surveys import Survey, Question

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return """
        <body>
        <h1>Welcome!</h1>
        <a href="/survey/"><button>Take Survey</button></a>
        </body>
    """

@app.route("/survey/")
def show_survey():
    return """
        <body>
        <h1>This is the Survey Page</h1>
        </body>
    """

if __name__ == '__main__':
    app.run()
