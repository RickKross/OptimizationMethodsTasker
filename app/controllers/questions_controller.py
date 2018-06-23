import time
from contextlib import contextmanager
from random import shuffle

from flask import session

from app import app



def questions_gen():
    for idx, task in enumerate(session.get('tasks', []), start=1):
        answers = task['answers']
        shuffle(answers)

        print(idx)

        yield {
            'number': idx,
            'text': task['question'],
            'answers': answers,
        }


def prepare_questions():
    session.clear()
    session.new = True

    tasks = app.config.get('TASKS', {'theory': [], 'practice': []})
    theory_tasks = tasks['theory']
    practice_tasks = tasks['practice']

    shuffle(theory_tasks)
    shuffle(practice_tasks)

    limited_theory_tasks = theory_tasks[:app.config.get('THEORY_TASKS_TO_RESPOND', None)]
    limited_practice_tasks = practice_tasks[:app.config.get('PRACTICE_TASKS_TO_RESPOND', None)]

    all_tasks = limited_theory_tasks + limited_practice_tasks

    shuffle(all_tasks)
    for task in all_tasks:
        shuffle(task['answers'])

    session['tasks_len'] = len(all_tasks)
    session['tasks'] = all_tasks
    session['result'] = []
    session['start'] = time.time()


def _int(x, default=''):
    try:
        x = int(x)
    except:
        x = default
    return x


@contextmanager
def timeit():
    ts = time.time()

    yield

    print('-' * 30, 'Итого времени затрачено: %.2f секунд' % (time.time() - ts), sep='\n')