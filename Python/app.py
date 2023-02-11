from flask import Flask, redirect
from surveys import Survey, Question

app = Flask(__name__)

responses = []

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
    survey_html += f"<a href='/question/1/'><button>Click here to get started!</button></a>"

    return f"""
        <body>
        {survey_html}
        </body>
    """


@app.route("/question/1/")
def show_question1():
    question = personality_quiz.questions[0]
    question_html = f"<p>{question.question}</p>"
    question_html += "<ul>"
    question_html += f"<li><a href='/response/1/yes/'><button>Yes</button></a></li>"
    question_html += f"<li><a href='/response/1/no/'><button>No</button></a></li>"
    question_html += "</ul>"

    return f"""
    <body>
    {question_html}
    </body>
    """


@app.route("/response/1/<response>/")
def add_response1(response):
    responses.append(response)
    return redirect(f"/question/2/")


@app.route("/question/2/")
def show_question2():
    question = personality_quiz.questions[1]
    question_html = f"<p>{question.question}</p>"
    question_html += "<ul>"
    question_html += f"<li><a href='/response/2/yes/'><button>Yes</button></a></li>"
    question_html += f"<li><a href='/response/2/no/'><button>No</button></a></li>"
    question_html += "</ul>"

    return f"""
    <body>
    {question_html}
    </body>
    """


@app.route("/response/2/<response>/")
def add_response2(response):
    responses.append(response)
    print(response)
    return redirect(f"/question/3/")


@app.route("/question/3/")
def show_question3():
    question = personality_quiz.questions[2]
    question_html = f"<p>{question.question}</p>"
    question_html += "<ul>"
    question_html += f"<li><a href='/response/3/porcupines/'><button>porcupines</button></a></li>"
    question_html += f"<li><a href='/response/3/hedgehogs/'><button>hedgehogs</button></a></li>"
    question_html += "</ul>"

    return f"""
    <body>
    {question_html}
    </body>
    """


@app.route("/response/3/<response>/")
def add_response3(response):
    responses.append(response)
    print(response)
    return redirect(f"/question/4/")


@app.route("/question/4/")
def show_question4():
    question = personality_quiz.questions[3]
    question_html = f"<p>{question.question}</p>"
    question_html += "<ul>"
    question_html += f"<li><a href='/response/4/yes/'><button>Yes</button></a></li>"
    question_html += f"<li><a href='/response/4/no/'><button>No</button></a></li>"
    question_html += "</ul>"

    return f"""
    <body>
    {question_html}
    </body>
    """


@app.route("/response/4/<response>/")
def add_response4(response):
    responses.append(response)
    print(response)
    question1 = personality_quiz.questions[0]
    question2 = personality_quiz.questions[1]
    question3 = personality_quiz.questions[2]
    question4 = personality_quiz.questions[3]


    return f"""
    You have completed the survey. Thank you for participating!

    <ul>
        <li>{question1.question}: {responses[0]}</li>
        <li>{question2.question}: {responses[1]}</li>
        <li>{question3.question}: {responses[2]}</li>
        <li>{question4.question}: {responses[3]}</li>
    </ul>
    """


if __name__ == '__main__':
    app.run()
