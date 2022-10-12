import pytest
from main import name_output, shelf_number_output

FIXTURES_1 = [
    ("2207 876234", "Василий Гупкин"),
    ("11-2", "Геннадий Покемонов"),
    ("10006", "Аристарх Павлов"),
    ("1234", None)
]

FIXTURES_2 = [
    ('2207 876234', '1'),
    ('11-2', '1'),
    ('5455 028765', '1'),
    ('10006', '2'),
    ('1234', None)
]


@pytest.mark.parametrize("doc_number, doc_name", FIXTURES_1)
def test_name_output(doc_number, doc_name):
    test_result = name_output(doc_number)
    assert doc_name == test_result


@pytest.mark.parametrize("doc_number,shelf_number", FIXTURES_2)
def test_shelf_number_output(doc_number, shelf_number):
    test_result_1 = shelf_number_output(doc_number)
    assert shelf_number == test_result_1
