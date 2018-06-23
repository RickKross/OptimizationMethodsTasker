import os
import sys
from uuid import uuid4

from flask import Flask

from app.utils import A
from config import Config

kw = {'static_folder': 'static'}
if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    kw['template_folder'] = template_folder
    kw['static_folder'] = static_folder

app = Flask(__name__, **kw)

print('-' * 64,
      '',
      'Для прохождения задания необходимо в браузере перейти по адресу',
      'http://127.0.0.1:8080/',
      '',
      'При закрытии сервер остановистся и прогресс сбросится',
      '',
      '-' * 64, sep='\n')


app.config.from_object(Config)

app.secret_key = str(uuid4())

from app.views.base_view import base_view
