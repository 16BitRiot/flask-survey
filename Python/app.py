from flask import Flask, redirect, flash, session, url_for, render_template, request
from surveys import Survey, Question, personality_quiz as personality_quiz, surveys

app = Flask(__name__, template_folder="templates")
app.secret_key = "your_secret_key"

responses = []

@app.route("/question/<int:question_id>/")
def question(question_id):
    survey = surveys['personality']
    question = survey.questions[question_id-1]

    if 'responses' not in session:
        session['responses'] = {}

    if request.args:
        # save the response in the session
        session['responses'][question_id] = request.args['response']

        if len(session['responses']) == len(survey.questions):
            return redirect('/results/')

        return redirect(f"/question/{question_id+1}/")

    return render_template("question.html", question=question, question_id=question_id)


@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


@app.route('/start_survey', methods=['GET', 'POST'])
def start_survey():
    session['responses'] = []  # set session["responses"] to an empty list
    return redirect(url_for('question', question_id=1))  # redirect to the start of the survey


@app.route("/survey/")
def show_survey():
    survey = personality_quiz
    return render_template("survey.html", survey=survey)


@app.route("/response/<int:question_number>/<response>/", methods=['GET', 'POST'])
def handle_response(question_number, response):
    print(f"question_number: {question_number}")
    print(f"response: {response}")
    try:
        response = int(response)
    except ValueError:
        flash("Invalid response.")
        return redirect(url_for("question", question_id=question_number))


    # update the responses stored in the session
    session['responses'].append(response)

    # redirect to the next question or the completion page
    if question_number + 1 < len(personality_quiz.questions):
        return redirect(url_for("question", question_id=question_number + 2))


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
