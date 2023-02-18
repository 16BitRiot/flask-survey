from flask import Flask, redirect, flash, session, url_for, render_template
from surveys import Survey, Question, personality_quiz as personality_quiz

app = Flask(__name__, template_folder="templates")
app.secret_key = "your_secret_key"

responses = []

@app.route("/question/<int:question_number>/")
def show_question(question_number):
    if question_number >= len(personality_quiz.questions):
        flash("Invalid request: that question does not exist.")
        return redirect(url_for("goodbye"))
    question = personality_quiz.questions[question_number]
    return render_template("question.html", question=question, question_number=question_number)

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


@app.route('/start_survey', methods=['GET', 'POST'])
def start_survey():
    session['responses'] = []  # set session["responses"] to an empty list
    return redirect(url_for('show_question', question_number=0))  # redirect to the start of the survey

# @app.route('/start_survey', methods=['GET'])
# def start_survey_get():
#     return redirect(url_for('welcome'))


@app.route("/survey/")
def show_survey():
    survey = personality_quiz
    return render_template("survey.html", survey=survey)


@app.route("/response/<int:question_number>/<response>/")
def handle_response(question_number, response):
    try:
        response = int(response)
    except ValueError:
        flash("Invalid response.")
        return redirect(url_for("show_question", question_number=question_number))

    # update the responses stored in the session
    session['responses'].append(response)

    # redirect to the next question or the completion page
    if question_number + 1 < len(personality_quiz.questions):
        return redirect(url_for('show_question', question_number=question_number + 1))
    else:
        return redirect(url_for('show_results'))


@app.route("/results/", methods=['GET', 'POST'])
def show_results():
    # get the user's responses
    responses = session.get('responses')

    # clear the responses from the session
    session.pop('responses', None)

    return render_template("results.html", responses=responses)



if __name__ == '__main__':
    app.run(debug=True)
