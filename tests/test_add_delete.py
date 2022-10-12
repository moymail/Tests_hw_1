import pytest
from main import add_new_document, delete_document


def test_add_new_document():
    assert (add_new_document('12345', 'passport', 'Иван Кузнецов', '3'))


def test_delete_document():
    assert (delete_document('11-2'))
