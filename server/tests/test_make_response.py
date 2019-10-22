
import pytest

from datetime import datetime

from protocol import make_response

'''

Данный скрипт тестирует модуль protocol, в частности функцию make_response

'''


CODE = 200

ACTION = 'test'

TIME = datetime.now().timestamp() # фиксирует время выполнения скрипта

DATA = 'some client data'

# Зададим аргументы-константы для подстановки в тестируемую функцию
REQUEST = {
    'action': ACTION,
    'time': TIME,
    'data': 'some client data'
}

# каждый тест проверяет, что проходя через тестируемую функцию результат после обработки функцией соответствует ожидаемому.
def test_action_make_response():
    response = make_response(REQUEST, CODE, DATA, date=TIME)
    action = response.get('action')
    assert action == ACTION


def test_code_make_response():
    response = make_response(REQUEST, CODE, DATA, date=TIME)
    action = response.get('code')
    assert action == CODE


def test_time_make_response():
    response = make_response(REQUEST, CODE, DATA, date=TIME)
    action = response.get('time')
    assert action == TIME


def test_data_make_response():
    response = make_response(REQUEST, CODE, DATA, date=TIME)
    action = response.get('data')
    assert action == DATA

# Проверка на примере заранее известной ошибки
def test_none_request_make_response():
    with pytest.raises(AttributeError):
        response = make_response(None, CODE)
