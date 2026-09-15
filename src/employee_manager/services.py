from employee_manager.models import Employee


def filter_by_department(
    employees: list[Employee],
    department: str,
) -> list[Employee]:

    return [
        employee
        for employee in employees
        if employee.department.lower() == department.lower()
    ]


def calculate_average_salary(
    employees: list[Employee],
) -> float:
    if not employees:
        return 0.0

    total = sum(
        employee.salary
        for employee in employees
    )

    return total / len(employees)


def find_highest_paid_employee(
    employees: list[Employee],
) -> Employee | None:
    if not employees:
        return None

    return max(
        employees,
        key=lambda employee: employee.salary,
    )


def calculate_total_payroll(
    employees: list[Employee],
) -> float:

    return sum(
        employee.salary
        for employee in employees
    )