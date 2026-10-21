from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('main', __name__)

# Questions Data Structure
QUESTIONS = [
    {
        "id": 1,
        "question": "When you connect to a remote server via SSH, where must the SSH daemon (sshd) be active and running to maintain the connection?",
        "choices": [
            "Both sides need to run an SSH daemon.",
            "Only on the client side.",
            "Only on the server side.",
            "None of the sides need a daemon."
        ],
        "correct": 3  # "Only on the server side."
    },
    {
        "id": 2,
        "question": "Which elliptic-curve algorithm is widely used as a default for secure key exchange (KEX) during an SSH handshake in modern Linux systems?",
        "choices": [
            "Ed25519",
            "Curve25519",
            "Diffie-Hellman-Group1-SHA1",
            "RSA"
        ],
        "correct": 2  # "Curve25519"
    }
    {
        "id": 3,
        "question": "Which of the following statements is true regarding how the `scp` command works?",
        "choices": [
            "scp needs an active live SSH connection to transfer files.",
            "scp does not need an SSH active connection to transfer files.",
            "scp can be used to move files from a remote host to another remote host only.",
            "scp can be used to move files remote to local or local to remote only."
        ],
        "correct": 1  # Option 1 is correct
    }
]


@bp.route('/')
def home():
    return render_template('index.html', title="LinuxQuest")


# Redirect /quiz to the first question automatically
@bp.route('/quiz')
def quiz():
    return redirect(url_for('main.quiz_question', q_id=1))


# Dynamic route that handles any question number (1, 2, 3...)
@bp.route('/quiz/<int:q_id>', methods=['GET', 'POST'])
def quiz_question(q_id):
    # Find the question with matching ID (or return None if index out of bounds)
    question = next((q for q in QUESTIONS if q["id"] == q_id), None)

    if not question:
        return "<h1>Quiz Finished or Question Not Found!</h1>", 404

    if request.method == 'POST':
        selected_answer = request.form.get('answer')
        
        if not selected_answer:
            return render_template('quiz.html', title=f"LinuxQuest | Question {q_id}", q=question, error="Please select an answer!")

        # Calculate next question ID
        next_q_id = q_id + 1
        has_next = any(q["id"] == next_q_id for q in QUESTIONS)

        is_correct = int(selected_answer) == question['correct']

        # For now, progress to next question if available
        if has_next:
            return redirect(url_for('main.quiz_question', q_id=next_q_id))
        else:
            return "<h1>Quiz Completed!</h1><p>More questions are on the way</p>"

    return render_template('quiz.html', title=f"LinuxQuest | Question {q_id}", q=question)
