from flask import Blueprint, render_template

# This line defines 'bp' which our __init__.py is looking for
bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('index.html', title="LinuxQuest")
@bp.route('/quiz')
def quiz():
    # Our first real Linux question!
    question_data = {
        "id": 1,
        "question": "When you connect to a remote server via SSH, where must the SSH daemon (sshd) be active and running to maintain the connection?",
        "choices": [
            "Both sides need to run an SSH daemon.",
            "Only on the client side.",
            "Only on the server side.",
            "None of the sides need a daemon."
        ]
    }
    return render_template('quiz.html', title="LinuxQuest | Question 1", q=question_data)
