import pytest

from employee_fixture import Employee


@pytest.fixture
def employee():
    employee = Employee('icaro', 'calado', 25_000)
    return employee


def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.salary == 35_000


def test_give_custom_raise(employee):
    employee.give_raise(25_000)
    assert employee.salary == 50_000
