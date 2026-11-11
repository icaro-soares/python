from employee import Employee


def test_give_default_raise():
    employee = Employee('jonh', 'cena', 5_000)
    employee.give_raise()
    assert employee.salary == 10_000


def test_give_custom_raise():
    employee_2 = Employee('mark', 'zuckerberg', 10_000)
    employee_2.give_raise(15_000)
    assert employee_2.salary == 25_000