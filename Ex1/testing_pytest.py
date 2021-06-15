import pytest
from main import people
from data import *

class TestSomething_:
    def setup(self):
        print('method setUp')

    @pytest.mark.parametrize('a, b, expected_result', [(documents, '11-2', "Геннадий Покемонов"), (documents, '10006', "Аристарх Павлов"), (documents, '111', 'Нет такого номера документа')])
    def test_people(self, a, b, expected_result):
        assert people(a, b) == expected_result

    def teardown(self):
        print('method tearDown')

