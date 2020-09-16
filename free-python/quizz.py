from guizero import App, TextBox, PushButton, Picture, Text
from random import randrange

questions = ['What Python function is equivalent to the Scratch "say" block ?',
             'What Python module contains the randint function ?',
             'Fill in the blank - pseudo____ ?']

answers = ['print',
           'random',
           'code']

def start():
    question.index_value = randrange(len(questions))
    question.value = questions[question.index_value]
    start.text = 'Next'
    check_answer.show()

def check():
    if input_box.value == answers[question.index_value]:
        question.value = 'Correct'
    else:
        question.value = 'Incorrect'

app = App(title='Quiz', width=500, height=300)
question = Text(app, text='Ready to start the quiz?')
input_box = TextBox(app, text='Answer')
check_answer = PushButton(app, command = check, text='Check answer')
check_answer.hide()
start = PushButton(app, command=start, text='Start')

app.display()