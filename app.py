from flask import Flask, render_template, request

app = Flask(__name__)

high_score = 0  # Initialize the high score to 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global high_score  # Use the global variable
    score = 0
    message = ''

    if request.method == 'POST':
        question = request.form['question']
        expected_answer = request.form['expected_answer']
        user_answer = request.form['user_answer']

        if user_answer.lower() == expected_answer.lower():
            message = 'Correct!'
            score = 1
        else:
            message = 'Incorrect!'

        if score > high_score:  # Update the high score if necessary
            high_score = score

    return render_template('index.html', score=score, message=message, high_score=high_score)

if __name__ == '__main__':
    app.run()
