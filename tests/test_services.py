from employee_manager.models import Employee
from employee_manager.services import (
    calculate_average_salary,
    calculate_total_payroll,
    filter_by_department,
    find_highest_paid_employee,
)


def create_sample_employees() -> list[Employee]:

    return [
        Employee(
            name="Anna Kolesnik",
            position="Manager",
            department="Sales",
            salary=1200.0,
        ),
        Employee(
            name="Oleh Ivanenko",
            position="Developer",
            department="IT",
            salary=2500.0,
        ),
        Employee(
            name="Iryna Petrenko",
            position="Accountant",
            department="Finance",
            salary=1800.0,
        ),
    ]


def test_filter_by_department() -> None:
    employees = create_sample_employees()

    result = filter_by_department(employees, "IT")

    assert len(result) == 1
    assert result[0].name == "Oleh Ivanenko"


def test_filter_by_department_case_insensitive() -> None:
    employees = create_sample_employees()

    result = filter_by_department(employees, "it")

    assert len(result) == 1


def test_calculate_average_salary() -> None:
    employees = create_sample_employees()

    average = calculate_average_salary(employees)

    assert average == 1833.3333333333333


def test_calculate_average_salary_empty_list() -> None:
    average = calculate_average_salary([])

    assert average == 0.0


def test_find_highest_paid_employee() -> None:
    employees = create_sample_employees()

    best = find_highest_paid_employee(employees)

    assert best is not None
    assert best.name == "Oleh Ivanenko"


def test_find_highest_paid_employee_empty_list() -> None:
    best = find_highest_paid_employee([])

    assert best is None


def test_calculate_total_payroll() -> None:
    employees = create_sample_employees()

    total = calculate_total_payroll(employees)

    assert total == 5500.0