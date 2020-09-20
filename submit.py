from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('make_profile.html')


@app.route("/result", methods='POST')
def result():
    timer = request.form['timer_input']
    log_message = "Water every {} days".format(timer)
    screen_message = "Sure, will water every {} days!".format(timer)
    save(log_message)
    return screen_message


def save(text, filepath='timer.txt'):
    with open("timer.txt", "w") as f:
        f.write(text)
