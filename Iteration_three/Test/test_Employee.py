import pytest
from Iteration_three.Model.Employee import Employee


@pytest.fixture
def my_emp():
    return Employee('jsw833', 'ellen1234', 'Ellen', 'Jensen', '45456576', 'Ellen@jensen.dk', '241094-0202')


def test_get_age(my_emp):

    assert my_emp.get_age() == 27


def test_get_gender(my_emp):

    assert my_emp.get_gender() == "female"
