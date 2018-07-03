from random import randint

from app import app

if __name__ == '__main__':

    try:
        print('Введите номер порта, на котором будет запущен сервер. Диапазон [8000; 60000]')
        port = int(input("Или нажмите <Enter> для выбора случайного: "))

        if port < 8000 or port > 60000 or not port:
            raise ValueError
    except:
        port = randint(8000, 60000)

    print('-' * 64,
          '',
          'Для прохождения задания необходимо в браузере перейти по адресу',
          'http://127.0.0.1:%s/' % port,
          '',
          'При закрытии сервер остановистся и прогресс сбросится',
          '',
          '-' * 64, sep='\n')
    app.run(port=port, debug=True, use_reloader=False)
