import pytest

from utils import get_last_data, get_formatted_data, get_filtred_data


def test_get_data(test_data):
    url = operations.BANK_TRANSACTION_DATA
    assert operations.json_reader(url)


def test_get_filtered_data(test_data):
    assert len(get_filtred_data(test_data)) == 3
    assert len(get_filtred_data(test_data, filtered_empty_from=True)) == 2


def test_get_last_data(test_data):
    data = get_last_data(test_data, count_last_values=2)
    assert data[0]['date'] == '2019-08-26T10:50:58.294041'
    assert len(data) == 2


def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data[:1])
    assert data == ['07.17.2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> Счет **3655\n48150.39 USD\n']