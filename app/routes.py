from flask import Blueprint, render_template

# This line defines 'bp' which our __init__.py is looking for
bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('index.html', title="LinuxQuest")
