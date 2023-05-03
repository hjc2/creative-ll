

# importing all the libraries

from operator import contains
from flask import Flask, render_template, request


import values

import openai

import OPEN_API_KEY # we need the API key and its hidden in a seperate local file

app = Flask(__name__)

#Score Values for tracking gameplay
high_score = 0
score = 0


# setting up the API key to be ready for use
openai.api_key = OPEN_API_KEY.mykey



# main page for the website
@app.route('/', methods=['GET', 'POST'])
def index():
    global high_score  # Use the global variable
    global score
    message = ''

    if request.method == 'POST': # If the user has submitted an answer, check if it is correct
        user_answer = request.form['user_answer'] # get the answer from the user
        question = request.form['question'] # get the question from the page


        if decide(question, user_answer): # if the answer is correct, it will say so, and continue the game
            message = 'Correct!'
            score += 1

        else:
            message = explain(question, user_answer) # if the answer is incorrect, it will explain why
            score = 0

        if score > high_score:  # Update the high score if necessary
            high_score = score

    # generates the next question
    question = apiQ(values.qgen)

    return render_template('index.html', score=score, message=message, high_score=high_score, question=question) # updates the page with the new question and score


# generates a question based on the question prompt
def apiQ(content):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}],
        max_tokens=150,
        temperature = 1
    )
    return(completion['choices'][0]['message']['content'])



# decides if an answer is correct or not

def decide(question, answer):
    content = values.decideGen(question, answer)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}],
        max_tokens=150,
        temperature = 0
    )

    v = completion['choices'][0]['message']['content']

    g = values.yesNo(v)
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": g}],
        max_tokens=150,
        temperature = 0
    )
    z = completion['choices'][0]['message']['content']

    print("v: " + v)
    print("z: " + z)
    
    #see if yes is in v
    if "Yes" in v:

        return True

    return False


# writes the explanation as to why an answer is incorrect

def explain(question, answer):

    content = values.explainGen(question, answer)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}],
        max_tokens=100,
        temperature = 0
    )
    
    return(completion['choices'][0]['message']['content'])

# runs the app
if __name__ == '__main__':
    app.run()
