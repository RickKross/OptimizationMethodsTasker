import time

from flask import Blueprint, render_template, url_for, redirect as redir, session, request

from app import app
from app.controllers.questions_controller import prepare_questions

base_view = Blueprint('vacancies_view', __name__, static_folder='static', template_folder='templates')


def redirect(endpoint, **values):
    return redir(url_for(endpoint, **values))


@app.route('/', methods=['GET'])
def index():
    return render_template('begin.html')


@app.route('/shuffle', methods=['get'])
def shuffle_tasks():
    prepare_questions()
    return redirect('question', idx=1)


@app.route('/check/', methods=['post'])
def check():
    pass


@app.route('/questions/<int:idx>', methods=['get'])
def question(idx):
    if not idx:
        return redirect('question', idx=idx + 1)

    try:
        tasks = session.get('tasks', [])
        if tasks is None:
            return redirect('index')
        question = tasks[idx - 1]
        if not isinstance(question, dict):
            raise IndexError
    except (IndexError, TypeError):
        session['finish'] = time.time() - session.get('start', time.time())
        return redirect('result')

    question.update({'number': idx})
    content = {
        'current_question': question,
        'total_questions': session['tasks_len'],
    }

    return render_template('question.html', **content)


@app.route('/answer/<int:idx>', methods=['post'])
def answer(idx):
    try:
        user_answer = None

        for ans_idx in request.form.values():
            user_answer = int(ans_idx)

        curr_task = session.get('tasks', [])[idx - 1]
        real_answers = curr_task['answers']

        if not real_answers:
            raise IndexError

        session['result'].append(real_answers[user_answer][1])
        session.modified = True

    except (IndexError, KeyError, ValueError, TypeError):
        print('-------ERROR-------')
        print('Error while parsing answer .-.')
        session['result'].append(False)
        session.modified = True

    return redirect('question', idx=idx + 1)


@app.route('/result', methods=['get'])
def result():
    success = len(list(filter(lambda x: x, session.get('result', []))))
    total = len(session.get('tasks', []))

    content = {
        'total_questions': total,
        'result': {
            'success': success,
            'time':  '%.2f сек' % session.get('finish', -1),
            'percent': ('%.2f%%' % (success / total * 100)) if total > 0 else '<Ошибка>'
        }
    }
    return render_template('result.html', **content)
