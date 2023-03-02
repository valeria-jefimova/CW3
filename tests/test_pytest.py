import pytest
from utils import get_last_data, get_formatted_data, get_filtred_data


@pytest.fixture
def test_data():
    return [
        {'id': 441945886,
         'state': 'EXECUTED',
         'date': '2019-08-26T10:50:58.294041',
         'description': 'Перевод организации',
         'from': 'Maestro 1596837868705199',
         'to': 'Счет 64686473678894779589',
         'operationAmount': {'amount': '31957.58',
                             'currency': {'name': 'руб.', 'code': 'RUB'}}},
        {'id': 441428829,
         'state': 'EXECUTED',
         'date': '2019-07-03T18:35:29.512364',
         'description': 'Перевод организации',
         'from': 'MasterCard 7158300734726758',
         'to': 'Счет 35383033474447895560',
         'operationAmount': {'amount': '8221.37',
                             'currency': {'name': 'USD', 'code': 'USD'}}},
        {'id': 939719570,
         'state': 'EXECUTED',
         'date': '2018-06-30T02:08:58.425572',
         'description': 'Перевод организации',
         'from': 'Счет 75106830613657916952',
         'to': 'Счет 11776614605963066702',
         'operationAmount': {'amount': '9824.07',
                             'currency': {'name': 'USD', 'code': 'USD'}}},
        {'id': 587085106,
         'state': 'EXECUTED',
         'date': '2018-03-23T10:45:06.972075',
         'description': 'Открытие вклада',
         'to': 'Счет 41421565395219882431',
         'operationAmount': {'amount': '48223.05',
                             'currency': {'name': 'руб.', 'code': 'RUB'}}},
        {'id': 142264268,
         'state': 'CANCELED',
         'date': '2019-04-04T23:20:05.206878',
         'description': 'Перевод со счета на счет',
         'from': 'Счет 19708645243227258542',
         'to': 'Счет 75651667383060284188',
         'operationAmount': {'amount': '79114.93',
                             'currency': {'name': 'USD', 'code': 'USD'}}}
    ]



# def test_get_data(test_data):
#     url = operations.BANK_TRANSACTION_DATA
#     assert operations.json_reader(url)


def test_get_filtered_data(test_data):
    assert len(get_filtred_data(test_data)) == 4
    assert len(get_filtred_data(test_data, filtered_empty_from=True)) == 2


def test_get_last_data(test_data):
    data = get_last_data(test_data, count_last_values=2)
    assert data[0]['date'] == '2019-08-26T10:50:58.294041'
    assert len(data) == 2



def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data[:1])
    assert data == ['07.17.2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> Счет **3655\n48150.39 USD\n']