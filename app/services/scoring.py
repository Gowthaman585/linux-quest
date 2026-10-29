# app/services/quiz_logic.py

from flask import session
from app.questions.ssh import QUESTIONS

def init_quiz_session():
    session['answers'] = {}
    session['score'] = 0

def process_answer(question_id, selected_choice):
    if 'answers' not in session:
        session['answers'] = {}
        
    question = QUESTIONS[question_id - 1]
    is_correct = (selected_choice == question['correct'])
    
    answers = session['answers']
    answers[str(question_id)] = {
        'selected': selected_choice,
        'correct': is_correct
    }
    session['answers'] = answers
    
    # Recalculate score
    score = sum(1 for a in answers.values() if a['correct'])
    session['score'] = score
    return is_correct

def get_quiz_results():
    total = len(QUESTIONS)
    score = session.get('score', 0)
    percentage = int((score / total) * 100) if total > 0 else 0
    return score, total, percentage
