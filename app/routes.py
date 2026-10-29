from flask import Blueprint, render_template, request, redirect, url_for
from app.questions.ssh import QUESTIONS

bp = Blueprint('main', __name__)

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
