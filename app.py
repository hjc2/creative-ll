from operator import contains
from flask import Flask, render_template, request

app = Flask(__name__)

high_score = 0  # Initialize the high score to 0


import openai

import OPEN_API_KEY

openai.api_key = OPEN_API_KEY.mykey

@app.route('/', methods=['GET', 'POST'])
def index():
    global high_score  # Use the global variable
    score = 0
    message = ''

    if request.method == 'POST':
        question = request.form['question']
        user_answer = request.form['user_answer']

        question = "How do we solve the isreal palestine conflict?"



        if decide(question, user_answer):
            message = 'Correct!'
            score = 1
        else:
            message = 'Incorrect!'

        if score > high_score:  # Update the high score if necessary
            high_score = score

        # message = apiQ(user_answer)


    return render_template('index.html', score=score, message=message, high_score=high_score)



def apiQ(content):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}],
        max_tokens=200,
        temperature = 0
    )
    return(completion['choices'][0]['message']['content'])


def decide(question, answer):
    content = "Question: " + question + " Answer: " + answer + " Prompt: Is this is a good answer to the question? Answer Yes or No."

    v = apiQ(content)

    #see if yes is in v
    if "Yes" in v:
        return True

    return False



if __name__ == '__main__':
    app.run()
