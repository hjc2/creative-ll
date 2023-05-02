from operator import contains
from flask import Flask, render_template, request

import random


app = Flask(__name__)
high_score = 0  # Initialize the high score to 0
score = 0

import openai

import OPEN_API_KEY

openai.api_key = OPEN_API_KEY.mykey

@app.route('/', methods=['GET', 'POST'])
def index():
    global high_score  # Use the global variable
    global score
    message = ''

    if request.method == 'POST':
        user_answer = request.form['user_answer']
        question = request.form['question']


        if decide(question, user_answer):
            message = 'Correct!'
            score += 1

        else:
            message = explain(question, user_answer)
            score = 0
            # message = 'Incorrect!'

        if score > high_score:  # Update the high score if necessary
            high_score = score

        # message = apiQ(user_answer)

    question = apiQ("generate a hard question about politics and conflicts? Be specific. Make it short, less than 12 words Ex. Should we ban books that include hate speech? How do we solve the isreali palestinian conflict? How can governments address income inequality? How do we stop school shootings in America?")

    return render_template('index.html', score=score, message=message, high_score=high_score, question=question)



def apiQ(content):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}],
        max_tokens=150,
        temperature = 1
    )
    return(completion['choices'][0]['message']['content'])


def decide(question, answer):
    content = "Question: " + question + " Answer: " + answer + ". Prompt: Is this is a good answer to the question? Answer Yes or No."

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}],
        max_tokens=150,
        temperature = 0
    )

    v = completion['choices'][0]['message']['content']

    #see if yes is in v
    if "Yes" in v:
        return True

    return False

def explain(question, answer):
    content = "Question: " + question + " Answer: " + answer + ". Explain why this is a bad answer."
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}],
        max_tokens=100,
        temperature = 0
    )
    
    return(completion['choices'][0]['message']['content'])


if __name__ == '__main__':
    app.run()
