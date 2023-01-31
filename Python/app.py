from flask import Flask
from surveys import Survey, Question

app = Flask(__name__)

personality_quiz = Survey(
    "Rithm Personality Test",
    "Learn more about yourself with our personality quiz!",
    [
        Question("Do you ever dream about code?"),
        Question("Do you ever have nightmares about code?"),
        Question("Do you prefer porcupines or hedgehogs?",
                 ["Porcupines", "Hedgehogs"]),
        Question("Which is the worst function name, and why?",
                 ["do_stuff()", "run_me()", "wtf()"],
                 allow_text=True),
    ]
)

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
    survey = personality_quiz

    survey_html = f"<h1>{survey.title}</h1>"
    survey_html += f"<p>{survey.instructions}</p>"

    for question in survey.questions:
        survey_html += f"<p>{question.question}</p>"
        survey_html += "<ul>"
        for choice in question.choices:
            survey_html += f"<li>{choice}</li>"
        survey_html += "</ul>"

    return f"""
        <body>
        {survey_html}
        </body>
    """

if __name__ == '__main__':
    app.run()
